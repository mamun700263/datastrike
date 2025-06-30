
import time

import requests
from selenium.webdriver.common.by import By


class CaptchaSolver:
    def __init__(self, driver, logger,captcha):
        self.driver = driver
        self.logger = logger
        self.api_key = captcha.api_key
        self.submit_url = captcha.submit_url
        self.poll_url = captcha.poll_url

    def get_site_info(self):
        site_key = self.driver.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')
        page_url = self.driver.current_url
        self.logger.info(f"🔑 site_key: {site_key}")
        self.logger.info(f"🌐 page_url: {page_url}")
        return site_key, page_url

    def submit_captcha(self, site_key, page_url):
        data = {
            'key': self.api_key,
            'method': 'userrecaptcha',
            'googlekey': site_key,
            'pageurl': page_url,
        }
        self.logger.info(f"📤 Submitting captcha: {data}")
        response = requests.post(self.submit_url, data=data)
        self.logger.info(f"🧾 Response: {response.text}")
        if not response.text.startswith('OK|'):
            raise Exception(f"Captcha submit failed: {response.text}")
        return response.text.split('|')[1]

    def poll_solution(self, captcha_id, max_retries=30, delay=5):
        self.logger.info(f"🕓 Starting polling for ID: {captcha_id}")
        for attempt in range(max_retries):
            url = f'{self.poll_url}?key={self.api_key}&action=get&id={captcha_id}'
            res = requests.get(url)
            self.logger.info(f"[{attempt}] 🔄 Poll response: {res.text}")
            if res.text == 'CAPCHA_NOT_READY':
                time.sleep(delay)
                continue
            if res.text.startswith('OK|'):
                token = res.text.split('|')[1]
                self.logger.info(f"✅ Captcha solved: {token[:30]}...")
                return token
            else:
                raise Exception(f"❌ Error solving captcha: {res.text}")
        raise TimeoutError("Captcha solving timed out")

    def inject_token(self, token):
        script = """
        const textarea = document.querySelector('textarea[name="g-recaptcha-response"]');
        textarea.style.display = 'block';
        textarea.value = arguments[0];
        textarea.dispatchEvent(new Event('change'));
        """
        self.logger.info("💉 Injecting token into textarea")
        self.driver.execute_script(script, token)
