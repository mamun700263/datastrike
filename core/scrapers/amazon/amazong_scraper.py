from typing import List, Dict

from urllib.parse import quote_plus

from ...logger import Logger
from core.utils.selenium_utils import ScraperConfig
from core.utils.soup_utils import SoupUtils
from core.utils.scroller import Scroller
from core.utils.pagination import Pagination
from core.utils.humanizer import Humanizer
from amazon import ProductExtractor


class AmazonScraper:
    def __init__(self, config: ScraperConfig, logger: Logger):
        self.config = config
        self.driver = config.get_driver()
        self.logger = logger
        self.url = "https://www.amazon.com"
        self.logger.info("🚀 AmazonScraper initialized")

    def _get_search_url(self, keyword: str) -> str:
        encoded = quote_plus(keyword)
        search_url = f"{self.url}/s?k={encoded}"
        self.logger.debug(f"🔗 Generated search URL: {search_url}")
        return search_url

    def _scrape_search_results(self, keyword: str, wait_time: int=3) -> str:
        url = self._get_search_url(keyword)
        self.logger.info(f"🌐 Navigating to search page: {url}")
        try:
            Scroller.load_and_scroll(self.driver,url)
            self.logger.info("✅ Page loaded and ready for scraping")
            return self.driver.page_source
        except Exception as e:
            self.logger.error(f"❌ Error loading page for keyword '{keyword}': {e}")
            return ""

    def scrape_all_pages(self, keyword: str, max_pages=5)-> List[Dict[str, str]]:
        results = []
        response = self._scrape_search_results(keyword)
        soup = SoupUtils.make_soup(response)
        page = 0
        amazon_extractor = ProductExtractor(soup,self.url,self.logger)

        while soup and page < max_pages: #apply retry here
            data = amazon_extractor.extract()
            results += data

            self.logger.info(f"📄 Page {page + 1} scraped.")

            next_page_url = Pagination.get_next_url(soup,self.url)
            # next_page_url = next_page_url[:-1]+(next_page_url[-1]+1)
            if not next_page_url:
                break

            self.driver.get(next_page_url)
            Humanizer.sleep_random(2,5)
            soup = SoupUtils.make_soup(self.driver.page_source)
            page += 1

        return results

    def quit(self):
        self.logger.info("🛑 Quitting WebDriver")
        self.driver.quit()