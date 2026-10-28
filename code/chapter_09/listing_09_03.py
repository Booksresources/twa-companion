# Listing 9.3: Topics from NMF on TF-IDF features
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

tfidf = TfidfVectorizer(stop_words="english", min_df=10, max_df=0.5,
                        token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z]{2,}\b")
T = tfidf.fit_transform(docs)
nmf = NMF(n_components=12, init="nndsvd", random_state=42, max_iter=400)
doc_topics_nmf = nmf.fit_transform(T)
show_topics(nmf, tfidf.get_feature_names_out())
