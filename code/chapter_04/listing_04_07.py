# Listing 4.7: Batch processing with nlp.pipe()
import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

def lemmas(doc):
    return [t.lemma_.lower() for t in doc
            if t.is_alpha and not t.is_stop]

reviews = ["The rooms were cleaner than expected.",
           "Staff were helpful and the breakfast was amazing.",
           "Checking in took forever; the lifts kept breaking."]

for doc in nlp.pipe(reviews, batch_size=64):
    print(lemmas(doc))
