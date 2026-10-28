# Listing 4.3: Removing stop words, with exceptions
from nltk.corpus import stopwords

stop_en = set(stopwords.words("english"))
tokens = ["the", "service", "was", "not", "good", "and", "very", "slow"]

print([t for t in tokens if t not in stop_en])

keep = {"not", "no", "nor", "very"}            # words that carry meaning here
custom_stop = stop_en - keep
print([t for t in tokens if t not in custom_stop])
print(len(stop_en), "English stop words;",
      len(stopwords.words("spanish")), "Spanish stop words")
