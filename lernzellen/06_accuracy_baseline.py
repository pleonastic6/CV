# Absichtliche Nullmodell-Baseline: immer "kein Objekt" melden.
# Das ist nicht unser bisheriger Klassifikator.
baseline_pred = [0] * len(y_selten)

baseline_accuracy = sum(
    w == p for w, p in zip(y_selten, baseline_pred)
) / len(y_selten)

baseline_recall = sum(
    w == 1 and p == 1 for w, p in zip(y_selten, baseline_pred)
) / sum(y_selten)

print(f"Immer-negativ-Baseline – Accuracy: {baseline_accuracy:.1%}")
print(f"Immer-negativ-Baseline – Recall: {baseline_recall:.1%}")
