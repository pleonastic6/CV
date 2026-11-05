import matplotlib.pyplot as plt

fig, achse = plt.subplots(figsize=(7, 4.5))
for schwelle, fpr, recall, precision in ergebnisse:
    achse.scatter(recall, precision, color="tab:blue", s=45)
    achse.annotate(
        f"{schwelle:.2f}", (recall, precision),
        xytext=(7, 5), textcoords="offset points", fontsize=9
    )

achse.set_title("PR-Messpunkte – Beschriftung: Entscheidungsschwelle")
achse.set_xlabel("Recall")
achse.set_ylabel("Precision")
achse.set_xlim(0, 1.12)
achse.set_ylim(0, 1.12)
achse.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
achse.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
achse.grid(alpha=0.3)
fig.tight_layout()
plt.show()
