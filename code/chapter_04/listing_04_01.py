# Listing 4.1: Whitespace splitting versus NLTK tokenizers
from nltk.tokenize import sent_tokenize, word_tokenize

text = ("Dr. Okafor's team didn't expect 3,500 replies. "
        "The survey closed on 12.05.2025 - results are online!")

print(text.split()[:6])
print(sent_tokenize(text))
print(word_tokenize(text)[:12])
