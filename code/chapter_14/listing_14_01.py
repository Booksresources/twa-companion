# Listing 14.1: Loading the post dataset
import pandas as pd
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 10)

posts = pd.read_json("posts.json")
posts["time"] = pd.to_datetime(posts["time"])
posts["is_repost"] = posts["repost_of"].notna()
original = posts[~posts["is_repost"]].copy()

print(f"{len(posts):,} posts by {posts['user'].nunique():,} accounts, "
      f"{posts['time'].min():%d %b} to {posts['time'].max():%d %b %Y}")
print(
    f"Original posts: {len(original):,}   Reposts: {posts['is_repost'].sum():,}"
)
