# Listing 5.3: TF-IDF weights with TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

docs = ["the battery lasts all day",
        "the screen is bright and the battery is strong",
        "the screen cracked"]

tfidf = TfidfVectorizer()
X = tfidf.fit_transform(docs)

idf = pd.Series(tfidf.idf_, index=tfidf.get_feature_names_out()).round(2)
print(idf.sort_values().to_string())
print(pd.Series(X.toarray()[1], index=tfidf.get_feature_names_out())
        .round(2).sort_values(ascending=False).head(4))
