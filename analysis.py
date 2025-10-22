import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
import re

# Load the dataset
df = pd.read_csv('emails.csv')

# Tokenization function
def tokenize(text):
    # convert to lowercase and remove punctuation
    text = re.sub(r'[\W_]+', ' ', text.lower())
    return text.split()

stopwords = set(['the', 'to', 'a', 'and', 'in', 'for', 'on', 'with', 'of', 'is', 
                 'your', 'you', 'here', 'it', 'we', 'are', 'has', 'have', 
                 'this', 'my', 'i', 'be', 'at', 'me', 'from', 'our'])

# Compute word frequencies by label
word_freqs = {'phishing': Counter(), 'legit': Counter()}

for label in ['phishing', 'legit']:
    tokens = [token for text in df[df['label'] == label]['text'] 
              for token in tokenize(text)]
    filtered = [w for w in tokens if len(w) > 2 and w not in stopwords]
    word_freqs[label] = Counter(filtered)
phishing_top = word_freqs['phishing'].most_common(10)
legit_top = word_freqs['legit'].most_common(10)

print("Top phishing words:", phishing_top)
print("Top legit words:", legit_top)

# Create a DataFrame for plotting
phishing_df = pd.DataFrame(phishing_top, columns=['Word', 'Frequency'])

# Plot the top phishing words
plt.figure(figsize=(8, 6))
plt.bar(phishing_df['Word'], phishing_df['Frequency'])
plt.title('Top Phishing Words')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_phishing_words.png')  # saves the image in your project folder
plt.show()
