from . import BaseOrchestrator
from app.core.scrapers.amazon.amazon_scraper import AmazonScraper
from app.core.utils import ScraperConfig
from app.core.logger import Logger

class AmazonSearchOrchestrator(BaseOrchestrator):
    def __init__(self, keyword: str, page: int = 1, exporter: str = "file", export_config: dict = None, use_uc: bool = False):
        config = ScraperConfig(use_uc=use_uc)
        self.logger = Logger.get_logger(__name__, "amazon")
        self.keyword = keyword
        self.page = page
        scraper = AmazonScraper(config=config, logger=self.logger)

        # Bypass scraper_class, directly pass instantiated scraper
        # You must tweak BaseOrchestrator to optionally accept an instance
        self.scraper = scraper
        # self.exporter = exporter
        self.export_config = export_config or {}

    def run(self):
        self.logger.info(f"🔍 Searching Amazon for: {self.keyword}")
        data = self.scraper.search(self.keyword, self.page)
        
        if not data:
            self.logger.warning("⚠️ No products found.")
            return []

        self.logger.info(f"✅ Found {len(data)} items.")
        # self._export(data)
        return data
