import sys
import time
import os
# from PyQt4.QtWebKit import *

import PyQt5
# from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5 import *
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings

from PyQt5.QtCore import Qt, QUrl, QTimer


# os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")
# os.environ.update({"QT_QPA_PLATFORM_PLUGIN_PATH": "/home/udara/anaconda3/envs/research-headless/lib/python3.8/site-packages/PyQt5/Qt5/plugins/xcbglintegrations/libqxcb-glx-integration.so"})

class Screenshot(QWebView):

    def capture(self, url, output_file):
        self.output_file = output_file
        self.load(QUrl(url))
        self.loadFinished.connect(self.on_loaded)
        # Create hidden view without scrollbars
        self.setAttribute(Qt.WA_DontShowOnScreen)
        self.page().settings().setAttribute(
            QWebSettings.ShowScrollBars, False)
        self.show()

    def on_loaded(self):
        size = self.page().contentsSize().toSize()
        self.resize(size)
        # Wait for resize
        QTimer.singleShot(1000, self.take_screenshot)

    def take_screenshot(self):
        self.grab().save(self.output_file, b'PNG')
        self.app.quit()

app = QApplication(sys.argv)
s = Screenshot()
s.app = app
s.capture('https://www.google.com/search?q=11', 'screenGL2.png')
app.exec_()


s.capture('https://www.google.com/', 'screenGL1.png')
sys.exit(app.exec_())


