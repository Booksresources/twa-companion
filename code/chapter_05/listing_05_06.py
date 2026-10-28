# Listing 5.6: Training Word2Vec with gensim
import nltk
from gensim.models import Word2Vec

nltk.download("brown", quiet=True)
sentences = [[w.lower() for w in sent if w.isalpha()]
             for sent in nltk.corpus.brown.sents()]

model = Word2Vec(sentences, vector_size=100, window=5, min_count=5,
                 sg=1, epochs=10, workers=1, seed=42)

print(len(model.wv), "words in the vocabulary")
print(model.wv["money"].shape)
for word in ["city", "monday", "husband", "blue"]:
    print(word, "->", [w for w, _ in model.wv.most_similar(word, topn=5)])
