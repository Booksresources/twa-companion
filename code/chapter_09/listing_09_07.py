# Listing 9.7: Measuring topic stability across random seeds
import numpy as np
from scipy.optimize import linear_sum_assignment

def top_words(model, n=10):
    return [set(terms[w.argsort()[-n:]]) for w in model.components_]

def match_topics(ref, other):
    sim = np.array([[len(a & b) / len(a | b) for b in other] for a in ref])
    rows, cols = linear_sum_assignment(-sim)          # best one-to-one matching
    return sim[rows, cols]

reference = top_words(lda)                           # the model from Listing 9.1
stability = []
for seed in [1, 2, 3]:
    m = LatentDirichletAllocation(n_components=12, learning_method="online",
                                  random_state=seed, max_iter=10).fit(X)
    stability.append(match_topics(reference, top_words(m)))
stability = np.array(stability).mean(axis=0)

for k in np.argsort(stability)[::-1]:
    print(f"{labels[k]:26} mean Jaccard {stability[k]:.2f}")
