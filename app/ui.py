from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton,
    QTextEdit, QGroupBox,
    QCheckBox, QComboBox, QHBoxLayout
)
from PyQt6.QtCore import Qt


class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Crawler")
        self.setMinimumSize(950, 650)

        self.setStyleSheet(self.style())

        main = QVBoxLayout()

        # TITLE
        title = QLabel("Smart Data Crawler")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setObjectName("title")

        # URL INPUT
        url_box = QGroupBox("Target URL")
        url_layout = QVBoxLayout()

        self.url = QLineEdit()
        self.url.setPlaceholderText("https://example.com")

        url_layout.addWidget(self.url)
        url_box.setLayout(url_layout)

        # FIELD SELECTION
        field_box = QGroupBox("Fields to Extract")
        field_layout = QHBoxLayout()

        self.title_cb = QCheckBox("Title")
        self.text_cb = QCheckBox("Text")
        self.links_cb = QCheckBox("Links")

        self.title_cb.setChecked(True)
        self.text_cb.setChecked(True)

        field_layout.addWidget(self.title_cb)
        field_layout.addWidget(self.text_cb)
        field_layout.addWidget(self.links_cb)

        field_box.setLayout(field_layout)

        # EXPORT TYPE
        export_box = QGroupBox("Export Format")
        export_layout = QHBoxLayout()

        self.export = QComboBox()
        self.export.addItems(["JSON", "CSV", "SQLITE"])

        export_layout.addWidget(self.export)
        export_box.setLayout(export_layout)

        # BUTTON
        self.btn = QPushButton("🚀 Start Crawling")
        self.btn.setObjectName("btn")

        # OUTPUT
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        main.addWidget(title)
        main.addWidget(url_box)
        main.addWidget(field_box)
        main.addWidget(export_box)
        main.addWidget(self.btn)
        main.addWidget(self.output)

        self.setLayout(main)

    def style(self):
        return """
        QWidget {
            background-color: #0b1220;
            color: #e5e7eb;
            font-size: 13px;
        }

        #title {
            font-size: 22px;
            font-weight: bold;
            color: #38bdf8;
            padding: 10px;
        }

        QGroupBox {
            border: 1px solid #1f2937;
            border-radius: 10px;
            padding: 10px;
        }

        QLineEdit, QTextEdit {
            background-color: #111827;
            border: 1px solid #334155;
            border-radius: 8px;
        }

        QPushButton {
            background-color: #2563eb;
            padding: 10px;
            border-radius: 10px;
        }

        QPushButton:hover {
            background-color: #1d4ed8;
        }
        """