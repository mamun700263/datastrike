import time, random

from core import Logger
logger = Logger.get_logger(__name__,'Utils')

class Humanizer:
    @staticmethod
    def sleep_random(minimum: float = 3, maximum: float = 8) -> None:
        if minimum > maximum:
            minimum, maximum = maximum, minimum

        x = random.uniform(minimum, maximum)
        logger.debug(f"⏱️ Sleeping for {x:.2f} seconds...")
        time.sleep(x)
