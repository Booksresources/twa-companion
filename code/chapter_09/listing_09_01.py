# Listing 9.1: Fitting an LDA topic model with scikit-learn
import re
from nltk.corpus import reuters
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

docs = [re.sub(r"&lt;|<[^>]+>", " ", reuters.raw(f)) for f in reuters.fileids()]
print(len(docs), "articles")

vectorizer = CountVectorizer(stop_words="english", min_df=10, max_df=0.5,
                             token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z]{2,}\b")
X = vectorizer.fit_transform(docs)
terms = vectorizer.get_feature_names_out()
print(X.shape[1], "terms in the vocabulary")

lda = LatentDirichletAllocation(n_components=12, learning_method="online",
                                random_state=42, max_iter=10)
doc_topics = lda.fit_transform(X)
