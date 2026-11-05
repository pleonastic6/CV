# Kontrollversuch: Negative Fälle samt Score jeweils 20-mal gewichten.
# Das sind Wiederholungen, keine neuen unabhängigen Testbilder.
y_selten = []
scores_selten = []

for wahr, score in zip(y_true, scores):
    anzahl = 20 if wahr == 0 else 1
    y_selten.extend([wahr] * anzahl)
    scores_selten.extend([score] * anzahl)

# Feste Schwelle, unabhängig vom letzten Schleifendurchlauf im Notebook
vergleichsschwelle = 0.5

for name, labels, modell_scores in [
    ("Bisherige Verteilung", y_true, scores),
    ("Seltene positive Fälle", y_selten, scores_selten)
]:
    vorhersagen = [int(s >= vergleichsschwelle) for s in modell_scores]
    tp = sum(w == 1 and p == 1 for w, p in zip(labels, vorhersagen))
    fp = sum(w == 0 and p == 1 for w, p in zip(labels, vorhersagen))
    fn = sum(w == 1 and p == 0 for w, p in zip(labels, vorhersagen))
    tn = sum(w == 0 and p == 0 for w, p in zip(labels, vorhersagen))

    print(f"\n{name} – Schwelle {vergleichsschwelle}")
    print(f"Positive Fälle: {sum(labels)} von {len(labels)}")
    print(f"TP={tp}, FP={fp}, FN={fn}, TN={tn}")
    print(f"Precision: {tp / (tp + fp):.1%}")
    print(f"Recall: {tp / (tp + fn):.1%}")
    print(f"False Positive Rate: {fp / (fp + tn):.1%}")
