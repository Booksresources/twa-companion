# Listing 10.2: Counting entities in a news collection
import re
from collections import Counter
from nltk.corpus import reuters

ids = reuters.fileids("crude")[:300]
texts = [re.sub(r"&lt;|<[^>]+>", " ", reuters.raw(f)) for f in ids]

counts = {"ORG": Counter(), "GPE": Counter(), "PERSON": Counter()}
for doc in nlp.pipe(texts, batch_size=50, disable=["lemmatizer"]):
    for ent in doc.ents:
        if ent.label_ in counts:
            counts[ent.label_][ent.text.strip()] += 1

for label, c in counts.items():
    print(label, c.most_common(6))
