# Listing 2.13: Cleaning the feedback file
import re
import html
import pandas as pd

def parse_dates(s):
    s = s.str.replace("/", "-")
    iso = pd.to_datetime(s, format="%Y-%m-%d", errors="coerce")       # 2025-03-04
    day_first = pd.to_datetime(s, format="%d-%m-%Y", errors="coerce") # 04-03-2025
    return iso.fillna(day_first)

raw = pd.read_csv("feedback_raw.csv", encoding="utf-8")
print(f"Raw rows: {len(raw)}")

clean = (raw
    # exact duplicate rows
    .drop_duplicates()
    .dropna(subset=["comment"])                              # rows without text
    .assign(
        country=lambda d: d["country"].str.strip().str.title(),
        channel=lambda d: d["channel"].str.strip().str.lower(),
        comment=lambda d: d["comment"]
            .map(html.unescape)                              # &amp; -> &
            .str.replace(r"<[^>]+>", " ", regex=True)        # remove HTML tags
            .str.replace(r"\s+", " ", regex=True).str.strip(),
        date=lambda d: parse_dates(d["date"]),
    ))
print(f"Clean rows: {len(clean)}")
print(
    clean[["id", "date", "country", "channel", "comment"]].to_string(index=False)
)
