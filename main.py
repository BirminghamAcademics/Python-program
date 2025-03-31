from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class WebBrowser(QMainWindow):
    def __init__(self):
        super(WebBrowser, self).__init__()
        self.setWindowTitle("My Python Web Browser")
        self.setGeometry(100, 100, 800, 600)

        # Create the browser
        self.browser = QWebEngineView()
        self.browser.setUrl("https://www.google.com")

        # Create URL bar and button
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.load_url)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.go_button)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(url)

# Run the application
app = QApplication(sys.argv)
window = WebBrowser()
window.show()
sys.exit(app.exec_())
