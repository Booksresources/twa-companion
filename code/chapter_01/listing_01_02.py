# Listing 1.2: A minimal rule-based sentiment score
positive = {"fast", "great", "happy", "love"}
negative = {"crashing", "slow", "damaged", "never"}

def score(text):
    words = set(text.lower().replace(",", "").split())
    return len(words & positive) - len(words & negative)

reviews["score"] = reviews["text"].apply(score)
print(reviews.groupby("channel")["score"].mean())
