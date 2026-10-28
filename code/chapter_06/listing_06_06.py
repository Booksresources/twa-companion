# Listing 6.6: Type-token ratio of the same text in six languages
import nltk
from nltk.corpus import udhr

nltk.download("udhr", quiet=True)
languages = {"English": "English-Latin1", "Spanish": "Spanish-Latin1",
             "German": "German_Deutsch-Latin1", "Finnish": "Finnish_Suomi-Latin1",
             "Swahili": "Swahili_Kiswahili-Latin1",
             "Indonesian": "Indonesian-Latin1"}

for name, fileid in languages.items():
    words = [w.lower() for w in udhr.words(fileid) if w.isalpha()]
    ttr = len(set(words)) / len(words)
    print(
        f"{name:11} tokens={len(words):5}  types={len(set(words)):5}  "
        f"TTR={ttr:.2f}"
    )
