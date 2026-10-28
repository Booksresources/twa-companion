# Listing 4.4: Stemming versus lemmatization in NLTK
from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["studies", "studying", "better", "running", "ran", "universities", "was"]
print(f"{'word':14}{'stem':12}{'lemma (verb)':14}{'lemma (noun)'}")
for w in words:
    print(f"{w:14}{stemmer.stem(w):12}{lemmatizer.lemmatize(w, pos='v'):14}"
          f"{lemmatizer.lemmatize(w, pos='n')}")
