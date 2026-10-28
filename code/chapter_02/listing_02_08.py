# Listing 2.8: Text columns in a pandas DataFrame
import pandas as pd

df = pd.DataFrame(
    {
        "date": [
            "2025-01-03",
            "2025-01-15",
            "2025-02-02",
            "2025-02-20",
            "2025-03-11",
        ],
        "country": ["Brazil", "India", "Kenya", "India", "Germany"],
        "rating": [5, 2, 4, 3, 5],
        "text": [
            "Excellent support",
            "Late delivery, poor packaging",
            "Good value",
            "Okay product, slow refund",
            "Perfect, fast delivery",
        ],
    }
)
df["date"] = pd.to_datetime(df["date"])
df["n_words"] = df["text"].str.split().str.len()
df["mentions_delivery"] = df["text"].str.contains("delivery", case=False)

print(df[["country", "rating", "n_words", "mentions_delivery"]])
print(df.groupby("mentions_delivery")["rating"].mean())
