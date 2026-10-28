# Listing 6.3: A keyword-in-context concordance
from nltk.text import Text

news = Text(w.lower() for w in brown.words(categories="news"))
news.concordance("economy", width=70, lines=5)
