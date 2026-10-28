# Listing 12.6: A country co-mention network and its communities
import re
from itertools import combinations
from nltk.corpus import reuters

COUNTRIES = ["Saudi Arabia", "Kuwait", "Iran", "Iraq", "Qatar", "Venezuela",
             "Ecuador", "Nigeria", "Indonesia", "Mexico", "Norway", "Britain",
             "Japan", "China", "Soviet Union", "Canada", "United States",
             "Brazil", "Colombia", "West Germany", "France", "Algeria", "Libya",
             "Egypt"]
ALIASES = {"U.S.": "United States", "U.K.": "Britain", "Soviet": "Soviet Union",
           "Saudi": "Saudi Arabia"}
pattern = re.compile(
    r"\b(" + "|".join(map(re.escape, COUNTRIES + list(ALIASES))) + r")\b"
)

C = nx.Graph()
for fid in reuters.fileids(["crude", "ship", "coffee"]):
    found = {ALIASES.get(m, m) for m in pattern.findall(reuters.raw(fid))}
    # every pair mentioned together
    for a, b in combinations(sorted(found), 2):
        w = C.get_edge_data(a, b, {"weight": 0})["weight"]
        C.add_edge(a, b, weight=w + 1)

C.remove_edges_from([(a, b) for a, b, w in C.edges(data="weight") if w < 3])
C.remove_nodes_from(list(nx.isolates(C)))
communities = nx.community.louvain_communities(C, weight="weight", seed=42)
print(
    C.number_of_nodes(),
    "countries,",
    C.number_of_edges(),
    "links (3+ shared articles)",
)
for i, com in enumerate(sorted(communities, key=len, reverse=True)):
    print(f"Community {i}: {', '.join(sorted(com))}")
print(
    f"Modularity: {nx.community.modularity(C, communities, weight='weight'):.3f}"
)
