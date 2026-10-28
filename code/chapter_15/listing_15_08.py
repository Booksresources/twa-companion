# Listing 15.8: Measuring tokenizer fertility across languages
from nltk.corpus import udhr

SAMPLES = {"English": "English-Latin1", "Spanish": "Spanish-Latin1",
           "Swahili": "Swahili_Kiswahili-Latin1",
           "Indonesian": "Indonesian-Latin1", "Turkish": "Turkish_Turkce-UTF8",
           "Yoruba": "Yoruba-UTF8", "Vietnamese": "Vietnamese-UTF8",
           "Russian": "Russian-UTF8", "Hindi": "Hindi-UTF8"}

print(f"{'language':11} {'tokens per word':>15}   {'[UNK] share':>11}")
for lang, fid in SAMPLES.items():
    words = udhr.raw(fid).lower().split()[:1000]
    pieces = [tokenizer.encode(w).tokens for w in words]
    n_tokens = sum(len(p) for p in pieces)
    unknown = sum(t == "[UNK]" for p in pieces for t in p) / n_tokens
    print(f"{lang:11} {n_tokens / len(words):15.2f}   {unknown:11.0%}")
