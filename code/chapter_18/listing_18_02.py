# Listing 18.2: Monitoring vocabulary drift
import re
import pandas as pd
import numpy as np
from collections import Counter
from scipy.spatial.distance import jensenshannon

reviews = pd.read_json("reviews.json")
reviews["month"] = pd.to_datetime(reviews["date"]).dt.to_period("M")
def distribution(texts, vocab):
    c = Counter(w for t in texts for w in re.findall(r"\w+", t.lower()))
    v = np.array([c[w] for w in vocab], dtype=float) + 1   # add-one smoothing
    return v / v.sum()

vocab = sorted(
    {w for t in reviews["text"] for w in re.findall(r"\w+", t.lower())}
)
months = sorted(reviews["month"].unique())
baseline = distribution(reviews[reviews["month"].isin(months[:3])]["text"], vocab)
drift = {
    str(m): jensenshannon(
        baseline, distribution(reviews[reviews["month"] == m]["text"], vocab)
    )
    for m in months[3:]
}
threshold = 1.5 * np.median(list(drift.values())[:3])
for m, d in drift.items():
    print(f"{m}  {d:.3f}  {'ALERT' if d > threshold else ''}")
