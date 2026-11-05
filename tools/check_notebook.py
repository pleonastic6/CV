"""Validate and execute the project notebook in a fresh current-interpreter kernel."""
from pathlib import Path
import sys

import nbformat
from jupyter_client import KernelManager
from nbclient import NotebookClient


def main():
    root = Path(__file__).resolve().parents[1]
    notebook = nbformat.read(root / 'roc_pr.ipynb', as_version=4)
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
    last_text = ''.join(output.get('text', '') for output in code[-1].get('outputs', []))
    assert 'Alle Ergebnisprüfungen bestanden.' in last_text
    output = root / 'build' / 'roc_pr.executed.ipynb'
    output.parent.mkdir(exist_ok=True)
    nbformat.write(executed, output)
    figures = sum('image/png' in item.get('data', {}) for cell in code
                  for item in cell.get('outputs', []))
    print(f'OK: {len(code)} code cells, {figures} plot outputs, no execution errors')
    print(last_text.strip())
    print(output)


if __name__ == '__main__':
    main()
