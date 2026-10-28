# Listing 10.4: Keyphrases with YAKE
import yake

text = ("Coastal cities around the world are investing in flood defences as "
        "sea levels rise.\nRotterdam combines storm surge barriers with "
        "floating neighbourhoods, while Jakarta is\nbuilding a giant sea "
        "wall and Lagos is restoring mangrove forests. Urban planners say\n"
        "that nature-based solutions such as mangrove restoration can be "
        "cheaper than concrete\nbarriers and also protect biodiversity. "
        "However, financing remains the main obstacle\nfor many coastal "
        "cities in low-income countries.")

extractor = yake.KeywordExtractor(lan="en", n=2, top=8, dedupLim=0.3)
for phrase, score in extractor.extract_keywords(text):
    print(f"{score:.4f}  {phrase}")      # lower scores mean more relevant
