
from .base_scraper import BaseScraper
from app.utils.soup_utils import SoupUtils
import requests

class AmazonScraper(BaseScraper):
    def fetch(self):
        url = self.config.get("url")
        headers = self.config.get("headers", {})
        response = requests.get(url, headers=headers)
        return response.text

    def parse(self, raw_html):
        soup = SoupUtils.make_soup(raw_html)
        results = []

        for item in soup.select(".s-result-item"):
            title = item.select_one("h2")
            price = item.select_one(".a-price-whole")
            if title and price:
                results.append({
                    "title": title.text.strip(),
                    "price": price.text.strip(),
                })

        return results