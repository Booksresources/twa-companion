# Listing 5.5: Collocations ranked by pointwise mutual information
import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

nltk.download("brown", quiet=True)
words = [
    w.lower() for w in nltk.corpus.brown.words(categories="news") if w.isalpha()
]

finder = BigramCollocationFinder.from_words(words)
finder.apply_freq_filter(10)                 # ignore rare pairs
print(finder.nbest(BigramAssocMeasures.pmi, 8))
