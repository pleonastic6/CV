import matplotlib.pyplot as plt

# Bisherige Scores bleiben Modell A.
# Modell B: bewusst konstruierte zweite Scorequelle, kein Training.
# Die Positionen gehören weiterhin zu denselben Bildern in y_true.
scores_b = [0.90, 0.65, 0.85, 0.55, 0.30, 0.20, 0.60, 0.10]

# Genau dieselbe Wiederholungsregel und Reihenfolge wie bei Modell A
scores_b_selten = []
for wahr, score in zip(y_true, scores_b):
    anzahl = 20 if wahr == 0 else 1
    scores_b_selten.extend([score] * anzahl)

fig, achsen = plt.subplots(1, 2, figsize=(11, 4))

for name, modell_scores, marker in [
    ("Modell A", scores_selten, "o"),
    ("Modell B", scores_b_selten, "x")
]:
    punkte_modell = kurvenpunkte(y_selten, modell_scores)
    fpr_werte = [zeile[1] for zeile in punkte_modell]
    recall_werte = [zeile[2] for zeile in punkte_modell]
    precision_werte = [zeile[3] for zeile in punkte_modell]

    achsen[0].plot(
        [0] + fpr_werte, [0] + recall_werte,
        marker=marker, label=name
    )
    achsen[1].scatter(
        recall_werte, precision_werte,
        marker=marker, label=name
    )

achsen[0].set(title="ROC – Modellvergleich, seltene positive Fälle",
              xlabel="False Positive Rate", ylabel="Recall")
achsen[1].set(title="PR-Messpunkte – dieselben Fälle",
              xlabel="Recall", ylabel="Precision")

for achse in achsen:
    achse.set_xlim(-0.03, 1.05)
    achse.set_ylim(-0.03, 1.05)
    achse.grid(alpha=0.3)
    achse.legend()

plt.tight_layout()
plt.show()
