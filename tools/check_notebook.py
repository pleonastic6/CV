"""Validate and execute the project notebook in a fresh current-interpreter kernel."""
from pathlib import Path
import re
import sys

import nbformat
from jupyter_client import KernelManager
from nbclient import NotebookClient


def check_one(root, filename):
    notebook = nbformat.read(root / filename, as_version=4)
    nbformat.validate(notebook)
    manager = KernelManager(kernel_name='python3')
    # Use this interpreter, not an unrelated system/default Jupyter kernel.
    manager.kernel_spec.argv = [sys.executable, '-m', 'ipykernel_launcher',
                                '-f', '{connection_file}']
    client = NotebookClient(notebook, km=manager, timeout=120,
                            resources={'metadata': {'path': str(root)}})
    try:
        executed = client.execute()
    finally:
        if manager.has_kernel:
            manager.shutdown_kernel(now=True)
        manager.cleanup_resources()
    nbformat.validate(executed)
    code = [cell for cell in executed.cells if cell.cell_type == 'code']
    assert code and all(cell.execution_count is not None for cell in code)
    errors = [output for cell in code for output in cell.get('outputs', [])
              if output.output_type == 'error']
    assert not errors, 'Notebook contains execution errors'
    streams = '\n'.join(output.get('text', '') for cell in code
                        for output in cell.get('outputs', []) if output.output_type == 'stream')
    metric_pairs = re.findall(
        r'ROC-AUC:\s*([0-9.]+)\s*Average Precision \(AP\):\s*([0-9.]+)', streams)
    assert metric_pairs == [('0.6667', '0.6984'), ('0.6667', '0.3757'),
                            ('0.9333', '0.9167'), ('0.9333', '0.7101')], metric_pairs
    assert 'Accuracy: 97.1%' in streams and 'Recall: 0.0%' in streams
    if filename == 'roc_pr.ipynb':
        assert 'Alle Ergebnisprüfungen bestanden.' in streams
    output = root / 'build' / (Path(filename).stem + '.executed.ipynb')
    output.parent.mkdir(exist_ok=True)
    nbformat.write(executed, output)
    figures = sum('image/png' in item.get('data', {}) for cell in code
                  for item in cell.get('outputs', []))
    assert figures == 3, f'{filename}: expected 3 plot outputs, got {figures}'
    print(f'OK {filename}: {len(code)} code cells, {figures} plots, known results verified')
    print(output)


def main():
    root = Path(__file__).resolve().parents[1]
    for filename in ('01_start.ipynb', 'roc_pr.ipynb'):
        check_one(root, filename)


if __name__ == '__main__':
    main()
