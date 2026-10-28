# Listing 10.1: Recognizing named entities
import spacy

nlp = spacy.load("en_core_web_sm")
text = ("In March 2025, Northwind Systems opened a research center in Toronto, "
        "investing $50 million and hiring 300 engineers. Chief executive "
        "Amara Okafor said the center would work with the University of Toronto.")
doc = nlp(text)
for ent in doc.ents:
    print(f"{ent.text:28} {ent.label_:8} {spacy.explain(ent.label_)}")
