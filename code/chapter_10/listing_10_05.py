# Listing 10.5: Keyphrase candidates from noun chunks
from collections import Counter

doc = nlp(text)
phrases = Counter()
for chunk in doc.noun_chunks:                     # base noun phrases
    words = [t.lemma_.lower() for t in chunk if t.is_alpha and not t.is_stop]
    if words:
        phrases[" ".join(words)] += 1
print(phrases.most_common(8))
