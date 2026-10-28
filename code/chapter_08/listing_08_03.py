# Listing 8.3: Words and phrases most associated with each class
clf.fit(docs, labels)
terms = clf.named_steps["tfidf"].get_feature_names_out()
# positive weights favor 'pos'
weights = clf.named_steps["model"].coef_[0]
order = np.argsort(weights)
print("Negative:", ", ".join(terms[order[:10]]))
print("Positive:", ", ".join(terms[order[-10:][::-1]]))
