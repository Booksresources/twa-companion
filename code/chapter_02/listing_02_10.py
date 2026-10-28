# Listing 2.10: A clear horizontal bar chart
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

themes = ["Delivery", "Price", "Quality", "Support", "App"]
mentions = [142, 97, 88, 61, 37]

fig, ax = plt.subplots(figsize=(6.4, 3.2))
ax.barh(themes[::-1], mentions[::-1], color="#7FA7CF", edgecolor="#2F5D8C")
ax.set_xlabel(
    "Number of reviews mentioning the theme", fontsize=12, color="black"
)
ax.set_title(
    "Most discussed themes in customer reviews", fontsize=13, color="black"
)
ax.tick_params(labelsize=12, colors="black")
for y, value in enumerate(mentions[::-1]):
    ax.text(value + 2, y, str(value), va="center", fontsize=12, color="black")
ax.set_xlim(0, 165)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("themes.png", dpi=300)
