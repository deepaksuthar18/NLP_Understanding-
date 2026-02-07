"""
Zipf's Law Demonstration using NLTK

This script analyzes word frequency distribution in a small corpus
and verifies Zipf's Law using a log-log plot.
"""

import matplotlib.pyplot as plt
import nltk
from nltk.probability import FreqDist

# -----------------------------
# Step 1: Define the corpus
# -----------------------------
corpus = [
    "Natural Language Processing with NLTK",
    "Natural Language gets developed over the time",
    "Language Processing is very important",
    "Natural Language Processing is an important scientific field",
    "Natural Language Analysis",
    "Natural Language Processing",
    "Natural Language Understanding",
    "Natural Language Understanding"
]

# -----------------------------
# Step 2: Download tokenizer
# -----------------------------
nltk.download("punkt")

# -----------------------------
# Step 3: Tokenize the corpus
# -----------------------------
flat_corpus = []

for sentence in corpus:
    tokens = nltk.word_tokenize(sentence)
    flat_corpus.extend(tokens)

print("Tokenized Corpus:")
print(flat_corpus)

# -----------------------------
# Step 4: Compute frequency distribution
# -----------------------------
frequency_distribution = FreqDist(flat_corpus)

# Sort words by decreasing frequency (Zipf requirement)
sorted_words = [
    word for word, frequency in frequency_distribution.most_common()
]

# -----------------------------
# Step 5: Assign ranks and frequencies
# -----------------------------
ranks = list(range(1, len(sorted_words) + 1))
frequencies = [
    frequency_distribution[word] for word in sorted_words
]

# -----------------------------
# Step 6: Display frequency table
# -----------------------------
print("\nWord Frequency Table:")
print("{:<16s}{:<12s}{:<6s}".format("Word", "Frequency", "Rank"))
print("-" * 36)

for rank, word in enumerate(sorted_words, start=1):
    print(
        "{:<16s}{:<12d}{:<6d}".format(
            word,
            frequency_distribution[word],
            rank
        )
    )

# -----------------------------
# Step 7: Plot Zipf’s Law
# -----------------------------
plt.figure(figsize=(8, 6))
plt.loglog(ranks, frequencies, marker=".")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Zipf's Law Verification")
plt.grid(True)
plt.show()
