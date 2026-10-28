# Listing 11.6: A simple TF-IDF search engine
def search(query, top=3):
    q = tfidf.transform([query])
    scores = cosine_similarity(q, X).ravel()
    for i in scores.argsort()[::-1][:top]:
        first_line = texts[i].strip().split("\n")[0][:60]
        print(f"{scores[i]:.3f}  [{topics[i]}]  {first_line}")

search("tanker attacked in the gulf")
print()
search("central bank intervenes to support currency")
