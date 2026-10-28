# Listing 13.9: Engagement and conversion by traffic source
def channel(referrer):
    if referrer in ("-", ""):
        return "direct"
    if "google." in referrer or "bing." in referrer:
        return "search engine"
    if "facebook." in referrer or "instagram." in referrer:
        return "social media"
    if "shop.example.com" in referrer:
        return "internal"
    return "referral"

first = views.sort_values("time").groupby("session").first()
sessions["channel"] = first["referrer"].map(channel)
by_channel = sessions.groupby("channel").agg(
    sessions=("pages", "size"), bounce_rate=("pages", lambda p: (p == 1).mean()),
    conversion_rate=("converted", "mean"), purchases=("converted", "sum"))
p, n = by_channel["conversion_rate"], by_channel["sessions"]
margin = 1.96 * (p * (1 - p) / n) ** 0.5            # 95% confidence interval
by_channel["ci_low"], by_channel["ci_high"] = p - margin, p + margin
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 10)
print(by_channel.round(3).sort_values("sessions", ascending=False))
