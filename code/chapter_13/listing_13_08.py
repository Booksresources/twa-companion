# Listing 13.8: Which site searches fail?
searches = views[views["path"].str.startswith("/search")].copy()
searches["query"] = (
    searches["path"].str.extract(r"q=([^&]+)")[0].str.replace("+", " ")
)
searches["next"] = views.loc[searches.index, "next"]

report = searches.groupby("query").agg(
    searches=("query", "size"),
    exit_rate=("next", lambda n: (n == "exit").mean()),
    to_product=("next", lambda n: (n == "product").mean()))
print(report.sort_values("exit_rate", ascending=False).round(2).head(6))
