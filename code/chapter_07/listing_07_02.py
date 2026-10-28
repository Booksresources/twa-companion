# Listing 7.2: A TF-IDF and logistic regression pipeline
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

clf = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", min_df=2, sublinear_tf=True)),
    ("model", LogisticRegression(max_iter=1000)),
])
clf.fit(train["text"], train["topic"])
pred = clf.predict(test["text"])
print(classification_report(test["topic"], pred, digits=3))
