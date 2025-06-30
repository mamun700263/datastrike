
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    TimeoutException
    )
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.utils import CaptchaSolver, Humanizer


class RecaptchaHandler:

    def __init__(self, driver, logger, provider):

        self.driver = driver
        self.provider = provider
        self.logger = logger
        self.solver = CaptchaSolver(
            driver=self.driver,
            captcha=self.provider,
            logger=self.logger
        )

    def load_page(self, url: str):
        self.driver.get(url)

    def trigger_checkbox(self):
        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src, "recaptcha")]'))
        )
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'recaptcha-anchor'))
        ).click()
        self.driver.switch_to.default_content()

    def detect_challenge(self) -> bool:
        Humanizer.sleep_random()
        try:
            challenge_iframe = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src, "bframe")]'))
            )
            self.driver.switch_to.frame(challenge_iframe)
            self.logger.info("⚠️ Challenge triggered.")
            self.driver.switch_to.default_content()
            return True
        except (TimeoutException, NoSuchElementException):
            self.logger.info("✅ No image challenge.")
            return False

    def solve_and_submit(self):
        site_key, page_url = self.solver.get_site_info()
        captcha_id = self.solver.submit_captcha(site_key, page_url)
        token = self.solver.poll_solution(captcha_id)
        self.solver.inject_token(token)
        Humanizer.sleep_random(4,7)

        self.logger.info("🚀 Submitting the form.")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'recaptcha-demo-submit'))
            )
            self.driver.execute_script(
                "arguments[0].click();", 
                self.driver.find_element(By.ID, 'recaptcha-demo-submit')
            )
        except ElementClickInterceptedException:
            self.logger.warning("⚠️ Click intercepted. Retrying after delay.")
            Humanizer.sleep_random(1,2)
            self.driver.execute_script(
                "arguments[0].click();", 
                self.driver.find_element(By.ID, 'recaptcha-demo-submit')
            )

    def run(self, url="https://www.google.com/recaptcha/api2/demo"):
        self.load_page(url)
        self.trigger_checkbox()
        self.detect_challenge()
        self.solve_and_submit()
