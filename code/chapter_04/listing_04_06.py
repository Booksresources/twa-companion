# Listing 4.6: Token annotations in spaCy
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(
    "Ms. Tanaka didn't like the new app, but she loved the faster deliveries in "
    "Nairobi."
)

for token in doc[:10]:
    print(f"{token.text:10} {token.lemma_:8} {token.pos_:6} stop={token.is_stop}")
print([(ent.text, ent.label_) for ent in doc.ents])
