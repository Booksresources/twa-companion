# Listing 4.5: Snowball stemmers for other languages
from nltk.stem.snowball import SnowballStemmer

for lang, words in [("spanish", ["corriendo", "corrieron", "correr"]),
                    ("german", ["Häuser", "Hauses", "Haus"]),
                    ("french", ["mangeons", "mangeait", "manger"])]:
    stemmer = SnowballStemmer(lang)
    print(lang, [stemmer.stem(w) for w in words])
