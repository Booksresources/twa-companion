# Listing 16.4: Selecting few-shot examples by similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

labeled = [
    ("My parcel has been stuck at the depot for a week", "delivery"),
    ("The courier left the box in the rain and it was soaked", "delivery"),
    ("I was charged twice for the same order", "billing"),
    ("Still waiting for my refund after returning the jacket", "billing"),
    ("The zip on the bag broke after two days", "product_quality"),
    ("Colour is completely different from the photo", "product_quality"),
    ("I cannot log in since the app update", "account"),
    ("Password reset email never arrives", "account"),
]
vec = TfidfVectorizer(ngram_range=(1, 2)).fit([t for t, _ in labeled])
X = vec.transform([t for t, _ in labeled])

def select_examples(message, k=3):
    sims = cosine_similarity(vec.transform([message]), X).ravel()
    return [labeled[i] for i in sims.argsort()[::-1][:k]]

def few_shot_block(message, k=3):
    shots = select_examples(message, k)
    return "\n".join(
        f'Message: {t}\nAnswer: {{"category": "{c}"}}' for t, c in shots
    )

print(few_shot_block("I got charged for an order I cancelled and want a refund"))
