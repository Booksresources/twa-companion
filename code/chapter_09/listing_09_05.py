# Listing 9.5: Comparing coherence for different numbers of topics
from gensim.corpora import Dictionary
from gensim.models import CoherenceModel

analyzer = vectorizer.build_analyzer()
vocab = set(terms)
tokenized = [[w for w in analyzer(d) if w in vocab] for d in docs]
dictionary = Dictionary(tokenized)

def coherence(model, terms, n=10):
    topics = [list(terms[w.argsort()[-n:][::-1]]) for w in model.components_]
    cm = CoherenceModel(topics=topics, texts=tokenized, dictionary=dictionary,
                        coherence="c_v", processes=1)
    return cm.get_coherence()

for k in [4, 8, 12, 16, 20]:
    m = LatentDirichletAllocation(n_components=k, learning_method="online",
                                  random_state=42, max_iter=10).fit(X)
    print(f"k={k:2}  coherence={coherence(m, terms):.3f}")
