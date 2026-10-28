# Listing 13.4: Engagement and conversion metrics by device
summary = sessions.groupby("device").agg(
    sessions=("pages", "size"),
    pages_per_session=("pages", "mean"),
    bounce_rate=("pages", lambda p: (p == 1).mean()),
    median_duration_s=("duration_s", "median"),
    conversion_rate=("converted", "mean"))
print(summary.round(3).T)
