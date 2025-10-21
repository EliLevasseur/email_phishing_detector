# main.py — Day 2: load & sanity-check the dataset
import pandas as pd
from pathlib import Path

csv_path = Path("emails.csv")
if not csv_path.exists():
	raise FileNotFoundError("emails.csv not found in the project folder.")

df = pd.read_csv(csv_path)

# Basic checks
print(f"Rows: {len(df)}")
print("Columns:", list(df.columns))

# Ensure required columns exist
required = {"text", "label"}
missing = required - set(df.columns)
if missing:
	raise ValueError(f"Missing required columns: {missing}")

# Drop obvious bad rows
df = df.dropna(subset=["text", "label"])
df["label"] = df["label"].str.strip().str.lower()

# Show class balance
print("\nClass counts:")
print(df["label"].value_counts())

# Show a couple examples from each class
pd.set_option('display.max_colwidth', 100)

print("\nSample phishing:")
print(df[df["label"] == "phishing"]["text"].head(2))
print("\nSample legit:")
print(df[df["label"] == "legit"]["text"].head(2).to_string(index=False))

# Add quick text length stats
df["char_len"] = df["text"].astype(str).str.len()
df['word_length'] = df["text"].astype(str).str.split().str.len()

print("\nLength stats (characters):")
print(df.groupby("char_len")['word_length'].describe().round(1).head(2))

print("\nLength stats (words):")
print(df.groupby("char_len")["word_length"].describe().round(1).head(2))



