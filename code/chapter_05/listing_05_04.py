# Listing 5.4: Adding bigrams with ngram_range
from sklearn.feature_extraction.text import CountVectorizer

docs = ["not good at all", "very good value", "good but not great"]
bigram_vec = CountVectorizer(ngram_range=(1, 2))
bigram_vec.fit(docs)
print(bigram_vec.get_feature_names_out())
