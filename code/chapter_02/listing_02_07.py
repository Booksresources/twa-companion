# Listing 2.7: A small cleaning routine with re.sub()
import re

raw = "<p>Fast   shipping!!! Visit https://shop.example.com NOW :)</p>"

text = re.sub(r"<[^>]+>", " ", raw)            # remove HTML tags
text = re.sub(r"https?://\S+", " URL ", text)   # replace links with a token
text = re.sub(r"([!?.])\1+", r"\1", text)       # collapse repeated punctuation
text = re.sub(r"\s+", " ", text).strip()        # normalize whitespace
print(text)
