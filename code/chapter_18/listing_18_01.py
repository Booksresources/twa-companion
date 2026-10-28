# Listing 18.1: A production-style pipeline script
"""review_pipeline.py: daily job that summarizes new reviews."""
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

CONFIG = {"input": "reviews.json",
          "output_dir": "outputs",
          "min_reviews": 20,
          "aspects": {"battery": r"batter|bater[ií]a",
                      "sound": r"sound|audio|sonido|\bsom\b",
                      "connection": r"pair|bluetooth|disconnect|desconecta"}}
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
)
log = logging.getLogger("review_pipeline")

def load(path):
    df = pd.read_json(path)
    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
    return df

def validate(df):
    problems = []
    if df["text"].isna().any(): problems.append("missing text")
    if not df["rating"].between(1, 5).all():
        problems.append("rating out of range")
    if df["id"].duplicated().any(): problems.append("duplicate ids")
    return problems

def summarize(df, aspects):
    for name, pattern in aspects.items():
        df[name] = df["text"].str.contains(pattern, case=False, regex=True)
    return (
        df.groupby("month")
        .agg(
            reviews=("id", "size"),
            avg_rating=("rating", "mean"),
            **{f"{a}_share": (a, "mean") for a in aspects},
        )
        .round(3)
    )

def run(config):
    df = load(config["input"])
    if problems := validate(df):
        log.error("Validation failed: %s", problems); return None
    if len(df) < config["min_reviews"]:
        log.warning("Only %d reviews; skipping", len(df)); return None
    summary = summarize(df, config["aspects"])
    out = Path(config["output_dir"]); out.mkdir(exist_ok=True)
    summary.to_csv(out / "monthly_summary.csv")
    meta = {
        "run_at": datetime.now(timezone.utc).isoformat(),
        "rows": len(df),
        "config": config,
    }
    (out / "run_metadata.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False)
    )
    log.info("Wrote summary for %d months from %d reviews", len(summary), len(df))
    return summary

if __name__ == "__main__":
    run(CONFIG)
