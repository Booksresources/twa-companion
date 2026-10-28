# Listing 6.8: Comparing text statistics across languages and scripts
import unicodedata
import pandas as pd
from nltk.corpus import udhr

FILES = {"English": "English-Latin1", "Spanish": "Spanish-Latin1",
         "Swahili": "Swahili_Kiswahili-Latin1", "Yoruba": "Yoruba-UTF8",
         "Turkish": "Turkish_Turkce-UTF8", "Vietnamese": "Vietnamese-UTF8",
         "Russian": "Russian-UTF8", "Arabic": "Arabic_Alarabia-Arabic",
         "Hindi": "Hindi-UTF8", "Bengali": "Bengali-UTF8",
         "Korean": "Korean_Hankuko-UTF8", "Japanese": "Japanese_Nihongo-UTF8",
         "Chinese": "Chinese_Mandarin-GB2312"}

def script_of(text):
    letters = [unicodedata.name(c, "?").split()[0] for c in text if c.isalpha()]
    return pd.Series(letters).value_counts().index[0]

rows = []
for lang, fid in FILES.items():
    text = udhr.raw(fid)
    rows.append({"language": lang, "script": script_of(text),
                 "characters": sum(not c.isspace() for c in text),
                 "space_tokens": len(text.split()),
                 "utf8_bytes": len(text.encode("utf-8"))})
stats = pd.DataFrame(rows).set_index("language")
stats["chars_per_token"] = (stats["characters"] / stats["space_tokens"]).round(1)
stats["bytes_per_char"] = (stats["utf8_bytes"] / stats["characters"]).round(1)
print(
    stats[["script", "chars_per_token", "bytes_per_char"]]
    .sort_values("chars_per_token")
    .to_string()
)
