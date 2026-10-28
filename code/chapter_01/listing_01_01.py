# Listing 1.1: From raw comments to frequent terms
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

reviews = pd.DataFrame({
    "channel": ["web", "app", "web", "email", "app", "web"],
    "text": [
        "Fast delivery and great price, very happy",
        "The app keeps crashing when I try to pay",
        "Great quality but delivery was slow",
        "Customer support never replied to my email",
        "Love the new design, checkout is fast",
        "Slow delivery again, and the box was damaged",
    ],
})

# Represent: count words in each review, ignoring common English stop words
vectorizer = CountVectorizer(stop_words="english")
counts = vectorizer.fit_transform(reviews["text"])

# Interpret: which terms appear most often across all reviews?
totals = pd.Series(counts.sum(axis=0).A1,
                   index=vectorizer.get_feature_names_out())
print(totals.sort_values(ascending=False).head(5))
