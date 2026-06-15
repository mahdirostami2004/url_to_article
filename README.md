# 🚀 Smart Crawler Pro

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modern desktop web crawler built with Python and PyQt6 that allows users to extract structured data from web pages and export it in multiple formats.

---

## 📸 Preview

> *(Add a screenshot here later)*

```
/project_image/screenshot.png
```

---

## ✨ Features

* 🔍 Scrape data from any URL
* 🎯 Field-level extraction:

  * Title
  * Text
  * Links
* 📦 Multiple export formats:

  * JSON
  * CSV
  * SQLite
* ⚡ Multithreaded (responsive UI)
* 🛡️ Scrapeability detection (handles blocked sites)
* 🎨 Clean and modern PyQt6 interface

---

## 🧱 Project Structure

```
smart_crawler_pro/
│
├── app/
│   ├── main.py        # Entry point
│   ├── ui.py          # UI layout
│   ├── worker.py      # Background thread
│
├── core/
│   ├── scraper.py     # HTTP + parsing
│   ├── extractor.py   # Data extraction
│   ├── checker.py     # Site validation
│
├── utils/
│   ├── exporter.py    # Export logic
│   ├── logger.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/mahdirostami2004/url_to_article.git
cd url_to_article
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python3 -m app.main
```

---

## 🧠 How It Works

1. Enter a target URL
2. Select desired fields (title, text, links)
3. Choose export format
4. The crawler:

   * Validates the website
   * Fetches HTML content
   * Parses and extracts data
   * Exports structured output

---

## 📊 Example Output

### JSON

```json
[
  {
    "url": "https://example.com",
    "title": "Example Domain",
    "text": "This domain is for use in illustrative examples...",
    "links": ["https://www.iana.org/domains/example"]
  }
]
```

---

## ⚠️ Limitations

* Some websites block scraping (anti-bot protection)
* No JavaScript rendering (static HTML only)
* No multi-page crawling (single URL only)

---

## 🚀 Roadmap

* [ ] Async crawler (aiohttp)
* [ ] Proxy rotation
* [ ] JavaScript rendering (Playwright)
* [ ] Link-based crawling (multi-depth)
* [ ] Export to Excel
* [ ] Advanced UI (dashboard)

---

## 🧪 Tech Stack

* Python
* PyQt6
* requests
* BeautifulSoup

---

## 👨‍💻 Author

**Mahdi Rostami**
GitHub: https://github.com/mahdirostami2004

---

## 📌 About This Project

This project demonstrates:

* Modular Python architecture
* GUI development with PyQt6
* Multithreading in desktop apps
* Practical web scraping techniques

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐

---

## 📎 Notes

This project is intended for educational and demonstration purposes. Always respect website terms of service when scraping.
