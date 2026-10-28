# Listing 11.5: Finding near-duplicate articles with shingles
from collections import defaultdict

def shingles(text, k=5):
    words = re.findall(r"\w+", text.lower())
    return {" ".join(words[i:i + k]) for i in range(len(words) - k + 1)}

sets = [shingles(t) for t in texts]
index = defaultdict(set)                  # shingle -> documents containing it
for i, s in enumerate(sets):
    for sh in s:
        index[sh].add(i)

pairs = set()
for i, s in enumerate(sets):
    candidates = {j for sh in s for j in index[sh] if j > i}
    for j in candidates:
        sim = len(s & sets[j]) / len(s | sets[j])
        if sim >= 0.8:
            pairs.add((i, j, round(sim, 2)))
print(len(pairs), "near-duplicate pairs (Jaccard >= 0.8)")
for i, j, sim in sorted(pairs, key=lambda p: -p[2])[:3]:
    print(sim, ids[i], ids[j])
