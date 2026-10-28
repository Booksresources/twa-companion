# Listing 6.4: Distinctive words in two corpora by log-odds ratio
import numpy as np

def counts_for(category):
    words = [w.lower() for w in brown.words(categories=category) if w.isalpha()]
    return Counter(w for w in words if w not in stop)

a, b = counts_for("news"), counts_for("romance")
vocab = sorted(w for w in set(a) | set(b) if a[w] + b[w] >= 20)
na, nb = sum(a.values()), sum(b.values())

def log_odds(w, k=0.5):                 # k: smoothing for rare words
    pa = (a[w] + k) / (na + k * len(vocab))
    pb = (b[w] + k) / (nb + k * len(vocab))
    return np.log(pa / (1 - pa)) - np.log(pb / (1 - pb))

scores = pd.Series({w: log_odds(w) for w in vocab}).sort_values()
print("Romance:", list(scores.index[:8]))
print("News:   ", list(scores.index[-8:][::-1]))
