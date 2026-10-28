# Listing 2.6: Extracting hashtags, links, prices, and emails
import re

post = ("Loved the #DataScience meetup! Slides: https://example.org/slides "
        "Tickets were $25.00 (now $19.99). Contact info@example.org #NLP")

print(re.findall(r"#\w+", post))
print(re.findall(r"https?://\S+", post))
print(re.findall(r"\$\d+(?:\.\d{2})?", post))
print(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", post))
