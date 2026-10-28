# Listing 5.10: Adding averaged Word2Vec vectors and comparing
# Averaged Word2Vec vectors trained on the same articles
tokens = [re.findall(r"[a-z]+", t.lower()) for t in texts]
w2v = Word2Vec(
    tokens,
    vector_size=100,
    window=5,
    min_count=3,
    sg=1,
    epochs=10,
    workers=1,
    seed=42,
)
X_avg = np.array(
    [
        np.mean(
            [w2v.wv[w] for w in toks if w in w2v.wv] or [np.zeros(100)], axis=0
        )
        for toks in tokens
    ]
)
results["Averaged Word2Vec"] = cross_val_score(
    clf(), X_avg, labels, cv=cv, scoring="f1_macro"
).mean()

for name, score in sorted(results.items(), key=lambda kv: -kv[1]):
    print(f"{name:22} macro-F1 = {score:.3f}")
