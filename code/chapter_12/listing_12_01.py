# Listing 12.1: Crawling a website into a directed link graph
import networkx as nx
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_site(start_url, session, max_pages=200):
    """Breadth-first crawl of one website; returns a directed link graph."""
    site = urlparse(start_url).netloc
    G = nx.DiGraph()
    queue, seen = [start_url], {start_url}
    while queue and len(seen) <= max_pages:
        url = queue.pop(0)
        try:
            html = polite_get(session, url).text
        except Exception:
            # link target could not be fetched
            G.add_node(url, status="broken")
            continue
        G.add_node(url, status="ok")
        for a in BeautifulSoup(html, "html.parser").select("a[href]"):
            target = urljoin(url, a["href"]).split("#")[0]
            if urlparse(target).netloc != site:
                continue                          # keep internal links only
            G.add_edge(url, target)
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return G
