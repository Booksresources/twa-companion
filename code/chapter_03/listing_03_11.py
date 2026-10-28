# Listing 3.11: Crawling through the cache twice
def crawl_catalogue(start_url, cache, session, max_pages=3):
    url, records = start_url, []
    for _ in range(max_pages):
        rows, url = parse_page(cache.get(session, url), url)
        records.extend(rows)
        if url is None:
            break
    return records

session = make_session()
for run in (1, 2):
    cache = PageCache()
    books = crawl_catalogue(
        "https://books.toscrape.com/catalogue/page-1.html", cache, session
    )
    print(
        f"Run {run}: {len(books)} books, {cache.downloads} downloads, "
        f"{cache.hits} from cache"
    )
