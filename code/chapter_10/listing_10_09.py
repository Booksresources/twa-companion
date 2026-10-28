# Listing 10.9: Adding custom entities with the entity ruler
ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns([
    {"label": "PRODUCT", "pattern": "Aurora X2"},
    {"label": "PRODUCT", "pattern": [{"LOWER": "aurora"}, {"LOWER": "mini"}]},
    {"label": "ORG", "pattern": "Northwind Systems"},
])
doc = nlp("Customers in Nairobi compared the aurora mini with the Aurora X2 "
          "before Northwind Systems cut prices.")
print([(ent.text, ent.label_) for ent in doc.ents])
