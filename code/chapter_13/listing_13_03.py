# Listing 13.3: Sessionizing page views with a 30-minute timeout
views = views.sort_values(["visitor", "time"])
gap = views.groupby("visitor")["time"].diff()
new_session = gap.isna() | (gap > pd.Timedelta(minutes=30))
views["session"] = new_session.cumsum()

sessions = views.groupby("session").agg(
    visitor=("visitor", "first"), device=("device", "first"),
    start=("time", "min"), end=("time", "max"),
    pages=("path", "size"), entry=("path", "first"), exit=("path", "last"),
    converted=("path", lambda p: (p == "/confirmation").any()))
sessions["duration_s"] = (sessions["end"] - sessions["start"]).dt.total_seconds()
print(f"{sessions['visitor'].nunique():,} visitors, {len(sessions):,} sessions")
