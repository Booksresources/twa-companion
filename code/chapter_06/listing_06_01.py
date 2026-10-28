# Listing 6.1: Corpus size and the most frequent content words
import nltk
import pandas as pd
from collections import Counter
from nltk.corpus import brown, stopwords

nltk.download(["brown", "stopwords"], quiet=True)
stop = set(stopwords.words("english"))

tokens = [w.lower() for w in brown.words(categories="news") if w.isalpha()]
content = [w for w in tokens if w not in stop]

print(f"{len(tokens):,} tokens, {len(set(tokens)):,} distinct words")
freq = Counter(content)
print(pd.Series(dict(freq.most_common(10))).to_string())
