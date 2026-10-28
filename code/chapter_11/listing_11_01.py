# Listing 11.1: Comparing three similarity measures
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

texts = ["the train to the airport was delayed",
         "the airport train was delayed again and again and again",
         "our flight was cancelled at the airport",
         "the recipe needs two eggs and flour"]

def jaccard(a, b):
    a, b = set(a.split()), set(b.split())
    return len(a & b) / len(a | b)

X = TfidfVectorizer().fit_transform(texts)
cos = cosine_similarity(X)
print("Cosine similarity to text 0:   ", cos[0].round(2))
print(
    "Jaccard similarity to text 0:  ",
    np.round([jaccard(texts[0], t) for t in texts], 2),
)
counts = TfidfVectorizer(use_idf=False, norm=None).fit_transform(texts)
print("Euclidean distance (counts):   ", euclidean_distances(counts)[0].round(2))
