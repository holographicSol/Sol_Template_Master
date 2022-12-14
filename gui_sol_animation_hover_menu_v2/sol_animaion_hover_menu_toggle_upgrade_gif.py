"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""
import sys
import time
import win32api
import win32con
from PIL import Image
import win32process
from win32api import GetMonitorInfo, MonitorFromPoint
from PyQt5.QtGui import QIcon, QCursor, QMovie
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QDesktopWidget, QComboBox
from PyQt5.QtCore import Qt, QThread, QSize, QPoint, QCoreApplication, QObject, QTimer, QByteArray, pyqtSignal

print('initializing:')
if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    print('-- AA_EnableHighDpiScaling: True')
elif not hasattr(Qt, 'AA_EnableHighDpiScaling'):
    print('-- AA_EnableHighDpiScaling: False')
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    print('-- AA_UseHighDpiPixmaps: True')
elif not hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    print('-- AA_UseHighDpiPixmaps: False')

priority_classes = [win32process.IDLE_PRIORITY_CLASS,
                    win32process.BELOW_NORMAL_PRIORITY_CLASS,
                    win32process.NORMAL_PRIORITY_CLASS,
                    win32process.ABOVE_NORMAL_PRIORITY_CLASS,
                    win32process.HIGH_PRIORITY_CLASS,
                    win32process.REALTIME_PRIORITY_CLASS]
pid = win32api.GetCurrentProcessId()
print('-- process id:', pid)
handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
win32process.SetPriorityClass(handle, priority_classes[4])
print('-- win32process priority class:', priority_classes[4])

out_of_bounds = False
display_hover_menu = False
hover_menu_timer_engaged = False
user_mouse_activity = False
btn_title_logo_bool = False
glo_obj = []
prev_obj_eve = []
hover_menu_timer_thread = []


class ObjEveFilter(QObject):
    def eventFilter(self, obj, event):
        global glo_obj, prev_obj_eve, out_of_bounds
        obj_eve = obj, event

        # Uncomment This Line To See All Object Events
        # print('-- ObjEveFilter(QObject).eventFilter(self, obj, event):', obj_eve)

        # Filtered Object Events
        if out_of_bounds is False:
            if str(obj_eve[1]).startswith('<PyQt5.QtGui.QEnterEvent') and obj_eve[0] == glo_obj[1]:
                self.unhighlightObject()
            elif str(obj_eve[1]).startswith('<PyQt5.QtGui.QHoverEvent') and obj_eve[0] == glo_obj[2]:
                self.unhighlightObject()
                glo_obj[2].setStyleSheet(
                        """QPushButton{background-color: rgb(255, 0, 0);
                           border:0px solid rgb(0, 0, 0);}"""
                )
            elif str(obj_eve[1]).startswith('<PyQt5.QtGui.QHoverEvent') and obj_eve[0] == glo_obj[3]:
                self.unhighlightObject()
                glo_obj[3].setStyleSheet(
                    """QPushButton{background-color: rgb(0, 0, 255);
                       border:0px solid rgb(0, 0, 0);}"""
                )
        return False

    def unhighlightObject(self):
        glo_obj[1].setStyleSheet(
            """QLabel {background-color: rgb(15, 15, 15);
           border:0px solid rgb(35, 35, 35);}"""
        )
        print('-- ObjEveFilter(QObject).unhighlightObject(self):', glo_obj[1])
        glo_obj[2].setStyleSheet(
            """QPushButton{background-color: rgb(0, 0, 0);
               border:0px solid rgb(0, 0, 0);}"""
        )
        print('-- ObjEveFilter(QObject).unhighlightObject(self):', glo_obj[2])
        glo_obj[3].setStyleSheet(
            """QPushButton{background-color: rgb(0, 0, 0);
               border:0px solid rgb(0, 0, 0);}"""
        )
        print('-- ObjEveFilter(QObject).unhighlightObject(self):', glo_obj[3])


class App(QMainWindow):
    cursorMove = pyqtSignal(object)

    def __init__(self):
        super(App, self).__init__()
        global glo_obj

        self.filter = ObjEveFilter()

        self.setWindowIcon(QIcon('./icon.png'))
        self.title = '{dev gui}'
        print('-- setting self.title as:', self.title)
        self.setWindowTitle(self.title)

        self.prev_width = ()
        self.prev_height = ()
        self.prev_pos_w = ()
        self.prev_pos_h = ()
        self.prev_pos = self.pos()

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        image_f = "./image/giphy.gif"
        img = Image.open(image_f)
        self.width, self.height = img.size
        print('-- image geometry:', self.width, "x", self.height)

        print('-- setting window dimensions:', self.width, self.height + 22)
        self.setFixedSize(self.width, self.height + 22)

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setPalette(p)

        """ Tooltip """
        self.tooltip_style = """QToolTip {background-color: rgb(35, 35, 35);
                                   color: rgb(200, 200, 200);
                                   border-top:0px solid rgb(35, 35, 35);
                                   border-bottom:0px solid rgb(35, 35, 35);
                                   border-right:0px solid rgb(0, 0, 0);
                                   border-left:0px solid rgb(0, 0, 0);}"""
        self.setStyleSheet(self.tooltip_style)

        """ Combobox """
        self.cmb_menu_style = """QComboBox {background-color: rgb(10, 10, 10);
                           color: rgb(200, 200, 200);
                           border-top:2px solid rgb(5, 5, 5);
                           border-bottom:2px solid rgb(5, 5, 5);
                           border-right:2px solid rgb(5, 5, 5);
                           border-left:2px solid rgb(0, 0, 0);}"""

        self.cursorMove.connect(self.handleCursorMove)
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.pollCursor)
        self.timer.start()
        self.cursor = None

        self.btn_title_logo = QPushButton(self)
        self.btn_title_logo.move(0, 0)
        self.btn_title_logo.resize(20, 20)
        self.btn_title_logo.setIcon(QIcon("./icon.ico"))
        self.btn_title_logo.setIconSize(QSize(16, 16))
        self.btn_title_logo.clicked.connect(self.btn_title_logo_function_0)
        self.btn_title_logo.setStyleSheet(
            """QPushButton{background-color: rgb(0, 0, 0);
               border:0px solid rgb(0, 0, 0);}"""
        )
        self.btn_title_logo.installEventFilter(self.filter)
        print('-- created btn_title_logo', self.btn_title_logo)
        glo_obj.append(self.btn_title_logo)  # glo_obj 0

        self.lbl_main_bg = QLabel(self)
        self.lbl_main_bg.move(0, 20)
        self.lbl_main_bg.resize(self.width, self.height)
        self.lbl_main_bg.setStyleSheet(
            """QLabel {background-color: rgb(15, 15, 15);
           border:0px solid rgb(35, 35, 35);}"""
        )
        self.lbl_main_bg.installEventFilter(self.filter)
        print('-- created lbl_main_bg', self.lbl_main_bg)
        glo_obj.append(self.lbl_main_bg)  # glo_obj 1

        self.btn_quit = QPushButton(self)
        self.btn_quit.move((self.width - 20), 0)
        self.btn_quit.resize(20, 20)
        self.btn_quit.setIcon(QIcon("./image/img_close.png"))
        self.btn_quit.setIconSize(QSize(8, 8))
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)
        self.btn_quit.setStyleSheet(
            """QPushButton{background-color: rgb(0, 0, 0);
               border:0px solid rgb(0, 0, 0);}"""
        )
        self.btn_quit.installEventFilter(self.filter)
        print('-- created self.btn_quit', self.btn_quit)
        glo_obj.append(self.btn_quit)  # glo_obj 2

        self.btn_minimize = QPushButton(self)
        self.btn_minimize.move((self.width - 40), 0)
        self.btn_minimize.resize(20, 20)
        self.btn_minimize.setIcon(QIcon("./image/img_minimize.png"))
        self.btn_minimize.setIconSize(QSize(20, 20))
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_minimize.setStyleSheet(
            """QPushButton{background-color: rgb(0, 0, 0);
               border:0px solid rgb(0, 0, 0);}"""
        )
        self.btn_minimize.installEventFilter(self.filter)
        print('-- created self.btn_minimize', self.btn_minimize)
        glo_obj.append(self.btn_minimize)  # glo_obj 3

        self.movie = QMovie(image_f, QByteArray(), self)
        self.movie.installEventFilter(self.filter)
        self.movie_screen = QLabel(self)
        self.movie_screen.installEventFilter(self.filter)
        self.movie_screen.move(0, 22)
        self.movie_screen.resize(self.width, self.height)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()

        self.lbl_hover_menu_bg = QLabel(self)
        self.lbl_hover_menu_bg.move(0, 40)
        self.lbl_hover_menu_bg.resize(45, self.height)
        self.lbl_hover_menu_bg.setStyleSheet(
            """QLabel {background-color: rgba(15, 15, 15, 0%);
           border:0px solid rgb(35, 35, 35);}"""
        )
        self.lbl_hover_menu_bg.installEventFilter(self.filter)
        print('-- created lbl_hover_menu_bg', self.lbl_hover_menu_bg)
        glo_obj.append(self.lbl_hover_menu_bg)  # glo_obj 4

        self.btn_0_hover_menu = QPushButton(self)
        self.btn_0_hover_menu.move(0, 45)
        self.btn_0_hover_menu.resize(40, 40)
        # self.btn_0_hover_menu.setIcon(QIcon("./image/img_minimize.png"))
        # self.btn_0_hover_menu.setIconSize(QSize(40, 40))
        self.btn_0_hover_menu.clicked.connect(self.btn_0_hover_menu_function_0)
        self.btn_0_hover_menu.setStyleSheet(
            """QPushButton{background-color: rgb(0, 0, 0);
               border:0px solid rgb(0, 0, 0);}"""
        )
        self.btn_0_hover_menu.installEventFilter(self.filter)
        print('-- created self.btn_0_hover_menu', self.btn_0_hover_menu)
        self.btn_0_hover_menu.hide()
        glo_obj.append(self.btn_0_hover_menu)  # glo_obj 5

        self.initUI()

    def btn_title_logo_function_0(self):
        print('-- btn_title_logo_: clicked')
        global btn_title_logo_bool
        if btn_title_logo_bool is True:
            btn_title_logo_bool = False
        elif btn_title_logo_bool is False:
            btn_title_logo_bool = True

    def btn_0_hover_menu_function_0(self):
        print('-- btn_0_hover_menu: clicked')

    def initUI(self):
        global hover_menu_timer_thread
        hover_menu_timer_thread = HoverMenuTimerClass(self.lbl_hover_menu_bg)

        print('\ndisplaying application:')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.prev_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.prev_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.prev_pos = event.globalPos()

    def pollCursor(self):
        global user_mouse_activity
        pos = QCursor.pos()
        if pos != self.cursor:
            user_mouse_activity = True
            self.cursor = pos
            self.cursorMove.emit(pos)
            # print(user_mouse_activity)

        elif pos == self.cursor:
            user_mouse_activity = False
            # print(user_mouse_activity)

    def handleCursorMove(self, pos):
        global out_of_bounds
        global display_hover_menu
        global hover_menu_timer_thread
        global hover_menu_timer_engaged
        global glo_obj
        global btn_title_logo_bool
        if pos.x() > self.x() and pos.x() < (self.x() + self.width) and\
                pos.y() < (self.y() + self.height) and pos.y() > self.y() and self.isMinimized() is False:
            # print('-- App(QMainWindow).handleCursorMove(self, pos):', pos)
            out_of_bounds = False

            self.lbl_hover_menu_bg.setStyleSheet(
                """QLabel {background-color: rgba(15, 15, 15, 60%);
               border:0px solid rgb(35, 35, 35);}"""
            )
            glo_obj[5].show()

            if display_hover_menu is False:  # and hover_menu_timer_engaged is False:
                display_hover_menu = True

                hover_menu_timer_thread.start()

        else:
            # time.sleep(2)
            out_of_bounds = True

            glo_obj[1].setStyleSheet(
                """QLabel {background-color: rgb(15, 15, 15);
               border:0px solid rgb(35, 35, 35);}"""
            )
            glo_obj[2].setStyleSheet(
                """QPushButton{background-color: rgb(0, 0, 0);
                   border:0px solid rgb(0, 0, 0);}"""
            )
            glo_obj[3].setStyleSheet(
                """QPushButton{background-color: rgb(0, 0, 0);
                   border:0px solid rgb(0, 0, 0);}"""
            )
            if btn_title_logo_bool is False:
                self.lbl_hover_menu_bg.setStyleSheet(
                    """QLabel {background-color: rgba(15, 15, 15, 0%);
                   border:0px solid rgb(35, 35, 35);}"""
                )
                glo_obj[5].hide()


class HoverMenuTimerClass(QThread):
    def __init__(self, lbl_hover_menu_bg):
        QThread.__init__(self)
        self.lbl_hover_menu_bg = lbl_hover_menu_bg

    def run(self):
        print('-- thread started: HoverMenuTimerClass(QThread).run(self)')
        global display_hover_menu
        global hover_menu_timer_engaged
        global glo_obj
        global user_mouse_activity
        global btn_title_logo_bool

        time.sleep(0.8)
        menu_timeout = 5
        while user_mouse_activity is False and menu_timeout != -1:
            if btn_title_logo_bool is False:
                print('-- user mouse movement inactivity:', menu_timeout)
                menu_timeout -= 1
                time.sleep(1)

                if menu_timeout is 0:

                    print('-- HoverMenuTimerClass(QThread): user_mouse_activity: 5.5 seconds idle')

                    self.lbl_hover_menu_bg.setStyleSheet(
                        """QLabel {background-color: rgba(15, 15, 15, 0%);
                       border:0px solid rgb(35, 35, 35);}"""
                    )
                    glo_obj[5].hide()
                    print('-- HoverMenuTimerClass(QThread).run(self) ~ reset lbl_hover_menu_bg transparency.')

            else:
                time.sleep(1)
        hover_menu_timer_engaged = False
        display_hover_menu = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
