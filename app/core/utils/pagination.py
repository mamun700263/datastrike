from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import Optional

from ...core import Logger
logger = Logger.get_logger(__name__,'Utils')

class Pagination:
    @staticmethod
    def get_next_url(soup: BeautifulSoup, base_url: str) -> Optional[str]:
        logger.debug("📄 Checking for pagination...")
        try:
            next_page = soup.find("a", class_="s-pagination-next")
            if not next_page or not next_page.get("href"):
                logger.warning("⚠️ No next page link found")
                return None
            next_url = urljoin(base_url, next_page["href"])
            logger.info(f"➡️ Found next page URL: {next_url}")
            return next_url
        except (AttributeError, TypeError) as e:
            logger.error(f"❌ Pagination error: {e}")
            return None
