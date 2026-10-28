# Listing 13.6: Transition probabilities between page types
def page_type(path):
    for prefix, name in [
        ("/product/", "product"),
        ("/category/", "category"),
        ("/search", "search"),
        ("/cart", "cart"),
        ("/checkout", "checkout"),
        ("/confirmation", "purchase"),
    ]:
        if path.startswith(prefix):
            return name
    return "home" if path == "/" else "other"

views["page"] = views["path"].map(page_type)
views["next"] = views.groupby("session")["page"].shift(-1).fillna("exit")
transitions = pd.crosstab(views["page"], views["next"], normalize="index").round(
    2
)
order = ["home", "category", "search", "product", "cart", "checkout", "purchase"]
print(transitions.loc[order, order + ["exit"]])
