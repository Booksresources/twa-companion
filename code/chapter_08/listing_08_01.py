# Listing 8.1: Scoring sentences with VADER
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()       # requires nltk.download("vader_lexicon")
examples = ["The battery is good.",
            "The battery is not good.",
            "The battery is very good!",
            "The battery is VERY GOOD!!!",
            "The screen is great, but the battery is awful.",
            "Delivery was fast 😊",
            "Oh great, it broke after one day."]
for text in examples:
    s = sia.polarity_scores(text)
    print(
        f"{s['compound']:+.3f}  neg={s['neg']:.2f} neu={s['neu']:.2f} "
        f"pos={s['pos']:.2f}  {text}"
    )
