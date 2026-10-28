# Listing 14.5: Flagging likely automated accounts
import numpy as np

def account_features(df):
    g = df.sort_values("time").groupby("user")
    feats = pd.DataFrame(
        {
            "posts": g.size(),
            "posts_per_day": g.size() / 7,
            "duplicate_share": g["text"].agg(lambda t: 1 - t.nunique() / len(t)),
            "interval_cv": g["time"].agg(
                lambda t: (
                    lambda d: d.std() / d.mean() if len(d) > 2 else np.nan
                )(t.diff().dt.total_seconds().dropna())
            ),
            "hashtags_per_post": g["text"].agg(lambda t: t.str.count("#").mean()),
        }
    )
    return feats

feats = account_features(original)
suspect = feats[
    (feats["posts_per_day"] > 10)
    & (feats["duplicate_share"] > 0.5)
    & (feats["interval_cv"] < 0.2)
]
print(suspect.round(2))
print(f"\n{len(suspect)} suspected automated accounts produced "
      f"{original['user'].isin(suspect.index).mean():.0%} of all original posts")
