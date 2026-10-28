# Listing 2.3: Essential string methods
text = "  Great Coffee, friendly staff -- but SLOW Wi-Fi!  "

clean = text.strip().lower()
print(clean)
print(clean.split())
print(clean.replace("--", ",").count(","))
print("wi-fi" in clean, clean.startswith("great"))
print(f"{len(text)} characters before, {len(clean)} after")
