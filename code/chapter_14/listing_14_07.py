# Listing 14.7: Cascade sizes, concentration, and timing
import numpy as np

humans_only = original[~original["user"].isin(suspect.index)]
# cascade size = reposts per original post
sizes = humans_only["reposts"]
print(
    f"{len(sizes):,} original posts by people; {sizes.sum():,} reposts in total"
)
print(f"Posts with no reposts: {(sizes == 0).mean():.0%}")
top = sizes.sort_values(ascending=False)
top1 = top.head(max(1, len(top) // 100))
print(
    f"Largest 1% of cascades ({len(top1)} posts) hold "
    f"{top1.sum() / sizes.sum():.0%} of all reposts"
)

hours = (
    posts[posts["is_repost"]]
    .assign(orig_time=lambda d: d["repost_of"].map(posts.set_index("id")["time"]))
    .eval("delay = (time - orig_time).dt.total_seconds() / 3600")["delay"]
)
print(
    f"Median time to repost: {hours.median():.1f} hours; 90% within "
    f"{hours.quantile(0.9):.1f} hours"
)
influencer_share = (
    humans_only.loc[humans_only["user"].isin(pr.index[:5]), "reposts"].sum()
    / sizes.sum()
)
print(f"Reposts of the five most influential accounts: {influencer_share:.0%}")
