# Listing 8.8: Calibrating the VADER threshold on rated reviews
import numpy as np
import pandas as pd
from sklearn.metrics import balanced_accuracy_score

reviews = pd.read_json("reviews.json")
english = reviews[(reviews["language"] == "en") & (reviews["rating"] != 3)].copy()
english["truth"] = np.where(english["rating"] >= 4, "positive", "negative")
english["compound"] = english["text"].map(
    lambda t: sia.polarity_scores(t)["compound"]
)

# Calibrate on half of the reviews, test the chosen threshold on the other half
calib = english.sample(frac=0.5, random_state=42)
test = english.drop(calib.index)

def score(df, threshold):
    predicted = np.where(df["compound"] > threshold, "positive", "negative")
    return balanced_accuracy_score(df["truth"], predicted)

thresholds = np.round(np.arange(-0.6, 0.61, 0.1), 1)
curve = {t: score(calib, t) for t in thresholds}
best = max(curve, key=curve.get)
print(
    f"Calibration half: best threshold {best:+.1f} (balanced accuracy "
    f"{curve[best]:.3f})"
)
print(
    f"Test half: default +0.05 -> {score(test, 0.05):.3f}   calibrated "
    f"{best:+.1f} -> {score(test, best):.3f}"
)
