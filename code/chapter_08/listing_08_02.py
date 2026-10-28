# Listing 8.2: Lexicon versus supervised classifier on film reviews
import numpy as np
from nltk.corpus import movie_reviews
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold

docs = [movie_reviews.raw(f) for f in movie_reviews.fileids()]
# 'pos'/'neg'
labels = [movie_reviews.categories(f)[0] for f in movie_reviews.fileids()]

# Lexicon baseline: positive if VADER's compound score is above zero
vader_pred = [
    "pos" if sia.polarity_scores(d)["compound"] > 0 else "neg" for d in docs
]
print(
    "VADER accuracy:               "
    f"{np.mean(np.array(vader_pred) == np.array(labels)):.3f}"
)

clf = Pipeline(
    [
        (
            "tfidf",
            TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True),
        ),
        ("model", LogisticRegression(C=10, max_iter=2000)),
    ]
)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(clf, docs, labels, cv=cv, scoring="accuracy")
print(f"TF-IDF + logistic regression: {scores.mean():.3f} ± {scores.std():.3f}")
