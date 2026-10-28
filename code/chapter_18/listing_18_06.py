# Listing 18.6: Redacting personal information with patterns
import re

PATTERNS = [
    ("EMAIL", r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    ("CARD",  r"\b(?:\d[ -]?){12,15}\d\b"),
    ("PHONE", r"\+?\d[\d\s-]{7,}\d"),
    ("URL",   r"https?://\S+"),
    ("USER",  r"@\w+"),
]

def redact(text):
    # order matters: emails before @mentions,
    for label, pattern in PATTERNS:
                                             # card numbers before phone numbers
        text = re.sub(pattern, f"[{label}]", text)
    return text

samples = ["Please call me on +44 20 7946 0958 or email priya.n@example.com",
           "Card 4111 1111 1111 1111 was charged twice, see "
           "https://shop.example/o/88",
           "@kwame_a said the refund never arrived"]
for s in samples:
    print(redact(s))
