# Listing 2.4: Characters, bytes, and Unicode normalization
import unicodedata

for word in ["data", "café", "数据", "datos 📊"]:
    encoded = word.encode("utf-8")
    print(f"{word}: {len(word)} characters, {len(encoded)} bytes")

a = "caf\u00e9"          # é as one precomposed code point
b = "cafe\u0301"         # e + combining acute accent
print(a == b)
print(unicodedata.normalize("NFC", a) == unicodedata.normalize("NFC", b))
