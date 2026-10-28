# Listing 8.5: A rule-based aspect sentiment analyzer
import re
import pandas as pd
from nltk.tokenize import sent_tokenize

ASPECTS = {"room": {"room", "bed", "bathroom", "shower"},
           "staff": {"staff", "reception", "manager", "service"},
           "location": {"location", "metro", "beach", "area"},
           "food": {"breakfast", "restaurant", "food", "coffee"},
           "price": {"price", "value", "expensive", "overpriced"}}

def clauses(text):
    for sent in sent_tokenize(text):
        yield from re.split(
            r",?\s+\b(?:but|although|however|though)\b\s+", sent, flags=re.I
        )

def aspect_sentiment(reviews):
    rows = []
    for rid, text in enumerate(reviews):
        for clause in clauses(text):
            words = set(re.findall(r"[a-z]+", clause.lower()))
            for aspect, keys in ASPECTS.items():
                if words & keys:
                    rows.append(
                        {
                            "review": rid,
                            "aspect": aspect,
                            "score": sia.polarity_scores(clause)["compound"],
                        }
                    )
    return pd.DataFrame(rows)
