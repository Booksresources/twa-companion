# Listing 10.7: Extracting acquisition relations from dependency parses
ACQUIRE = {"acquire", "buy", "purchase", "take over"}

def acquisitions(doc):
    found = []
    for tok in doc:
        if tok.pos_ == "VERB" and tok.lemma_ in ACQUIRE:
            subj = [c for c in tok.children if c.dep_ in ("nsubj",)]
            obj = [c for c in tok.children if c.dep_ in ("dobj", "obj")]
            if subj and obj:
                span = lambda t: doc[t.left_edge.i : t.right_edge.i + 1].text
                found.append((span(subj[0]), tok.lemma_, span(obj[0])))
    return found

sentences = [
    "Northwind Systems acquired a small robotics startup.",
    "Last year, Kalahari Foods bought two regional bakeries in Botswana.",
    "The deal was announced on Monday.",
    "Analysts expect that Andes Mining will purchase the smelter.",
]
for doc in nlp.pipe(sentences):
    print(acquisitions(doc))
