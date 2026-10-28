# Listing 8.6: Aspect sentiment for a set of hotel reviews
reviews = [
    "Great location near the metro, but the room was tiny and noisy.",
    "The staff at reception were wonderful and the breakfast was excellent.",
    "Overpriced for what you get. The bathroom was dirty.",
    "Lovely beach area. Breakfast was average, though the coffee was great.",
    "Friendly staff, comfortable bed, fair price.",
    "The manager ignored our complaint and the shower was broken.",
    "Perfect location and good value, but the restaurant was disappointing.",
    "Clean, spacious room. The service was slow at dinner.",
]
aspects = aspect_sentiment(reviews)
summary = (aspects.groupby("aspect")["score"]
                  .agg(mentions="count", mean_score="mean")
                  .round(2).sort_values("mean_score"))
print(summary)
