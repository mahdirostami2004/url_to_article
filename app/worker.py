from PyQt6.QtCore import QThread, pyqtSignal

from core.scraper import fetch_html, parse
from core.extractor import extract_title, extract_text, extract_links
from core.checker import check_scrapeability
from utils.exporter import export_json, export_csv, export_sqlite


class Worker(QThread):
    progress = pyqtSignal(str)
    done = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, url, options, export_type):
        super().__init__()
        self.url = url
        self.options = options
        self.export_type = export_type

    def run(self):
        try:
            report = check_scrapeability(self.url)

            self.progress.emit(
                f"Status: {report['status']} | {report['reason']}"
            )

            if not report["ok"]:
                self.error.emit("Scraping blocked or failed")
                return

            html = fetch_html(self.url)
            soup = parse(html)

            item = {"url": self.url}

            if self.options["title"]:
                item["title"] = extract_title(soup)

            if self.options["text"]:
                item["text"] = extract_text(soup)

            if self.options["links"]:
                item["links"] = extract_links(soup)

            results = [item]

            # EXPORT
            if self.export_type == "JSON":
                export_json(results)
            elif self.export_type == "CSV":
                export_csv(results)
            elif self.export_type == "SQLITE":
                export_sqlite(results)

            self.done.emit(f"Saved as {self.export_type}")

        except Exception as e:
            self.error.emit(str(e))