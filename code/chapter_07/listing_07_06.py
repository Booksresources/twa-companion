# Listing 7.6: Tuning the pipeline with grid search
from sklearn.model_selection import GridSearchCV

pipe = Pipeline(
    [
        ("tfidf", TfidfVectorizer(stop_words="english", sublinear_tf=True)),
        ("model", LinearSVC(class_weight="balanced", max_iter=5000)),
    ]
)
grid = {"tfidf__ngram_range": [(1, 1), (1, 2)],
        "tfidf__min_df": [1, 3],
        "model__C": [0.1, 1.0, 10.0]}
search = GridSearchCV(pipe, grid, cv=cv, scoring="f1_macro", n_jobs=-1)
search.fit(train["text"], train["topic"])

print("Best settings:", search.best_params_)
print(f"Cross-validated macro-F1: {search.best_score_:.3f}")
test_f1 = f1_score(test["topic"], search.predict(test["text"]), average="macro")
print(f"Test macro-F1: {test_f1:.3f}")
