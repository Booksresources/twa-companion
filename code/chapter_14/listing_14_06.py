# Listing 14.6: Daily volume and sentiment after removing automated accounts
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
humans = original[~original["user"].isin(suspect.index)].copy()
humans["sentiment"] = humans["text"].map(
    lambda t: sia.polarity_scores(t)["compound"]
)

daily = humans.set_index("time").resample("D").agg(
    posts=("id", "size"), mean_sentiment=("sentiment", "mean"),
    share_negative=("sentiment", lambda s: (s <= -0.05).mean()))
print(daily.round(2))
