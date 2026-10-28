# Listing 15.2: Context changes the representation of a word
# Word2Vec vectors from Listing 5.6
wv = model.wv
cos = lambda a, b: float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

def contextual(sentence, word, scale=4.0):
    tokens = [t for t in sentence.split() if t in wv]
    X = np.array([wv[t] for t in tokens])
    X = X / np.linalg.norm(X, axis=1, keepdims=True)
    # self-attention with Q = K = V = X
    out, w = attention(X * scale, X * scale, X)
    i = tokens.index(word)
    return out[i], {t: round(float(v), 2) for t, v in zip(tokens, w[i])}

print(
    f"static 'bank':      water {cos(wv['bank'], wv['water']):.2f}   money "
    f"{cos(wv['bank'], wv['money']):.2f}"
)
for s in [
    "we walked along the bank of the river",
    "the bank raised interest rates",
]:
    vec, weights = contextual(s, "bank")
    print(
        f"in context:         water {cos(vec, wv['water']):.2f}   money "
        f"{cos(vec, wv['money']):.2f}   | {s}"
    )
    print("   attention from 'bank':", weights)
