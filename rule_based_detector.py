# rule_based_detector.py
import pandas as pd
import re
from collections import Counter
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- Config: update keywords if you want ----------
PHRASE_KEYWORDS = [
    "verify your identity",
    "update your billing",
    "click the link",
    "reset your password",
    "unusual sign in attempt",
    "confirm your account",
]

PHISHING_KEYWORDS = [
    "account", "update", "click", "verify", "information",
    "password", "immediately", "suspend", "confirm", "urgent",
    "billing", "login", "signin", "verify", "security", "reset"
]

# helper: normalize text
def normalize(text):
    if pd.isna(text):
        return ""
    s = str(text).lower()
    s = re.sub(r'[^a-z0-9 ]+', ' ', s)
    return s

def detect_phishing(text):
    s = normalize(text)
    # exact phrase hits first
    for phrase in PHRASE_KEYWORDS:
        if phrase in s:
            return "phishing"

    # rule: if ANY keyword present -> phishing
    for kw in PHISHING_KEYWORDS:
        if f" {kw} " in f" {s} " or s.startswith(kw + " ") or s.endswith(" " + kw) or (" " + kw + " ") in (" " + s + " "):
            return "phishing"
    return "legit"

def main():
    # Load dataset
    df = pd.read_csv("emails.csv")
    assert {"text", "label"} <= set(df.columns), "emails.csv must contain 'text' and 'label' columns"
    df['label'] = df['label'].astype(str).str.strip().str.lower()

    # Predict
    df['prediction'] = df['text'].apply(detect_phishing)

    # Save predictions for inspection
    df.to_csv("rule_based_results.csv", index=False)

    # Metrics
    y_true = df['label']
    y_pred = df['prediction']
    acc = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred, labels=["phishing", "legit"])
    report = classification_report(y_true, y_pred, digits=4)

    print(f"Accuracy: {acc:.4f}")
    print("Confusion matrix (rows=true, cols=pred):\n", cm)
    print("\nClassification report:\n", report)

    # Plot confusion matrix
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["phishing","legit"],
                yticklabels=["phishing","legit"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix — Rule-based Detector")
    plt.tight_layout()
    plt.savefig("confusion_matrix_rule_based.png", dpi=150)
    print("Saved confusion matrix -> confusion_matrix_rule_based.png")

    # ---------- Inspect false positives / negatives ----------
df_results = pd.read_csv("rule_based_results.csv")

false_neg = df_results[(df_results['label'] == 'phishing') & (df_results['prediction'] == 'legit')]
false_pos = df_results[(df_results['label'] == 'legit') & (df_results['prediction'] == 'phishing')]

print("\n--- False Negatives (missed phishing) ---")
print(false_neg['text'].head(5).to_list())

print("\n--- False Positives (flagged legit as phishing) ---")
print(false_pos['text'].head(5).to_list())


if __name__ == "__main__":
    main()
