import sys
import webbrowser
import time
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

url = 'http://google.com/'
chrome_path='C:/Users/rachit/PycharmProjects/Website/main.py'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        new_tab = QAction('New Tab', self)
        new_tab.triggered.connect(self.navigate_new_tab)
        navbar.addAction(new_tab)

        lucky = QAction("I'm Feeling Lucky", self)
        lucky.triggered.connect(self.navigate_lucky)
        navbar.addAction(lucky)

        gmail = QAction("Emails", self)
        gmail.triggered.connect(self.navigate_gmail)
        navbar.addAction(gmail)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://example.com'))

    def navigate_new_tab(self):
         self.browser.setUrl(QUrl('http://google.com'))

    def navigate_lucky(self):
         self.browser.setUrl(QUrl('https://www.google.com/doodles'))

    def navigate_gmail(self):
         self.browser.setUrl(QUrl('https://gmail.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Hacker Browser')
QApplication.setWindowIcon(QtGui.QIcon('wallibear.ico'))
window = MainWindow()
app.exec_()