# Listing 10.3: Highlighting entities with displacy
from spacy import displacy

displacy.render(doc, style="ent", jupyter=True)          # in a notebook
html = displacy.render(doc, style="ent", page=True)      # or as an HTML page
open("entities.html", "w", encoding="utf-8").write(html)
