# Listing 16.8: Comparing chunk sizes for retrieval
import numpy as np
from nltk.corpus import reuters
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

articles = {}
for fid in reuters.fileids("crude"):
    lines = reuters.raw(fid).strip().split("\n")
    body = sent_tokenize(" ".join(" ".join(lines[1:]).split()))
    if len(body) >= 4:
        # (headline, body sentences)
        articles[fid] = (lines[0].strip(), body)

def recall_at_k(chunk_size, k=3):
    passages = [
        (fid, " ".join(s[i : i + chunk_size]))
        for fid, (_, s) in articles.items()
        for i in range(0, len(s), chunk_size)
    ]
    vec = TfidfVectorizer(stop_words="english", sublinear_tf=True).fit(
        [p for _, p in passages]
    )
    P = vec.transform([p for _, p in passages])
    owners = np.array([fid for fid, _ in passages])
    hits = []
    # each headline is a question
    for fid, (headline, _) in articles.items():
        sims = cosine_similarity(vec.transform([headline]), P).ravel()
        hits.append(fid in owners[sims.argsort()[::-1][:k]])
    words = np.mean([len(p.split()) for _, p in passages])
    return np.mean(hits), len(passages), words

for size in [1, 3, 6, 1000]:
    r, n, w = recall_at_k(size)
    label = "whole article" if size == 1000 else f"{size} sentence(s)"
    print(
        f"{label:15} {n:5} passages  {w:6.0f} words each   recall@3 = {r:.2f}   "
        f"~{3 * w:,.0f} words in prompt"
    )
