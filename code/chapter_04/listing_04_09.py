# Listing 4.9: Detecting the language of short texts
from langdetect import detect_langs, DetectorFactory

DetectorFactory.seed = 0          # make results repeatable
texts = ["The delivery arrived two days late.",
         "La entrega llegó dos días tarde.",
         "La livraison est arrivée avec deux jours de retard.",
         "Die Lieferung kam zwei Tage zu spät an.",
         "Uwasilishaji ulichelewa kwa siku mbili."]
for t in texts:
    best = detect_langs(t)[0]
    print(f"{best.lang} ({best.prob:.2f})  {t}")
