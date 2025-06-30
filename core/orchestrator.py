from typing import Type, Optional, Dict, Any, List
from app.scrapers.base_scraper import BaseScraper
from app.dataExporters.api_post import post_data_to_api
from app.dataExporters.file_saver import save_to_file
from app.dataExporters.google_sheet_pusher import push_to_google_sheet


class Orchestrator:
    def __init__(
        self,
        scraper_class: Type[BaseScraper],
        config: Dict[str, Any],
        exporter: Optional[str] = "file",  # file, api, google
        export_config: Optional[Dict[str, Any]] = None,
    ):
        self.scraper = scraper_class(config)
        self.exporter = exporter
        self.export_config = export_config or {}

    def run(self) -> List[Dict[str, Any]]:
        print("🚀 Starting scraping process...")
        data = self.scraper.scrape()

        if not data:
            print("⚠️ No data scraped.")
            return []

        print(f"✅ Scraped {len(data)} items. Exporting via '{self.exporter}'...")
        self._export(data)
        return data

    def _export(self, data: List[Dict[str, Any]]) -> None:
        if self.exporter == "file":
            save_to_file(data, **self.export_config)
        elif self.exporter == "api":
            post_data_to_api(data, **self.export_config)
        elif self.exporter == "google":
            push_to_google_sheet(data, **self.export_config)
        else:
            print(f"❌ Unknown exporter: {self.exporter}")
