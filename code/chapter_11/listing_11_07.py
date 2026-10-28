# Listing 11.7: Finding the most related articles
def related(i, V, k=3):
    sims = cosine_similarity(V[i:i + 1], V).ravel()
    sims[i] = -1
    headline = lambda j: texts[j].strip().split("\n")[0][:55]
    print(f"[{topics[i]}] {headline(i)}")
    for j in sims.argsort()[::-1][:k]:
        print(f"   {sims[j]:.2f} [{topics[j]}] {headline(j)}")

related(topics.index("coffee"), Z)
