# Listing 7.4: Comparing classifiers with stratified cross-validation
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.naive_bayes import ComplementNB
from sklearn.svm import LinearSVC

models = {"Complement Naive Bayes": ComplementNB(),
          "Logistic regression": LogisticRegression(max_iter=1000),
          "Linear SVM": LinearSVC()}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for name, model in models.items():
    pipe = Pipeline([("tfidf", TfidfVectorizer(stop_words="english", min_df=2,
                                               sublinear_tf=True)),
                     ("model", model)])
    scores = cross_val_score(pipe, train["text"], train["topic"],
                             cv=cv, scoring="f1_macro")
    print(f"{name:24} macro-F1 = {scores.mean():.3f} ± {scores.std():.3f}")
