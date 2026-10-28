# Listing 17.5: Country coverage by commodity topic
COUNTRIES = {"Saudi": r"Saudi", "Iran": r"Iran", "Japan": r"Japan",
             "US": r"U\.S\.|United States", "Brazil": r"Brazil",
             "China": r"China|Chinese", "USSR": r"Soviet|USSR",
             "Argentina": r"Argentin", "Colombia": r"Colombia",
             "EC": r"\bEC\b|European Community"}

for country, pattern in COUNTRIES.items():
    news[country] = news["id"].map(
        lambda f: bool(re.search(pattern, reuters.raw(f)))
    )

coverage = (
    news.groupby("topic")[list(COUNTRIES)].mean().mul(100).round(0).astype(int)
)
print(coverage.loc[["crude", "grain", "trade", "coffee", "sugar"], :].to_string())
