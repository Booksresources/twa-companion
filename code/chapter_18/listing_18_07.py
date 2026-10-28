# Listing 18.7: Measuring sentiment accuracy by language
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.metrics import recall_score

reviews = pd.read_json("reviews.json")
# clear opinions only
labeled = reviews[reviews["rating"] != 3].copy()
labeled["truth"] = (labeled["rating"] >= 4).map(
    {True: "positive", False: "negative"}
)

sia = SentimentIntensityAnalyzer()
labeled["predicted"] = labeled["text"].map(
    lambda t: (
        "positive" if sia.polarity_scores(t)["compound"] >= 0 else "negative"
    )
)

def group_report(df, group):
    rows = {}
    for g, d in df.groupby(group):
        rows[g] = {
            "reviews": len(d),
            "accuracy": (d["truth"] == d["predicted"]).mean(),
            "recall_negative": recall_score(
                d["truth"], d["predicted"], pos_label="negative"
            ),
        }
    report = pd.DataFrame(rows).T.round(2)
    report["reviews"] = report["reviews"].astype(int)
    return report

print(group_report(labeled, "language"))
