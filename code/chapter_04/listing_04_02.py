# Listing 4.2: Lowercasing, case folding, and accent removal
import unicodedata

def strip_accents(text):
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")

for s in ["Café Crème", "straße", "İstanbul"]:
    print(s, "| lower:", s.lower(), "| casefold:", s.casefold(),
          "| no accents:", strip_accents(s))
print(len("İstanbul".lower()), "characters after lower()")
