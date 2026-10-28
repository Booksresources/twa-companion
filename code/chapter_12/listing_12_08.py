# Listing 12.8: Hub and authority scores for the library website
hubs, authorities = nx.hits(G, max_iter=1000, normalized=True)
hits_table = pd.DataFrame({"hub": hubs, "authority": authorities,
                           "pagerank": nx.pagerank(G)}).round(3)
print("Top hubs:")
print(hits_table.sort_values("hub", ascending=False).head(3))
print("\nTop authorities:")
print(hits_table.sort_values("authority", ascending=False).head(3))
