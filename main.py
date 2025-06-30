from app.scrapers.amazon_scraper import AmazonScraper
from app.orchestrator import Orchestrator

config = {
    "url": "https://www.amazon.com/s?k=laptop",
    "headers": {"User-Agent": "TAV_DEV_Sniper/1.0"},
}

export_config = {
    "filename": "amazon_laptops.json",
    "format": "json"
}

orchestrator = Orchestrator(
    scraper_class=AmazonScraper,
    config=config,
    exporter="file",  # or "api" / "google"
    export_config=export_config
)

orchestrator.run()


