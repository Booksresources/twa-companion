# Listing 13.2: Filtering bots, assets, and errors, and pseudonymizing visitors
import hashlib

is_bot = logs["agent"].str.contains(r"bot|crawler|spider", case=False)
is_asset = logs["path"].str.match(
    r"^/(static|images)/|\.(js|css|png|ico)$|^/robots\.txt$"
)
is_error = logs["status"] >= 400
print(
    f"Bots: {is_bot.sum():,}  Assets: {is_asset.sum():,}  Errors: "
    f"{is_error.sum():,}"
)

views = logs[~is_bot & ~is_asset & ~is_error].copy()
views["device"] = (
    views["agent"]
    .str.contains("Mobile|Android|iPhone")
    .map({True: "mobile", False: "desktop"})
)
# pseudonymous visitor key
views["visitor"] = (views["ip"] + views["agent"]).map(
    lambda s: hashlib.sha256(s.encode()).hexdigest()[:12])
views = views.drop(columns=["ip"])
print(f"Page views kept: {len(views):,}")
