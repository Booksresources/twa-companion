# Listing 3.7: Rendering a JavaScript page with Playwright
# Setup: pip install playwright   then   playwright install chromium
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(user_agent="TWA-Book-Bot/1.0 (educational)")
    page.goto("https://quotes.toscrape.com/js/", timeout=30000)
    page.wait_for_selector("div.quote")       # wait until content appears
    quotes = page.locator("div.quote span.text").all_inner_texts()
    browser.close()

print(len(quotes), "quotes collected")
