from sklearn.metrics import roc_auc_score, average_precision_score

zusammenfassung = []

for name, labels, modell_scores in [
    ("A – bisherige Verteilung", y_true, scores),
    ("A – seltene positive Fälle", y_selten, scores_selten),
    ("B – bisherige Verteilung", y_true, scores_b),
    ("B – seltene positive Fälle", y_selten, scores_b_selten)
]:
    # Kontinuierliche Scores verwenden, nicht 0/1-Vorhersagen!
    roc_auc = roc_auc_score(labels, modell_scores)
    ap = average_precision_score(labels, modell_scores, pos_label=1)
    zusammenfassung.append((name, roc_auc, ap))

    print(f"\n{name}")
    print(f"ROC-AUC: {roc_auc:.4f}")
    print(f"Average Precision (AP): {ap:.4f}")
