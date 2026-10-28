# Listing 5.1: Building a document-term matrix
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

docs = ["the battery lasts all day",
        "the screen is bright and the battery is strong",
        "the screen cracked"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)

print(type(X).__name__, X.shape)
dtm = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out(),
                   index=["doc1", "doc2", "doc3"])
print(dtm)
