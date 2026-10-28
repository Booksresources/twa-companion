# Listing 11.2: Clustering news articles with k-means
import re
import pandas as pd
from nltk.corpus import reuters
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

TOPICS = ["crude", "grain", "money-fx", "ship", "coffee", "gold"]
ids = [f for f in reuters.fileids()
       if len(reuters.categories(f)) == 1 and reuters.categories(f)[0] in TOPICS]
texts = [re.sub(r"&lt;|<[^>]+>", " ", reuters.raw(f)) for f in ids]
topics = [reuters.categories(f)[0] for f in ids]

tfidf = TfidfVectorizer(stop_words="english", min_df=3, max_df=0.5,
                        token_pattern=r"(?u)\b[a-zA-Z]{3,}\b")
X = tfidf.fit_transform(texts)
km = KMeans(n_clusters=6, n_init=10, random_state=42).fit(X)

terms = tfidf.get_feature_names_out()
for c, center in enumerate(km.cluster_centers_):
    print(f"Cluster {c}: {', '.join(terms[center.argsort()[-6:][::-1]])}")
print(
    f"\n{X.shape[0]} articles | silhouette={silhouette_score(X, km.labels_):.3f}"
    f" | adjusted Rand index={adjusted_rand_score(topics, km.labels_):.3f}"
)
