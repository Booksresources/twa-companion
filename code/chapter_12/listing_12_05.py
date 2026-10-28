# Listing 12.5: Comparing degree, PageRank, and betweenness
import pandas as pd

metrics = pd.DataFrame({
    "in_degree": dict(G.in_degree()),
    "pagerank": nx.pagerank(G),
    "betweenness": nx.betweenness_centrality(G),
}).round(3)
print(metrics.sort_values("betweenness", ascending=False).head(5))
