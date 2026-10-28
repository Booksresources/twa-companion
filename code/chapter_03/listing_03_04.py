# Listing 3.4: Parsing HTML with BeautifulSoup
from bs4 import BeautifulSoup

html = """
<html><body>
  <h1>Community Library: New Arrivals</h1>
  <div class="book" data-id="101">
    <h2 class="title">Data and Society</h2>
    <span class="author">A. Mensah</span>
    <span class="lang">English</span>
    <a href="/books/101">Details</a>
  </div>
  <div class="book" data-id="102">
    <h2 class="title">La ciudad digital</h2>
    <span class="author">L. García</span>
    <span class="lang">Spanish</span>
    <a href="/books/102">Details</a>
  </div>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.h1.get_text(strip=True))

for card in soup.select("div.book"):
    title = card.select_one("h2.title").get_text(strip=True)
    author = card.select_one(".author").get_text(strip=True)
    link = card.find("a")["href"]
    print(card["data-id"], "|", title, "|", author, "|", link)
