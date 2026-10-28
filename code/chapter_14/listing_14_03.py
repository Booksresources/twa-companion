# Listing 14.3: A repost network and influence ranking
import networkx as nx

author = posts.set_index("id")["user"]
rp = posts[posts["is_repost"]].copy()
rp["original_author"] = rp["repost_of"].map(author)

# edge: reposter -> original author
R = nx.DiGraph()
for (src, dst), n in rp.groupby(["user", "original_author"]).size().items():
    R.add_edge(src, dst, weight=n)

pr = pd.Series(nx.pagerank(R, weight="weight")).sort_values(ascending=False)
# distinct accounts that reposted them
reach = pd.Series({u: R.in_degree(u) for u in R})
table = pd.DataFrame({"pagerank": pr.round(3), "distinct_reposters": reach})
print(table.sort_values("pagerank", ascending=False).head(6))
