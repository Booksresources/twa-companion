# Listing 5.7: Document vectors by averaging word embeddings
import numpy as np

def doc_vector(text, wv):
    words = [w for w in text.lower().split() if w in wv]
    if not words:
        return np.zeros(wv.vector_size)
    return np.mean([wv[w] for w in words], axis=0)

def cosine(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

query = doc_vector("the mayor spoke to the city council", model.wv)
for text in ["officials of the town government met",
             "the river flooded the farms",
             "she painted the kitchen yellow"]:
    print(f"{cosine(query, doc_vector(text, model.wv)):.2f}  {text}")
