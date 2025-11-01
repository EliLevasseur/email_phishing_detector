# predict_email.py
import sys
from rule_based_detector import detect_phishing, normalize

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 predict_email.py \"<email text>\"")
        sys.exit(1)
    text = " ".join(sys.argv[1:])
    label = detect_phishing(text)
    print(label)

if __name__ == "__main__":
    main()
