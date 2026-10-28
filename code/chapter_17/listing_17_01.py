# Listing 17.1: Monthly review volume and average rating
import re
import pandas as pd
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 12)
from nltk.sentiment import SentimentIntensityAnalyzer

reviews = pd.read_json("reviews.json")
reviews["date"] = pd.to_datetime(reviews["date"])
reviews["month"] = reviews["date"].dt.to_period("M")

monthly = reviews.groupby("month").agg(reviews=("id", "size"),
                                       avg_rating=("rating", "mean"))
print(monthly.round(2).to_string())
