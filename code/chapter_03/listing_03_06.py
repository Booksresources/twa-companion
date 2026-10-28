# Listing 3.6: A Scrapy spider for the same catalogue
import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]
    custom_settings = {
        "ROBOTSTXT_OBEY": True,
        "DOWNLOAD_DELAY": 1.0,
        "AUTOTHROTTLE_ENABLED": True,
        "USER_AGENT": "TWA-Book-Bot/1.0 (educational; your.email@example.org)",
        "FEEDS": {"books.jsonl": {"format": "jsonlines", "encoding": "utf8"}},
    }

    def parse(self, response):
        for card in response.css("article.product_pod"):
            yield {
                "title": card.css("h3 a::attr(title)").get(),
                "price": card.css("p.price_color::text").re_first(r"\d+\.\d+"),
                "rating": (card.css("p.star-rating::attr(class)")
                           .get().split()[-1]),
            }
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
