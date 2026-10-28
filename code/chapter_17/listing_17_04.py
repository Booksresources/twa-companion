# Listing 17.4: Classifying an incoming news stream
import re
import pandas as pd
from nltk.corpus import reuters
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

TOPICS = ["crude", "grain", "trade", "money-fx", "ship", "coffee", "sugar",
          "gold"]
single = [f for f in reuters.fileids() if len(reuters.categories(f)) == 1
          and reuters.categories(f)[0] in TOPICS]
train = [f for f in single if f.startswith("training")]
# the "incoming" articles
stream = [f for f in reuters.fileids() if f.startswith("test")]

clf = Pipeline(
    [
        (
            "tfidf",
            TfidfVectorizer(stop_words="english", min_df=2, sublinear_tf=True),
        ),
        ("svm", LinearSVC(class_weight="balanced")),
    ]
)
clf.fit(
    [reuters.raw(f) for f in train], [reuters.categories(f)[0] for f in train]
)

# Classify every incoming article and keep confident predictions only
scores = clf.decision_function([reuters.raw(f) for f in stream])
news = pd.DataFrame({"id": stream, "topic": clf.classes_[scores.argmax(1)],
                     "margin": scores.max(1)})
news = news[news["margin"] > 0].copy()
print(
    len(stream), "incoming articles;", len(news), "assigned to a monitored topic"
)
