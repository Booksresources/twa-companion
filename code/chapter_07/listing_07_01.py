# Listing 7.1: Loading Reuters news articles by topic
import pandas as pd
from nltk.corpus import reuters

TOPICS = ["earn", "acq", "crude", "trade", "money-fx", "interest"]
rows = []
for fid in reuters.fileids():
    cats = reuters.categories(fid)
    if len(cats) == 1 and cats[0] in TOPICS:        # single-topic articles only
        rows.append({"split": fid.split("/")[0], "topic": cats[0],
                     "text": reuters.raw(fid)})
news = pd.DataFrame(rows)
train, test = news[news.split == "training"], news[news.split == "test"]

print(len(train), "training and", len(test), "test articles")
print(train["topic"].value_counts().to_string())
