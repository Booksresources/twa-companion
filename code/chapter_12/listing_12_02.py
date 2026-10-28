# Listing 12.2: Summarizing the link graph
G = crawl_site("http://localhost:8766/index.html", make_session())
G = nx.relabel_nodes(G, lambda u: u.rsplit("/", 1)[-1].replace(".html", ""))

print(G.number_of_nodes(), "pages,", G.number_of_edges(), "links")
print("Broken:", [n for n, s in G.nodes(data="status") if s == "broken"])
print("Pages with no outgoing links:", [n for n in G if G.out_degree(n) == 0])
print(f"Density: {nx.density(G):.3f}")
