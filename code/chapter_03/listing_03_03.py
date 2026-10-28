# Listing 3.3: Converting nested JSON into a DataFrame
import pandas as pd

payload = {
    "articles": [
        {
            "title": "Port traffic rises",
            "source": {"name": "Daily Wire Service", "country": "SG"},
            "published": "2025-05-02",
            "tags": ["trade", "shipping"],
        },
        {
            "title": "New rail link opens",
            "source": {"name": "Metro News", "country": "NG"},
            "published": "2025-05-03",
            "tags": ["transport"],
        },
    ]
}
df = pd.json_normalize(payload["articles"])
print(df[["title", "source.name", "source.country", "published"]])
