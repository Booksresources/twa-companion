# Listing 4.11: Testing preprocessing steps one at a time
import re
from nltk.corpus import reuters
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score, StratifiedKFold

TOPICS = ["earn", "acq", "crude", "trade", "money-fx", "interest"]
ids = [f for f in reuters.fileids() if f.startswith("training")
       and len(reuters.categories(f)) == 1 and reuters.categories(f)[0] in TOPICS]
texts = [reuters.raw(f) for f in ids]
labels = [reuters.categories(f)[0] for f in ids]
stem = PorterStemmer().stem

def analyzer(lower=False, stop=False, stemming=False, clean=False):
    def run(text):
        if clean:
            # ticker markup, numbers
            text = re.sub(r"&lt;[^>]*>|\d+([.,]\d+)?", " ", text)
        tokens = re.findall(r"\w+", text.lower() if lower else text)
        if stop:
            tokens = [t for t in tokens if t.lower() not in ENGLISH_STOP_WORDS]
        if stemming:
            tokens = [stem(t) for t in tokens]
        return tokens
    return run

configs = {
    "Tokens only": {},
    "+ lowercase": dict(lower=True),
    "+ stop words removed": dict(lower=True, stop=True),
    "+ stemming": dict(lower=True, stop=True, stemming=True),
    "+ markup and numbers removed": dict(
        lower=True, stop=True, stemming=True, clean=True
    ),
}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for name, opts in configs.items():
    vec = TfidfVectorizer(analyzer=analyzer(**opts), sublinear_tf=True, min_df=2)
    vocab = len(vec.fit(texts).vocabulary_)
    f1 = cross_val_score(make_pipeline(vec, LinearSVC(class_weight="balanced")),
                         texts, labels, cv=cv, scoring="f1_macro").mean()
    print(f"{name:30} vocabulary={vocab:6,}   macro-F1={f1:.3f}")
