# Listing 17.8: A combined behavior and search audit
# Continues from the bookstore session data of Listings 13.1-13.3 and 13.6
pages = views.groupby("page").agg(
    views=("path", "size"), exit_rate=("next", lambda n: (n == "exit").mean())
)
pages["exits"] = (pages["views"] * pages["exit_rate"]).round().astype(int)

device_checkout = (
    views[views["page"] == "checkout"]
    .groupby("device")["next"]
    .apply(lambda n: (n == "exit").mean())
)
failed = (
    views[views["page"] == "search"]
    .assign(
        query=lambda d: d["path"]
        .str.extract(r"q=([^&]+)")[0]
        .str.replace("+", " ")
    )
    .groupby("query")["next"]
    .apply(lambda n: (n == "exit").mean())
)

print(pages.sort_values("exits", ascending=False).round(2).head(4))
print("\nCheckout exit rate by device:", device_checkout.round(2).to_dict())
print("Searches with exit rate above 50%:", sorted(failed[failed > 0.5].index))
