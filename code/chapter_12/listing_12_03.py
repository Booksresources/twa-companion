# Listing 12.3: Finding orphan pages and measuring click depth
sitemap = {"index", "about", "catalogue", "science", "history", "languages",
           "events", "workshops", "news", "reading-week", "contact",
           "accessibility", "privacy", "volunteer"}
print("Orphan pages (in sitemap, never linked):", sorted(sitemap - set(G)))

depth = nx.shortest_path_length(G, source="index")   # clicks from the home page
print("Click depth:", dict(sorted(depth.items(), key=lambda kv: kv[1])))
print("Deepest pages:", [p for p, d in depth.items() if d == max(depth.values())])
