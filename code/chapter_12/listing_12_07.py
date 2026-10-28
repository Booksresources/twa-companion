# Listing 12.7: A basic network drawing with NetworkX and Matplotlib
import matplotlib.pyplot as plt

pos = nx.kamada_kawai_layout(C)
color_of = {n: i for i, com in enumerate(communities) for n in com}
widths = [0.5 + w / 10 for _, _, w in C.edges(data="weight")]

plt.figure(figsize=(8, 6))
nx.draw_networkx_edges(C, pos, width=widths, edge_color="#B8C4D2")
nx.draw_networkx_nodes(C, pos, node_size=120,
                       node_color=[color_of[n] for n in C], cmap="tab10")
nx.draw_networkx_labels(C, pos, font_size=11, font_color="black")
plt.axis("off")
plt.savefig("country_network.png", dpi=300, bbox_inches="tight")
