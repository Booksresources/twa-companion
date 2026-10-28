# Listing 3.9: Checking robots.txt rules before crawling
from urllib.robotparser import RobotFileParser

rules = """
User-agent: *
Disallow: /checkout/
Disallow: /account/
Crawl-delay: 5
"""
robots = RobotFileParser()
robots.parse(rules.splitlines())

for path in ["/products/shoes", "/checkout/payment", "/blog/news"]:
    allowed = robots.can_fetch("TWA-Book-Bot", "https://shop.example.com" + path)
    print(f"{path:20} allowed={allowed}")
print("Crawl delay:", robots.crawl_delay("TWA-Book-Bot"), "seconds")
