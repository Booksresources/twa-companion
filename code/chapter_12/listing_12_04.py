# Listing 12.4: Implementing PageRank by power iteration
import numpy as np

def pagerank(G, d=0.85, tol=1e-10):
    nodes = list(G); n = len(nodes); idx = {u: i for i, u in enumerate(nodes)}
    pr = np.full(n, 1 / n)
    while True:
        new = np.full(n, (1 - d) / n)
        for u in nodes:
            out = list(G.successors(u))
            # share rank along outgoing links
            if out:
                for v in out:
                    new[idx[v]] += d * pr[idx[u]] / len(out)
            # dangling page: share with everyone
            else:
                new += d * pr[idx[u]] / n
        if np.abs(new - pr).sum() < tol:
            return dict(zip(nodes, new))
        pr = new

ours = pagerank(G)
theirs = nx.pagerank(G, alpha=0.85)
top = sorted(ours, key=ours.get, reverse=True)[:5]
for p in top:
    print(
        f"{p:13} ours={ours[p]:.4f}  networkx={theirs[p]:.4f}  "
        f"in-links={G.in_degree(p)}"
    )
