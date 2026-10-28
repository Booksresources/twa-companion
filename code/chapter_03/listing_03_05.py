# Listing 3.5: Scraping a paginated catalogue into a DataFrame
import re
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def parse_page(html, page_url):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for card in soup.select("article.product_pod"):
        link = card.select_one("h3 a")
        price_text = card.select_one("p.price_color").get_text()
        rating_word = card.select_one("p.star-rating")["class"][1]
        rows.append({
            "title": link["title"],
            "price": float(re.search(r"\d+\.\d+", price_text).group()),
            "rating": RATINGS[rating_word],
            "url": urljoin(page_url, link["href"]),
        })
    next_link = soup.select_one("li.next a")
    next_url = urljoin(page_url, next_link["href"]) if next_link else None
    return rows, next_url

def scrape(start_url, max_pages=3):
    session = make_session()
    url, records = start_url, []
    for _ in range(max_pages):
        response = polite_get(session, url)
        rows, url = parse_page(response.text, response.url)
        records.extend(rows)
        if url is None:
            break
    return pd.DataFrame(records)

books = scrape("https://books.toscrape.com/catalogue/page-1.html", max_pages=2)
print(books.shape)
print(books[["title", "price", "rating"]].head(3))
