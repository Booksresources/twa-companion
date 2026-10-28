# Listing 17.2: Aspect mentions and low ratings before and after February 2025
ASPECT_TERMS = {   # English, Spanish, and Portuguese keywords
    "battery":    r"batter|bater[ií]a",
    "sound":      r"sound|audio|bass|sonido|\bsom\b",
    "comfort":    r"comfort|fit|ears|falling out|confort",
    "connection": r"pair|bluetooth|disconnect|desconecta",
    "delivery":   r"deliver|arrived|box|caixa|chegou",
}
for aspect, pattern in ASPECT_TERMS.items():
    reviews[aspect] = reviews["text"].str.contains(
        pattern, case=False, regex=True
    )

reviews["period"] = (reviews["date"] >= "2025-02-01").map(
    {False: "before", True: "after"}
)
rows = []
for aspect in ASPECT_TERMS:
    sub = reviews[reviews[aspect]]
    g = sub.groupby("period")
    rows.append(
        {
            "aspect": aspect,
            "mention_rate_before": reviews.loc[
                reviews.period == "before", aspect
            ].mean(),
            "mention_rate_after": reviews.loc[
                reviews.period == "after", aspect
            ].mean(),
            "low_rating_before": (g.get_group("before")["rating"] <= 2).mean(),
            "low_rating_after": (g.get_group("after")["rating"] <= 2).mean(),
        }
    )
print(pd.DataFrame(rows).set_index("aspect").round(2))
