from typing import  Optional
from bs4 import BeautifulSoup, FeatureNotFound

from core import Logger
logger = Logger.get_logger(__name__,'Utils')


class SoupUtils:
    @staticmethod
    def make_soup(response: str) -> Optional[BeautifulSoup]:
        try:
            soup = BeautifulSoup(response, "lxml")
            logger.info("✅ Soup created successfully")
            return soup
        except (FeatureNotFound, TypeError) as e:
            logger.error(f"❌ Failed to create soup: {e}")
            return None
