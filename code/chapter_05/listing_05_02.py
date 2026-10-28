# Listing 5.2: Pruning the vocabulary with CountVectorizer options
from sklearn.feature_extraction.text import CountVectorizer

vec = CountVectorizer(lowercase=True,
                      stop_words="english",    # drop common English words
                      # keep terms in at least 2 documents
                      min_df=2,
                      # drop terms in over 90% of documents
                      max_df=0.9,
                      max_features=5000)        # cap the vocabulary size
corpus = ["Fast delivery, great price", "Slow delivery and poor packaging",
          "Great price but slow support", "Support was fast and friendly"]
X = vec.fit_transform(corpus)
print(vec.get_feature_names_out())
print(X.toarray())
