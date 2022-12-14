import os
import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui

tray_icon = []


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):

        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)

        # initiate context menu style
        self.context_menu_style = """QMenu {background-color: rgb(35, 35, 35);
                                   color: rgb(200, 200, 200);
                                   border-top:0px solid rgb(35, 35, 35);
                                   border-bottom:0px solid rgb(35, 35, 35);
                                   border-right:0px solid rgb(0, 0, 0);
                                   border-left:0px solid rgb(0, 0, 0);}"""

        # initiate QMenu and set context menu style
        menu = QtWidgets.QMenu(parent)
        menu.setStyleSheet(self.context_menu_style)

        # initiate context menu items
        menu.addAction("         Sol's System Tray Template")
        menu.addSeparator()
        action_0 = menu.addAction(QtGui.QIcon("./icon.ico"), "Super Function 0")
        action_1 = menu.addAction(QtGui.QIcon("./icon.ico"), "Super Function 1")
        action_2 = menu.addAction(QtGui.QIcon("./icon.ico"), "Super Function 2")
        action_3 = menu.addAction(QtGui.QIcon("./icon.ico"), "Super Function 3")
        action_4 = menu.addAction(QtGui.QIcon("./icon.ico"), "Super Function 4")
        menu.addSeparator()
        exit_action = menu.addAction("Exit")

        # set context menu
        self.setContextMenu(menu)

        # plug context menu items into functions
        action_0.triggered.connect(self.action_function_0)
        action_1.triggered.connect(self.action_function_1)
        action_2.triggered.connect(self.action_function_2)
        action_3.triggered.connect(self.action_function_3)
        action_4.triggered.connect(self.action_function_3)
        exit_action.triggered.connect(self.exit)

    def exit(self):
        QtCore.QCoreApplication.exit()

    def action_function_0(self):
        print('selected: action 0')
        tray_icon.setIcon(QtGui.QIcon('./icon_passed.ico'))
        time.sleep(1)
        tray_icon.setIcon(QtGui.QIcon('./icon.ico'))

    def action_function_1(self):
        global tray_icon
        print('selected: action 1')
        tray_icon.setIcon(QtGui.QIcon('./icon_passed.ico'))
        time.sleep(1)
        tray_icon.setIcon(QtGui.QIcon('./icon.ico'))

    def action_function_2(self):
        print('selected: action 2')
        tray_icon.setIcon(QtGui.QIcon('./icon_passed.ico'))
        time.sleep(1)
        tray_icon.setIcon(QtGui.QIcon('./icon.ico'))

    def action_function_3(self):
        print('selected: action 3')
        tray_icon.setIcon(QtGui.QIcon('./icon_passed.ico'))
        time.sleep(1)
        tray_icon.setIcon(QtGui.QIcon('./icon.ico'))

    def action_function_3(self):
        print('selected: action 4')
        tray_icon.setIcon(QtGui.QIcon('./icon_passed.ico'))
        time.sleep(1)
        tray_icon.setIcon(QtGui.QIcon('./icon.ico'))


def main(image):
    global tray_icon
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon(image), w)
    tray_icon.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    on = 'icon.ico'
    main(on)
