import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

from app.ui import UI
from app.worker import Worker


class App(UI):
    def __init__(self):
        super().__init__()

        self.btn.clicked.connect(self.start)
        self.worker = None

    def start(self):
        url = self.url.text().strip()

        if not url:
            QMessageBox.critical(self, "Error", "URL required")
            return

        options = {
            "title": self.title_cb.isChecked(),
            "text": self.text_cb.isChecked(),
            "links": self.links_cb.isChecked()
        }

        export_type = self.export.currentText()

        self.btn.setEnabled(False)

        self.worker = Worker(url, options, export_type)

        self.worker.progress.connect(self.output.append)
        self.worker.done.connect(self.done)
        self.worker.error.connect(self.fail)

        self.worker.start()

    def done(self, msg):
        self.btn.setEnabled(True)
        self.output.append("\nDONE\n" + msg)

    def fail(self, msg):
        self.btn.setEnabled(True)
        QMessageBox.critical(self, "Error", msg)
        self.output.append(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())