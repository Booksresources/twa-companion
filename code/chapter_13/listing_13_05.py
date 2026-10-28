# Listing 13.5: A purchase funnel by device
steps = {"Product": r"^/product/", "Cart": r"^/cart$",
         "Checkout": r"^/checkout$", "Purchase": r"^/confirmation$"}

reached = pd.DataFrame({step: views.groupby("session")["path"].apply(
                            lambda p, rx=rx: p.str.match(rx).any())
                        for step, rx in steps.items()})
reached["device"] = sessions["device"]

funnel = reached.groupby("device")[list(steps)].sum().T
for dev in funnel.columns:
    funnel[f"{dev}_step_rate"] = (funnel[dev] / funnel[dev].shift(1)).round(2)
print(funnel)
