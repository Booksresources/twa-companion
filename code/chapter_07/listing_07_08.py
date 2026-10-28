# Listing 7.8: Measuring how performance grows with training data
import numpy as np
from sklearn.model_selection import learning_curve

svm = Pipeline(
    [
        (
            "tfidf",
            TfidfVectorizer(stop_words="english", min_df=2, sublinear_tf=True),
        ),
        ("model", LinearSVC(class_weight="balanced")),
    ]
)
sizes, train_scores, val_scores = learning_curve(
    svm, train["text"], train["topic"], cv=cv, scoring="f1_macro",
    train_sizes=[0.02, 0.05, 0.1, 0.25, 0.5, 1.0], shuffle=True, random_state=42)

for n, tr, va in zip(sizes, train_scores.mean(1), val_scores.mean(1)):
    print(f"{n:5} training articles   train F1={tr:.3f}   validation F1={va:.3f}")
