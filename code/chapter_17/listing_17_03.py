# Listing 17.3: Words that rose most after February 2025
import numpy as np
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from collections import Counter

def words(texts):
    return Counter(
        w
        for t in texts
        for w in re.findall(r"[a-záéíóúãõç]+", t.lower())
        if len(w) > 2 and w not in ENGLISH_STOP_WORDS
    )

before, after = words(reviews.loc[reviews.period == "before", "text"]), words(
    reviews.loc[reviews.period == "after", "text"]
)
vocab = sorted(w for w in set(before) | set(after) if before[w] + after[w] >= 30)
nb, na = sum(before.values()), sum(after.values())
lo = {
    w: np.log((after[w] + 0.5) / (na - after[w] + 0.5))
    - np.log((before[w] + 0.5) / (nb - before[w] + 0.5))
    for w in vocab
}
print("Rising after February 2025:", sorted(lo, key=lo.get, reverse=True)[:8])
