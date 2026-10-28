# Listing 14.2: Hashtags and engagement by account
original["hashtags"] = (
    original["text"].str.findall(r"#\w+").map(lambda t: [h.lower() for h in t])
)
original["mentions"] = original["text"].str.findall(r"@\w+")

tags = original.explode("hashtags")["hashtags"].value_counts()
print(tags.head(6).to_string())

reposts_per_post = posts["repost_of"].value_counts()
original["reposts"] = original["id"].map(reposts_per_post).fillna(0).astype(int)
by_user = original.groupby("user").agg(
    posts=("id", "size"), reposts=("reposts", "sum")
)
by_user["reposts_per_post"] = (by_user["reposts"] / by_user["posts"]).round(1)
print(by_user.sort_values("reposts", ascending=False).head(5))
