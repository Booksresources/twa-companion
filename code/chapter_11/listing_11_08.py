# Listing 11.8: Evaluating recommendations with precision at k
import numpy as np

def precision_at_k(V, labels, k=5):
    """Share of each document's k nearest neighbours that share its topic."""
    S = cosine_similarity(V)
    np.fill_diagonal(S, -1)                       # exclude the document itself
    neighbours = np.argsort(-S, axis=1)[:, :k]
    labels = np.array(labels)
    return (labels[neighbours] == labels[:, None]).mean()

for name, V in [("TF-IDF", X), ("LSA, 100 dimensions", Z)]:
    print(f"{name:20} precision@5 = {precision_at_k(V, topics):.3f}")
