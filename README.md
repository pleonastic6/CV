# ROC und Precision-Recall

Arbeitsstand des Computer-Vision-Bonusprojekts: ROC- und Precision-Recall-Darstellungen anhand zweier **simulierter Scorequellen** vergleichen und den Einfluss der Klassenverteilung untersuchen.

**Status:** Arturos tatsächlich bearbeitetes Notebook liegt als `01_start.ipynb` im Repo. Nur die veraltete erste/letzte Markdown-Zelle wurden redaktionell korrigiert und eine leere Codezelle entfernt; seine neun nichtleeren Codezellen blieben unverändert. Das unveränderte Original bleibt privat im Projektarchiv, nicht im Repo. `roc_pr.ipynb` ist die bereits zuvor erstellte alternative Zusammenführung derselben Lernschritte. Beide sind ausführbare **Arbeitsstände**, keine als fertig deklarierte Projektabgabe.

## Einstieg

1. Python **3.13** verwenden; mit 3.13.5 geprüft.
2. Virtuelle Umgebung erstellen und aktivieren:

   ```bash
   python -m venv .venv
   # Linux/macOS:
   source .venv/bin/activate
   # Windows PowerShell alternativ:
   # .venv\Scripts\Activate.ps1
   python -m pip install -r requirements-dev.txt
   ```

3. **Mit `01_start.ipynb` anfangen** – das ist Arturos Notebook. In einem Jupyter-kompatiblen Editor öffnen, den Interpreter der `.venv` auswählen und alle Zellen von oben nach unten ausführen.
4. Alternativ den vollständigen Notebook-Durchlauf ohne Editor prüfen:

   ```bash
   python tools/check_notebook.py
   ```

   Dabei werden **beide** Notebooks nacheinander in jeweils einem neuen Python-Kernel geprüft. Die geprüften Ausgaben werden unter `build/` gespeichert; die versionierten Notebooks bleiben unverändert.

## Inhalt

- `01_start.ipynb`: Arturos geprüftes Notebook mit seinen unveränderten Codezellen und korrigiertem Einleitungs-/Schlusstext; **dies ist der Einstieg**.
- `roc_pr.ipynb`: die zuvor von Vesper zusammengeführte Alternative mit zusätzlichen Erklärungen und Regressionsprüfungen. **Nicht parallel als zweite Lösung bearbeiten.**
- `lernzellen/`: ursprüngliches Start-Notebook und unveränderte einzelne Python-Lernzellen. Die `.py`-Dateien sind **Notebook-Zellen**, keine unabhängig startbaren Programme; sie verwenden Variablen aus den vorherigen Schritten.
- `figures/`: bereits erzeugte PNG-Grafiken der Lernschritte. Die aktuellen Grafiken können zusätzlich direkt im zusammengeführten Notebook erzeugt werden.
- `requirements.txt`: geprüfte Versionen der beiden direkten Analyseabhängigkeiten.
- `requirements-dev.txt`: zusätzlich die Werkzeuge für Notebook-Kernel und automatisierten Durchlauf. Kein vollständiger plattformübergreifender Lockfile.
- `tools/check_notebook.py`: strukturelle Validierung und echte saubere Kernel-Durchläufe beider Notebooks; vergleicht die vier AUC/AP-Ausgaben mit den bekannten Werten und prüft die Accuracy-Baseline.

## Versuchsaufbau

- Acht konstruierte Fälle: drei positive und fünf negative Labels.
- Zwei bewusst vorgegebene Scorequellen A/B, kein Training und kein realer Bilddatensatz.
- Positive Vorhersage bei `score >= schwelle`.
- Für die zweite Verteilung wird jedes negative Label samt zugehörigem Score 20-mal wiederholt. Positive Fälle bleiben unverändert. So entstehen 103 Einträge, davon drei positiv – **keine 103 unabhängigen Beobachtungen**.
- ROC-Darstellung und beschriftete PR-Messpunkte, Verteilungsvergleich, Immer-negativ-Baseline, Vergleich der Scorequellen sowie ROC-AUC und Average Precision.

Average Precision wird mit `average_precision_score` berechnet. Sie wird nicht als trapezförmige PR-Fläche oder als Precision bei einer einzelnen Schwelle bezeichnet.

## Grenzen und offene Abgabe-Arbeit

- Der kleine deterministische Versuch veranschaulicht Zusammenhänge; er belegt keine Generalisierung eines trainierten Modells.
- Scorequelle B ist absichtlich günstiger konstruiert. Ihr Vorteil ist keine unabhängig gemessene reale Modellverbesserung.
- Die ursprüngliche Verteilung ist 3/8 positiv und damit nicht exakt ausgeglichen.
- Die im Kontrollversuch identischen ROC-Punkte entstehen durch die erhaltenen klassenbedingten Scoreverteilungen. Eine beliebige neue Stichprobe muss nicht dieselbe ROC ergeben.
- PR zeigt hier einzelne gemessene Schwellenpunkte; diese werden nicht künstlich geglättet.
- Noch offen: Anwendungsempfehlung gemeinsam begründen, Grenzen/Quellen final ausarbeiten sowie Dokumentation und Präsentation fertigstellen.

Die Inhalte wurden mit KI-Unterstützung schrittweise erarbeitet. Vor einer Abgabe müssen die Beteiligten die Schritte nachvollziehen, fachlich prüfen und gemäß den Kursregeln dokumentieren. Vorlesungsunterlagen, Kurszugänge, virtuelle Umgebungen und persönliche Notizen sind nicht Bestandteil dieses Repositories.
