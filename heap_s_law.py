# -*- coding: utf-8 -*-
"""
Heap's Law Demonstration in NLP

This script demonstrates how vocabulary size grows
as the number of tokens increases in a corpus.
"""

import matplotlib.pyplot as plt
import nltk

# --------------------------------------------------
# Download required tokenizer resource
# --------------------------------------------------
nltk.download("punkt")
nltk.download("punkt_tab")

# --------------------------------------------------
# Corpus Definition
# --------------------------------------------------
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

# --------------------------------------------------
# Tokenization
# Flatten the corpus into a list of words
# --------------------------------------------------
flat_corpus = []

for sentence in corpus:
    tokens = nltk.word_tokenize(sentence)
    flat_corpus.extend(tokens)

print("Tokenized Corpus:")
print(flat_corpus)

# --------------------------------------------------
# Heap’s Law Computation
# --------------------------------------------------
vocabulary_sizes = []
document_lengths = []

unique_words = set()

for index, word in enumerate(flat_corpus, start=1):
    unique_words.add(word)  # Add word to vocabulary
    vocabulary_sizes.append(len(unique_words))  # Vocabulary size
    document_lengths.append(index)  # Token count

# --------------------------------------------------
# Visualization of Heap's Law
# --------------------------------------------------
plt.figure(figsize=(8, 6))
plt.plot(document_lengths, vocabulary_sizes, marker='.')

plt.xlabel("Document Length (Number of Tokens)")
plt.ylabel("Vocabulary Size (Unique Words)")
plt.title("Heap's Law: Vocabulary Growth Curve")

plt.grid(True)
plt.show()
