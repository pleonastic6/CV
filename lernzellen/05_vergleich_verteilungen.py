import matplotlib.pyplot as plt

# Bisherige Berechnung als wiederverwendbare Funktion
# Voraussetzung: Beide Klassen kommen in labels vor.
def kurvenpunkte(labels, modell_scores):
    punkte = []
    for schwelle in sorted(set(modell_scores), reverse=True):
        vorhersagen = [int(s >= schwelle) for s in modell_scores]
        tp = sum(w == 1 and p == 1 for w, p in zip(labels, vorhersagen))
        fp = sum(w == 0 and p == 1 for w, p in zip(labels, vorhersagen))
        fn = sum(w == 1 and p == 0 for w, p in zip(labels, vorhersagen))
        tn = sum(w == 0 and p == 0 for w, p in zip(labels, vorhersagen))
        punkte.append((schwelle, fp / (fp + tn),
                       tp / (tp + fn), tp / (tp + fp)))
    return punkte

punkte_bisher = kurvenpunkte(y_true, scores)
punkte_selten = kurvenpunkte(y_selten, scores_selten)

fig, achsen = plt.subplots(1, 2, figsize=(11, 4))

for punkte, name, stil, marker in [
    (punkte_bisher, "Bisherige Verteilung", "-", "o"),
    (punkte_selten, "Seltene positive Fälle", "--", "x")
]:
    fpr_werte = [zeile[1] for zeile in punkte]
    recall_werte = [zeile[2] for zeile in punkte]
    precision_werte = [zeile[3] for zeile in punkte]

    achsen[0].plot([0] + fpr_werte, [0] + recall_werte,
                   linestyle=stil, marker=marker, label=name)
    achsen[1].scatter(recall_werte, precision_werte,
                      marker=marker, label=name)

achsen[0].set(title="ROC – Vergleich der Verteilungen",
              xlabel="False Positive Rate", ylabel="Recall")
achsen[1].set(title="PR-Messpunkte – Vergleich der Verteilungen",
              xlabel="Recall", ylabel="Precision")

for achse in achsen:
    achse.set_xlim(-0.03, 1.05)
    achse.set_ylim(-0.03, 1.05)
    achse.grid(alpha=0.3)
    achse.legend()

plt.tight_layout()
plt.show()
