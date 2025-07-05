import random, os, json

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options as ChromeOptions

from typing import List, Optional, Union

from dotenv import load_dotenv

from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from ...core import Logger

logger = Logger.get_logger(__name__, 'Utils')
load_dotenv()

API_KEYS = {
    'scrapeops':os.getenv("SCRAPEOPS_API_KEY"),
    'scrapingbee':os.getenv("SCRAPINGBEE_API_KEY"),
    'scraperapi':os.getenv("SCRAPERAPI_API_KEY"),
    'scrapedo':os.getenv("SCRAPEDO_API_KEY"),
}


class ScraperConfig:

    SCRAPEOPS_API_KEY: str = os.getenv("SCRAPEOPS_API_KEY")
    

    def __init__(self, use_uc=False, headless=False, incognito=True, user_agent=None, use_proxy= False, site='scrapeops'):

        logger.info("🛠️ Initializing ScraperConfig...")
        self.use_uc = use_uc
        self.headless = headless
        self.incognito = incognito
        self.use_proxy = use_proxy
        self.site = site

        self.uc_options = uc.ChromeOptions()
        self.chrome_options = ChromeOptions()

        self._driver = None
        self.api_keys = {
            'scrapeops': os.getenv("SCRAPEOPS_API_KEY"),
            'scrapingbee': os.getenv("SCRAPINGBEE_API_KEY"),
            'scraperapi': os.getenv("SCRAPERAPI_API_KEY"),
            'scrapedo': os.getenv("SCRAPEDO_API_KEY"),
        }
        self.proxy = None

        self.user_agents: List[str] = self._load_user_agents()
        
        if not self.user_agents:
            logger.warning("⚠️ No agents found — falling back to default")
            self.user_agents =  [os.getenv("DEFAULT_USER_AGENT", "Mozilla/5.0 (X11; Linux x86_64)")]
        
        self.random_user_agent: str = user_agent or random.choice(self.user_agents)
        logger.info(f"🎭 Using User-Agent: {self.random_user_agent}")

    def get_driver(self, new_driver=False):
        if self._driver is None or new_driver:
            logger.info("🚀 Building new WebDriver instance...")
            self._driver = self._init_driver()
        else:
            logger.info("♻️ Reusing existing WebDriver instance")
        return self._driver

    def _init_driver(self):
        try:
            if self.use_uc:
                logger.info("⚙️ Using undetected_chromedriver (UC)")
                return self._get_uc_driver()
            logger.info("⚙️ Using standard Chrome driver")
            return self._get_normal_driver()
        except Exception as e:
            logger.error(f"❌ Driver launch failed: {e}")
            raise e  


    def _get_uc_driver(self) -> uc.Chrome:
        logger.info("🔒 Applying UC-specific options")
        self._apply_common_options(self.uc_options)
        self.uc_options.add_argument("--disable-blink-features=AutomationControlled")
        
        if self.use_proxy:
            self.proxy = self._get_proxy_url(self.site)
            self.uc_options.add_argument(f"--proxy-server={self.proxy}")
            logger.info(f"🌐 UC Proxy set: {self.proxy}")

        logger.info("🚘 Launching UC Chrome...")
        return uc.Chrome(options=self.uc_options)

    def _get_normal_driver(self):
        logger.info("🔧 Preparing standard Chrome options")
        self._apply_common_options(self.chrome_options)

        if self.use_proxy:
            self.proxy = self._get_proxy_url(self.site)
            logger.info("📡 Using SeleniumWire with proxy")
            seleniumwire_options = {
                "proxy": {
                    "http": self.proxy,
                    "https": self.proxy,
                    "no_proxy": "localhost,127.0.0.1"
                }
            }
            return webdriver.Chrome(
                options=self.chrome_options,
                seleniumwire_options=seleniumwire_options
            )
        logger.info("🚘 Launching standard Chrome...")
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=self.chrome_options
        )


    def _apply_common_options(self, options):
        logger.info("🧰 Applying common Chrome options...")
        if self.headless:
            options.add_argument("--headless=new")
            logger.info("🕶️ Headless mode enabled")
        if self.incognito:
            options.add_argument("--incognito")
            logger.info("👤 Incognito mode enabled")
        if self.proxy and not self.use_proxy:  
            options.add_argument(f"--proxy-server={self.proxy}")
            logger.info(f"🌐 Proxy server set: {self.proxy}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(f"user-agent={self.random_user_agent}")
        logger.info("✅ Common options applied")

    def _load_user_agents(self) -> List[str]:
        logger.info("📁 Loading user agents from core/utils/assets/user_agents.json")
        try:
            base_dir = os.path.dirname(__file__)  # /full/path/to/selenium_utils.py
            file_path = os.path.join(base_dir, "assets", "user_agents.json")
            with open(file_path, "r") as f:
                agents = json.load(f)
                logger.info(f"✅ Loaded {len(agents)} user agents")
                return agents
        except Exception as e:
            logger.error(f"❌ Failed to load user agents: {e}")
            logger.warning("👉 Make sure 'core/utils/assets/user_agents.json' exists and is valid.")
            return []


    def _get_proxy_url(self, site: str) -> Optional[str]:
        logger.info(f"🔧 Getting proxy for site: {site}")
        key = self.api_keys.get(site)
        if not key:
            logger.error(f"❌ Missing API key for proxy site: {site}")
            raise ValueError("Missing API key")

        if site == 'scrapeops':
            return f"http://{key}@proxy.scrapeops.io:5353"
        elif site == 'scrapingbee':
            return f"http://{key}@proxy.scrapingbee.com:8080"
        elif site == 'scraperapi':
            return f"http://scraperapi:{key}@proxy-server.scraperapi.com:8001"
        elif site == 'scrapedo':
            return f"http://{key}@proxy.scrape.do:8080"
        else:
            raise ValueError(f"❌ Invalid proxy provider: {site}")
