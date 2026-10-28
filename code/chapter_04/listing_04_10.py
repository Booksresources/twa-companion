# Listing 4.10: A configurable preprocessing function
import re
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
KEEP = {"no", "not", "never", "very"}

def normalize(text):
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"(\w)\1{2,}", r"\1\1", text)
    return re.sub(r"\s+", " ", text).strip()

def preprocess(texts, lemmatize=True, remove_stop=True, min_len=2):
    cleaned = (normalize(t) for t in texts)
    results = []
    for doc in nlp.pipe(cleaned, batch_size=256):
        tokens = []
        for t in doc:
            if not t.is_alpha or len(t) < min_len:
                continue
            if remove_stop and t.is_stop and t.lower_ not in KEEP:
                continue
            tokens.append(t.lemma_.lower() if lemmatize else t.lower_)
        results.append(tokens)
    return results

df = pd.DataFrame({"text": [
    "Not worth the price!!! Battery died after 2 days https://example.com",
    "Absolutely loooove the camera, very sharp photos",
    "Never received a reply from support."]})
df["tokens"] = preprocess(df["text"])
print(df["tokens"].tolist())
