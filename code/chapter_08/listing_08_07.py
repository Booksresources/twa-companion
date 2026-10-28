# Listing 8.7: Extending the lexicon with domain-specific words
for w in ["overpriced", "noisy", "tiny", "spacious", "dirty"]:
    print(f"{w:11} {sia.lexicon.get(w)}")

sia.lexicon.update(
    {"overpriced": -2.0, "noisy": -1.5, "tiny": -1.0, "spacious": 1.5}
)
updated = aspect_sentiment(reviews)
print(
    updated.groupby("aspect")["score"].mean().round(2).sort_values().to_string()
)
