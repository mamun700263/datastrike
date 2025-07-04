import os


class CaptchaProvider:
    DOMAIN_MAP = {
        "forcaptcha": "ocr.forcaptcha.com",
        "10captcha": "api.10captcha.io",
        "rapidcaptcha": "rapidcaptcha.tech"
    }

    def __init__(self, name):
        self.name = name
        self.domain = self.DOMAIN_MAP.get(name)

        if not self.domain:
            raise ValueError(f"No domain configured for provider {name}")
        
        self.api_key = os.getenv(f"{name.upper()}_API_KEY")
        if not self.api_key:
            raise ValueError(f"Missing API key for provider {name}")
        
        self.submit_url = self.make_url("in")
        self.poll_url = self.make_url("res")

    def make_url(self, endpoint):
        return f"https://{self.domain}/{endpoint}.php"

    def to_dict(self):
        return {
            "name": self.name,
            "submit_url": self.submit_url,
            "poll_url": self.poll_url,
            "api_key": self.api_key[:2] + "****"  # leak 2 chars max
        }
    
class CaptchaProviderRegistry:
    _registry = {}

    @classmethod
    def get(cls, name: str, logger) -> CaptchaProvider:
        if name not in CaptchaProvider.DOMAIN_MAP:
            logger.debug(...)
            raise ValueError(...)

        if name not in cls._registry:
            cls._registry[name] = CaptchaProvider(name)
            logger.debug(f"Captcha provider: {name} instantiated")

        return cls._registry[name]
