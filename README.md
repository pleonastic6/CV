# ROC und Precision-Recall

Arbeitsstand des Computer-Vision-Bonusprojekts: ROC- und Precision-Recall-Darstellungen anhand zweier **simulierter Scorequellen** vergleichen und den Einfluss der Klassenverteilung untersuchen.

**Status:** Der bisher gemeinsam erarbeitete praktische Versuch ist hier zusammengeführt. Dies ist keine als fertig deklarierte Projektabgabe. Das auf dem Laptop weiterbearbeitete persönliche Notebook wurde noch nicht übernommen; `roc_pr.ipynb` ist eine nachvollziehbare Zusammenführung der vorhandenen Lernschritte mit den bislang verwendeten Daten.

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

3. `roc_pr.ipynb` in einem Jupyter-kompatiblen Notebook-Editor öffnen und den Interpreter der `.venv` auswählen. Danach alle Zellen von oben nach unten ausführen.
4. Alternativ den vollständigen Notebook-Durchlauf ohne Editor prüfen:

   ```bash
   python tools/check_notebook.py
   ```

   Dabei wird ein neuer Python-Kernel gestartet. Die geprüfte Ausgabe wird unter `build/roc_pr.executed.ipynb` gespeichert; das versionierte Notebook bleibt unverändert.

## Inhalt

- `roc_pr.ipynb`: zusammengeführter Versuch mit Erklärungen, Code und tatsächlich ausgeführten Ausgaben.
- `lernzellen/`: ursprüngliches Start-Notebook und unveränderte einzelne Python-Lernzellen. Die `.py`-Dateien sind **Notebook-Zellen**, keine unabhängig startbaren Programme; sie verwenden Variablen aus den vorherigen Schritten.
- `figures/`: bereits erzeugte PNG-Grafiken der Lernschritte. Die aktuellen Grafiken können zusätzlich direkt im zusammengeführten Notebook erzeugt werden.
- `requirements.txt`: geprüfte Versionen der beiden direkten Analyseabhängigkeiten.
- `requirements-dev.txt`: zusätzlich die Werkzeuge für Notebook-Kernel und automatisierten Durchlauf. Kein vollständiger plattformübergreifender Lockfile.
- `tools/check_notebook.py`: strukturelle Validierung und echter sauberer Kernel-Durchlauf; die letzte Notebook-Zelle überprüft die bekannten Versuchsergebnisse.

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
- Noch offen: persönliches aktuelles Notebook abgleichen, Anwendungsempfehlung gemeinsam begründen, Grenzen/Quellen final ausarbeiten sowie Dokumentation und Präsentation fertigstellen.

Die Inhalte wurden mit KI-Unterstützung schrittweise erarbeitet. Vor einer Abgabe müssen die Beteiligten die Schritte nachvollziehen, fachlich prüfen und gemäß den Kursregeln dokumentieren. Vorlesungsunterlagen, Kurszugänge, virtuelle Umgebungen und persönliche Notizen sind nicht Bestandteil dieses Repositories.
