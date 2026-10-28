# Listing 5.9: Evaluating four count-based representations
import re
import numpy as np
from nltk.corpus import reuters
from gensim.models import Word2Vec
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold

TOPICS = ["earn", "acq", "crude", "trade", "money-fx", "interest"]
ids = [f for f in reuters.fileids() if f.startswith("training")
       and len(reuters.categories(f)) == 1 and reuters.categories(f)[0] in TOPICS]
texts = [re.sub(r"&lt;|<[^>]+>", " ", reuters.raw(f)) for f in ids]
labels = [reuters.categories(f)[0] for f in ids]
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
clf = lambda: LogisticRegression(max_iter=2000, C=10)

candidates = {
    "Counts": make_pipeline(
        CountVectorizer(stop_words="english", min_df=2), clf()
    ),
    "TF-IDF": make_pipeline(
        TfidfVectorizer(stop_words="english", min_df=2, sublinear_tf=True), clf()
    ),
    "TF-IDF + bigrams": make_pipeline(
        TfidfVectorizer(
            stop_words="english", min_df=2, sublinear_tf=True, ngram_range=(1, 2)
        ),
        clf(),
    ),
    "LSA (100 dimensions)": make_pipeline(
        TfidfVectorizer(stop_words="english", min_df=2, sublinear_tf=True),
        TruncatedSVD(100, random_state=42),
        clf(),
    ),
}
results = {}
for name, pipe in candidates.items():
    results[name] = cross_val_score(
        pipe, texts, labels, cv=cv, scoring="f1_macro"
    ).mean()
