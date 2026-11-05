import matplotlib.pyplot as plt

# Spalten aus der vorherigen Ergebnisliste entnehmen
fpr_werte = [zeile[1] for zeile in ergebnisse]
recall_werte = [zeile[2] for zeile in ergebnisse]
precision_werte = [zeile[3] for zeile in ergebnisse]

fig, achsen = plt.subplots(1, 2, figsize=(11, 4))

# ROC: ergänzter Startpunkt ohne positive Vorhersagen
achsen[0].plot([0] + fpr_werte, [0] + recall_werte, marker="o")
achsen[0].set_title("ROC-Kurve")
achsen[0].set_xlabel("False Positive Rate")
achsen[0].set_ylabel("Recall / True Positive Rate")

# PR: Messpunkte ohne Verbindungslinien, mit Schwellenbeschriftung
achsen[1].scatter(recall_werte, precision_werte)
for schwelle, fpr, recall, precision in ergebnisse:
    achsen[1].annotate(
        f"{schwelle:.2f}", (recall, precision),
        xytext=(7, 5), textcoords="offset points", fontsize=9
    )
achsen[1].set_title("PR-Messpunkte – Zahl = Schwelle")
achsen[1].set_xlabel("Recall")
achsen[1].set_ylabel("Precision")

for achse in achsen:
    achse.set_xlim(-0.03, 1.12)
    achse.set_ylim(-0.03, 1.12)
    achse.grid(alpha=0.3)

plt.tight_layout()
plt.show()
