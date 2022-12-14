"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""
import os
import sys
import win32com.client
from win32api import GetSystemMetrics
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QCursor, QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt, QThread, QSize, QPoint, QCoreApplication, QTimer
import time
import datetime

loading_bool = True


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        # Title
        self.title = '{dev loading}'
        self.setWindowTitle('{dev loading}')

        # Screen Metrics
        self.scr_w = GetSystemMetrics(0)  # Native Resolution Width.
        self.scr_h = GetSystemMetrics(1)  # Native Resolution Height.

        # App Metrics
        self.main_width = 400  # Application Window Width.
        self.main_height = 200  # Application Window Height.
        self.win_pos_w = int((self.scr_w / 2) - (self.main_width / 2))  # Centre the Application On The Screen.
        self.win_pos_h = int((self.scr_h / 2) - (self.main_height / 2))  # Centre the Application On The Screen.

        # Set App Geometry
        self.setGeometry(self.win_pos_w, self.win_pos_h, self.main_width, self.main_height)
        self.setFixedSize(self.main_width, self.main_height)

        # Set App Palette
        self.setWindowFlags(Qt.FramelessWindowHint)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

        # Label
        self.background_image = QLabel(self)
        self.background_image.move(0, 0)
        self.background_image.resize(self.main_width, self.main_height)
        # uncomment to add image
        # pixmap = QPixmap('./resources/image/splashscreen.png')
        # self.background_image.setPixmap(pixmap)
        self.background_image.setStyleSheet("""QLabel{background-color: rgb(24, 24, 24);
                color: rgb(0, 255, 0);
                border-top:8px solid rgb(14, 14, 14);
                border-bottom:8px solid rgb(14, 14, 14);
                border-right:8px solid rgb(14, 14, 14);
                border-left:8px solid rgb(14, 14, 14);}""")
        self.background_image.setAlignment(Qt.AlignCenter)
        self.background_image.setText('{dev gui} loading...')
        self.background_image.show()

        self.loading_timer_0 = QTimer(self)
        self.loading_timer_0.setInterval(0)
        self.loading_timer_0.timeout.connect(self.loading_timer_0_function)
        self.loading_timer_0_start_function()

        self.init_ui()

    def init_ui(self):      
        self.show()

    @QtCore.pyqtSlot()
    def loading_timer_0_start_function(self):
        self.loading_timer_0.start()

    @QtCore.pyqtSlot()
    def loading_timer_0_stop_function(self):
        self.loading_timer_0.stop()

    @QtCore.pyqtSlot()
    def loading_timer_0_function(self):
        global loading_bool
        if loading_bool is False:
            stop_loading()
        time.sleep(3)
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
