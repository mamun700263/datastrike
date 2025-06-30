import time

from core.utils  import Humanizer
from selenium.common.exceptions import WebDriverException, TimeoutException

from core import Logger
logger = Logger.get_logger(__name__,'Utils')


class Scroller:
    @staticmethod
    def get_scroll_height(driver) -> int:
        return driver.execute_script("return document.body.scrollHeight")

    @staticmethod
    def scroll_and_wait(driver, wait_time=2, scroll_pause=0.5, max_scrolls=10):
        last_height = Scroller.get_scroll_height(driver)

        for i in range(max_scrolls):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)
            new_height = Scroller.get_scroll_height(driver)

            logger.debug(f"🔁 Scroll {i+1}: height changed to {new_height}")
            if new_height == last_height:
                logger.info("📉 No new content loaded — stopping scroll")
                break
            last_height = new_height

        logger.info(f"✅ Scrolling completed with {i+1} scroll(s)")
        time.sleep(wait_time)

    @staticmethod
    def load_and_scroll(driver, url: str):
        try:
            logger.info(f"🌐 Navigating to: {url}")
            driver.set_page_load_timeout(15)
            driver.get(url)
            Humanizer.sleep_random()
            Scroller.scroll_and_wait(driver)
            logger.info(f"✅ Successfully loaded and scrolled: {url}")
        except (TimeoutException, WebDriverException) as e:
            logger.error(f"❌ Failed to load {url}: {e}")
