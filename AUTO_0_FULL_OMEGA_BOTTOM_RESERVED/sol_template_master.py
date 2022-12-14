"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""
import os
from superglobals import *
import sol_style as style
import sol_module as sol
import sys
import time
import datetime
import psutil
import subprocess
import win32api
import win32con
import win32gui
import win32process
import win32com.client
from importlib import reload
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QCursor, QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt, QThread, QSize, QPoint, QCoreApplication, QTimer
import sol_loading

# CONFIGURATION 1 - SETUP APPLICATION TEMPLATE BOOLEAN
auto_setup = True  # automatically creates modules that will be imported plugged in and ready to use.
auto_generate = True  # creates objects automatically using values below.
auto_generate_btn = True  # enables automatic button creation. plugged in automatically to automatically createde module.
auto_generate_btn_double = True  # enables automatic button creation at twice the width plus spacing. plugged in automatically to automatically createde module.
auto_generate_lbl = True  # enables automatic label creation.
auto_generate_qle = True  # enables automatic qlineedit creation. plugged in automatically to automatically createde module.
auto_generate_qle_double = True  # enables automatic qlineedit creation at twice the width plus spacing. plugged in automatically to automatically createde module.
auto_generate_tb = True  # enables automatic textboxbrowser creation. plugged in automatically to automatically createde module with automatically created timers.
auto_title_bar_toolbar = True  # enables automatically created title area toolbar.
debug_verbosity_bool = False  # enables verbose output
debug_enable_bool = True  # enables output
pin_to_taskbar = False  # enables application window attatch to taskbar
configuration_override_size = False  # enables app_width_static and app_height_static to be set manually, else application will automatically fit to object geometry

# CONFIGURATION 2 - SETUP APPLICATION TEMPLATE GEOMETRY (if auto_generate is true)
app_width_static, app_height_static = 400, 200  # application window size
main_border_height = 4  # application window border
titlebar_height = 28  # titlebar height
btn_size_titlebar = 24  # title bar object width/height
btnx_gen_max = 84  # maximum number of buttons to create
btnx_row_idx_max = 12  # maximum number of buttons in a row
btnx_position_initialize_x, btnx_position_initialize_y = 0, 0  # set initial button position x/y (can be used to offset position if not 0, 0)
btnx_height = 56  # set button size x/y
btnx_height_Y = btnx_height  # (don't touch)
btnx_sp_height = 8  # set button spacing x/y
btnx_sp_height_Y = btnx_sp_height  # (don't touch)
reserve_btnx = []  # reserve objects for any reason, like a menu.
reserve_btnx_double = [72, 82, 74, 76, 78, 80]  # reserve objects for any reason, like a menu.
reserve_lblx = []  # reserve objects for any reason, like a menu.
reserve_qlex = []  # reserve objects for any reason.
reserve_qlex_double = []  # reserve objects for any reason.
reserve_tbx = []  # reserve objects for any reason.
title_bar_toolbar_max = 12  # max objects in toolbar
title_bar_toolbar_w = 56  # toolbar object width
title_bar_toolbar_h = 24  # toolbar object height
title_bar_toolbar_sp = 8  # toolbar object spacing
title_bar_toolbar_name = ['File', 'Edit', 'Format', 'View', 'Window', 'Help']  # Items in list will be used to automatically create toolbar.
btnx_master = []
btnx_master.append([btnx_gen_max, btnx_row_idx_max, btnx_position_initialize_x, btnx_position_initialize_y, btnx_height, btnx_height_Y, btnx_sp_height, btnx_sp_height_Y])

# initiation
tb_message = []
event_filter_self = []
shell = win32com.client.Dispatch("WScript.Shell")
pid_main = os.getpid()
print(str('[' + str(datetime.datetime.now()) + '] [pid_main]' + str(pid_main)))
print(str('[' + str(datetime.datetime.now()) + '] initializing application'))
program_fname = os.path.basename(__file__)
program_fname_no_suffix = program_fname.replace('.py', '')  # used by auto button generator if write function file is True.
print(str('[' + str(datetime.datetime.now()) + '] [program_fname] ' + str(program_fname)))
cwd = os.getcwd() + '\\'

# subprocess arguments
info = subprocess.STARTUPINFO()  # Subprocess Control
info.dwFlags = 1
info.wShowWindow = 0

bool_switch_run_at_startup = False

def loading_function():
    cmd = 'python ./sol_loading.py'
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=False, startupinfo=info)

loading_function()

def app_activate():
    print(str('[' + str(datetime.datetime.now()) + '] [app_activate] plugged in'))
    shell.AppActivate(pid_main)

def app_display_stays_on_top():
    print(str('[' + str(datetime.datetime.now()) + '] [app_display_stays_on_top] plugged in'))
    event_filter_self[0].setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

def app_display_stays_on_bottom():
    print(str('[' + str(datetime.datetime.now()) + '] [app_display_stays_on_bottom] plugged in'))
    event_filter_self[0].setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint)

def app_display_default():
    print(str('[' + str(datetime.datetime.now()) + '] [app_display_default] plugged in'))
    event_filter_self[0].setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

def create_vbs():
    print(str('[' + str(datetime.datetime.now()) + '] [create_vbs] plugged in'))
    vbs_f = cwd + program_fname_no_suffix + '.vbs'
    exe_f = cwd + program_fname_no_suffix + '.exe'
    open(vbs_f, 'w').close()
    with open(vbs_f, 'a') as fo:
        fo.write('Set WshShell = CreateObject("WScript.Shell")' + '\n')
        fo.write('WshShell.Run chr(34) & "' + exe_f + '" & Chr(34), 0' + '\n')
        fo.write('Set WshShell = Nothing' + '\n')
    fo.close()

def create_lnk():
    print(str('[' + str(datetime.datetime.now()) + '] [create_lnk] plugged in'))
    vbs_f = cwd + program_fname_no_suffix + '.vbs'
    lnk_f = cwd + program_fname_no_suffix + '.lnk'
    open(lnk_f, 'w').close()
    icon = cwd + 'icon.ico'
    shortcut = shell.CreateShortCut(lnk_f)
    shortcut.Targetpath = vbs_f
    shortcut.WorkingDirectory = cwd
    shortcut.IconLocation = icon
    shortcut.save()

def run_at_startup():
    global bool_switch_run_at_startup
    print(str('[' + str(datetime.datetime.now()) + '] [run_at_startup] plugged in'))
    vbs_f = cwd + program_fname_no_suffix + '.vbs'
    shortcut_out = os.path.join(os.path.expanduser('~') + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/' + program_fname_no_suffix + '.lnk')

    # remove shortcut from startup directory
    if bool_switch_run_at_startup is True:
        if os.path.exists(shortcut_out):
            os.remove(shortcut_out)
            bool_switch_run_at_startup = False

    # create shortcut in startup directory
    elif bool_switch_run_at_startup is False:
        icon = cwd + './icon.ico'
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_out)
        shortcut.Targetpath = vbs_f
        shortcut.WorkingDirectory = cwd
        shortcut.IconLocation = icon
        shortcut.save()
        bool_switch_run_at_startup = True

create_vbs()
create_lnk()

# use high dpi scaling and high dpi pixel maps if available
if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    print(str('[' + str(datetime.datetime.now()) + '] AA_EnableHighDpiScaling: True'))
elif not hasattr(Qt, 'AA_EnableHighDpiScaling'):
    print(str('[' + str(datetime.datetime.now()) + '] AA_EnableHighDpiScaling: False'))
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    print(str('[' + str(datetime.datetime.now()) + '] AA_UseHighDpiPixmaps: True'))
elif not hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    print(str('[' + str(datetime.datetime.now()) + '] AA_UseHighDpiPixmaps: False'))

# cursor tracking
cur_pos_x = 0
cur_pos_y = 0
self_pos_x = 0
self_pos_y = 0
app_w = 0
app_h = 0
app_x_range = False
app_y_range = False
app_range_xy = False
titlebar_range_xy = False

# boolean
user_mouse_activity = False
first_load = True

# lists
prev_event = ''
class_0_thread = []
ui_object_complete = []
obj_geo_item = []
obj_icon_geo = []
obj_icon = []
ui_object_font_list_s6b = []
ui_object_font_list_s7b = []
ui_object_font_list_s8b = []
ui_object_font_list_s9b = []
debug_messages = []
btnx_var = []
lblx_var = []
btnx_double_var = []
qlex_var = []
qlex_double_var = []
tbx_var = []
btnx_titlebar_toolbar_var = []
tbx_message = []
tb_timer = []

# integers
avail_w, avail_h = 2, 2
prev_multiplier_w, prev_multiplier_h = 1, 1
pos_w_prev, pos_h_prev = 2, 2


class ObjEveFilter(QObject):
    def eventFilter(self, obj, event):

        global event_filter_self
        global app_range_xy
        global debug_messages, debug_enable_bool, debug_verbosity_bool
        global app_height_static
        global pos_w_prev, pos_h_prev
        global pin_to_taskbar
        
        obj_eve = obj, event

        # verbose level 2
        # print('-- ObjEveFilter(QObject).eventFilter(self, obj, event):', obj_eve)
        # debug_messages.append(str(datetime.datetime.now()) + ' [ObjEveFilter] object:' + str(obj) + ' event: ' + str(event))

        # verbose level 1
        if app_range_xy is True:
            if debug_enable_bool is True:
                if debug_verbosity_bool is True:
                    # print('-- ObjEveFilter(QObject).eventFilter(self, obj, event):', obj_eve)
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter] object:' + str(obj) + ' event: ' + str(event)))

        # scaling geometry
        pos_w = (QDesktopWidget().availableGeometry().width())
        pos_h = (QDesktopWidget().availableGeometry().height())
        if str(obj_eve[1]).startswith('<PyQt5.QtGui.QResizeEvent') or str(obj_eve[1]).startswith(
                '<PyQt5.QtGui.QMoveEvent'):
            self.scaling_geometry_function()

        # taskbar tracking
        if pos_w != pos_w_prev or pos_h != pos_h_prev:
            print(str('[' + str(datetime.datetime.now()) + '] taskbar may have changed position/resized or other event'))
            pos_w_prev = pos_w
            pos_h_prev = pos_h
            
            # set application window geometry
            if pin_to_taskbar is True:
                app_height_pos = int(QDesktopWidget().availableGeometry().height()) - int(app_height_static)
                event_filter_self[0].setGeometry(0, app_height_pos, app_width_static, app_height_static)
            elif pin_to_taskbar is False:
                app_height_pos = int(QDesktopWidget().availableGeometry().height() / 2) - int(app_height_static / 2)
                app_width_pos = int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2)

        return False

    def scaling_geometry_function(self):
        global event_filter_self
        global first_load
        global avail_w, avail_h
        global prev_multiplier_w, prev_multiplier_h
        global ui_object_complete, obj_geo_item, obj_icon_geo, obj_icon
        global ui_object_font_list_s6b, ui_object_font_list_s7b, ui_object_font_list_s8b, ui_object_font_list_s9b
        global debug_messages, debug_enable_bool
        global app_width_static, app_height_static

        # runs once on startup: loads all geometries into separate lists
        if first_load is True:
            first_load = False
            for _ in ui_object_complete:
                obj_geo_width = _.geometry().width()
                obj_geo_height = _.geometry().height()
                obj_geo_pos_w = _.geometry().x()
                obj_geo_pos_h = _.geometry().y()
                var = obj_geo_width, obj_geo_height, obj_geo_pos_w, obj_geo_pos_h
                obj_geo_item.append(var)
                try:
                    obj_icon_geo.append(_.iconSize())
                    obj_icon.append(_)
                except:
                    pass

        # get available geometry
        new_avail_w = QDesktopWidget().availableGeometry().width()
        new_avail_h = QDesktopWidget().availableGeometry().height()

        # obtain a multiplier from the available geometry
        if new_avail_w >= 1000 and new_avail_h >= 1000:
            multiplier_h = int(str(new_avail_h)[0])
        elif new_avail_w < 1000 and new_avail_h < 1000:
            multiplier_h = 1
        else:
            multiplier_h = 1
        multiplier_w = multiplier_h

        # check if multiplier has changed
        if prev_multiplier_w != multiplier_w or prev_multiplier_h != multiplier_h or new_avail_w != avail_w or new_avail_h != avail_h:
            if debug_enable_bool is True:
                if debug_verbosity_bool is True:
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] adjusting application to fit screen geometry'))
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] prev_multiplier_w: ' + str(prev_multiplier_w)))
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] prev_multiplier_h: ' + str(prev_multiplier_h)))

            # set new available geometry
            avail_h = new_avail_h
            avail_w = new_avail_w

            # set new application geometry using multiplier
            app_width = app_width_static * multiplier_w
            app_height = app_height_static * multiplier_h

            if debug_enable_bool is True:
                if debug_verbosity_bool is True:
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new application app_width: ' + str(app_width)))
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new application app_height: ' + str(app_height)))

            # centre application on the screen
            pos_w = (QDesktopWidget().availableGeometry().width())
            pos_h = (QDesktopWidget().availableGeometry().height())

            if debug_enable_bool is True:
                if debug_verbosity_bool is True:
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new application pos_w: ' + str(pos_w)))
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new application pos_h: ' + str(pos_h)))
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] attempting to set application geometry'))

            # set application window geometry
            if pin_to_taskbar is True:
                app_height_pos = int(QDesktopWidget().availableGeometry().height()) - int(app_height_static)
                event_filter_self[0].setGeometry(0, app_height_pos, app_width_static, app_height_static)
            elif pin_to_taskbar is False:
                app_height_pos = int(QDesktopWidget().availableGeometry().height() / 2) - int(app_height_static / 2)
                app_width_pos = int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2)
                event_filter_self[0].setGeometry(app_width_pos, app_height_pos, app_width_static, app_height_static)
                
            if debug_enable_bool is True:
                if debug_verbosity_bool is True:
                    debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] now attempting to set object geometries'))
            
            # set application object geometries
            i = 0
            for _ in ui_object_complete:

                # Default Width
                obj_w = obj_geo_item[i]
                obj_w = obj_w[0]

                # Default Height
                obj_h = obj_geo_item[i]
                obj_h = obj_h[1]

                # Default Position Width
                obj_pos_w = obj_geo_item[i]
                obj_pos_w = obj_pos_w[2]

                # Default Position Height
                obj_pos_h = obj_geo_item[i]
                obj_pos_h = obj_pos_h[3]

                # display last know object geometries
                if debug_enable_bool is True:
                    if debug_verbosity_bool is True:
                        debug_messages.append( \
                            str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] last geometry: ' + \
                                str(_) + ' ' + str(obj_w) + ' ' + str(obj_h) + ' ' + str(obj_pos_w) + ' ' + str(obj_pos_h)))
                
                # set new object geometries using multiplier
                new_obj_w = obj_w * multiplier_w
                new_obj_h = obj_h * multiplier_h
                new_obj_pos_w = obj_pos_w * multiplier_w
                new_obj_pos_h = obj_pos_h * multiplier_h
                if debug_enable_bool is True:
                    if debug_verbosity_bool is True:
                        debug_messages.append( \
                            str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new geometry: ' + \
                                str(_) + ' ' + str(new_obj_w) + ' ' + str(new_obj_h) + ' ' + str(new_obj_pos_w) + ' ' + str(new_obj_pos_h)))

                # move and resize object geometries using new geometries
                _.move(new_obj_pos_w, new_obj_pos_h)
                _.resize(new_obj_w, new_obj_h)
                i += 1

            # set icon geometries
            i = 0
            for _ in obj_icon_geo:
                try:
                    # obtain last known geometries
                    geo_var = str(_)
                    geo_var = geo_var.replace('PyQt5.QtCore.QSize(', '')
                    geo_var = geo_var.replace(')', '')
                    geo_var = geo_var.replace(',', '')
                    geo_var_split = geo_var.split()
                    icon_sz_w = int(geo_var_split[0])
                    icon_sz_h = int(geo_var_split[1])
                    if debug_enable_bool is True:
                        if debug_verbosity_bool is True:
                            debug_messages.append( \
                                str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] original icon_sz_w: ' + str(icon_sz_w) + \
                                    '  original icon_sz_h: ' + str(icon_sz_h)))

                    # set new geometries using multipliers
                    icon_size_w = icon_sz_w * multiplier_w
                    icon_size_h = icon_sz_h * multiplier_h
                    if debug_enable_bool is True:
                        if debug_verbosity_bool is True:
                            debug_messages.append( \
                                str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] [multiply result] new icon_sz_w: ' + str(icon_size_w) + \
                                    '  new icon_sz_h: ' + str(icon_size_h)))
                    obj_icon[i].setIconSize(QSize(icon_size_w, icon_size_h))

                except Exception as e:
                    if debug_enable_bool is True:
                        if debug_verbosity_bool is True:
                            debug_messages.append(str('[' + str(datetime.datetime.now()) + \
                                                      '] [ObjEveFilter.eventFilter] object icon size may be inapplicable: ' + str(_) + ' ' + str(e)))
                i += 1

            # set font geometries using multipliers
            font_size_6b = int(6 * multiplier_h)
            font_size_7b = int(7 * multiplier_h)
            font_size_8b = int(8 * multiplier_h)
            font_size_9b = int(9 * multiplier_h)
            font_s6b = QFont("Segoe UI", (font_size_6b), QFont.Bold)
            font_s7b = QFont("Segoe UI", (font_size_7b), QFont.Bold)
            font_s8b = QFont("Segoe UI", (font_size_8b), QFont.Bold)
            font_s9b = QFont("Segoe UI", (font_size_9b), QFont.Bold)
            for _ in ui_object_font_list_s6b:
                _.setFont(font_s6b)
            for _ in ui_object_font_list_s7b:
                _.setFont(font_s7b)
            for _ in ui_object_font_list_s8b:
                _.setFont(font_s8b)
            for _ in ui_object_font_list_s9b:
                _.setFont(font_s9b)

            # finally change previously known multipliers to current multipliers
            prev_multiplier_w = multiplier_w
            prev_multiplier_h = multiplier_h

            if debug_enable_bool is True:
                debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] ui geometry made it through the blender'))


class App(QMainWindow):
    cursorMove = pyqtSignal(object)

    def __init__(self):
        super(App, self).__init__()
        global btnx_var
        global event_filter_self, ui_object_complete
        global ui_object_font_list_s6b, ui_object_font_list_s7b, ui_object_font_list_s8b, ui_object_font_list_s9b
        global debug_enable_bool, debug_messages
        global app_height_static, app_width_static
        global auto_generate, auto_title_bar_toolbar

        # initiate some basics
        self.setWindowIcon(QIcon(cwd + 'icon.ico'))
        self.title = '{dev gui}'
        self.setWindowTitle(self.title)

        # main window color & window frame style
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setPalette(p)

        # Stylesheet: self
        self.setStyleSheet(style.self_style)

        # initialize fonts
        self.font_s6b = QFont("Segoe UI", 6, QFont.Bold)
        self.font_s7b = QFont("Segoe UI", 7, QFont.Bold)
        self.font_s8b = QFont("Segoe UI", 8, QFont.Bold)
        self.font_s9b = QFont("Segoe UI", 9, QFont.Bold)

        # initiate object event filter
        event_filter_self.append(self)
        self.filter = ObjEveFilter()
        
        # cursor tracking
        self.cursorMove.connect(self.handle_cursor_move)
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.poll_cursor)
        self.timer.start()
        self.cursor = None

        # button: logo (use main_border_height)
        self.btn_title_logo = QPushButton(self)
        self.btn_title_logo.move(main_border_height, main_border_height)
        self.btn_title_logo.resize(btn_size_titlebar, btn_size_titlebar)
        self.btn_title_logo.setIcon(QIcon("./icon.ico"))
        self.btn_title_logo.setIconSize(QSize(titlebar_height, titlebar_height))
        self.btn_title_logo.setStyleSheet(style.btn_title_bar_style)
        self.btn_title_logo.installEventFilter(self)
        ui_object_complete.append(self.btn_title_logo)
        if debug_enable_bool is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.__init__] created btn_title_logo: ' + str(self.btn_title_logo)))

        # button: quit (use main_border_height)
        self.btn_quit = QPushButton(self)
        self.btn_quit.move((app_width_static - (titlebar_height + main_border_height)), main_border_height)
        self.btn_quit.resize(titlebar_height, titlebar_height)
        self.btn_quit.setIcon(QIcon("./resources/image/close.png"))
        self.btn_quit.setIconSize(QSize(btn_size_titlebar, btn_size_titlebar - 4))
        self.btn_quit.setStyleSheet(style.btn_title_bar_style)
        self.btn_quit.installEventFilter(self.filter)
        ui_object_complete.append(self.btn_quit)
        if debug_enable_bool is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.__init__] created self.btn_quit: ' + str(self.btn_quit)))

        # button: minimize (use main_border_height)
        self.btn_minimize = QPushButton(self)
        self.btn_minimize.move((app_width_static - (titlebar_height + main_border_height) * 2), main_border_height)
        self.btn_minimize.resize(btn_size_titlebar, btn_size_titlebar)
        self.btn_minimize.setIcon(QIcon("./resources/image/minimize.png"))
        self.btn_minimize.setIconSize(QSize(24, 16))
        self.btn_minimize.setStyleSheet(style.btn_title_bar_style)
        self.btn_minimize.installEventFilter(self.filter)
        ui_object_complete.append(self.btn_minimize)
        
        if debug_enable_bool is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.__init__] created self.btn_minimize: ' + str(self.btn_minimize)))

        # title_bar_toolbar
        def automatic_title_toolbar_generator():
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] plugged in: automatic_title_toolbar_generator'))
            global btnx_titlebar_toolbar_var

            if auto_setup is True:
                open('./auto_gen_btnx_title_toolbar_functions.py', 'w').close()

                with open('./auto_gen_btnx_title_toolbar_functions.py', 'a') as fo:
                    fo.write('import datetime\n')
                    fo.write('var = []\n\n')
            
            i_x = 0
            while i_x < title_bar_toolbar_max:

                # button intitiation using values from btnx_master
                btnx_name = 'title_toolbar_' + str(i_x)
                self.btnx = btnx_name
                self.btnx = QPushButton(self)
                self.btnx.resize(title_bar_toolbar_w, title_bar_toolbar_h)
                self.btnx.setStyleSheet(style.btnx_style)
                try:
                    self.btnx.setText(title_bar_toolbar_name[i_x])
                except:
                    self.btnx.setText(str(i_x))
                btnx_titlebar_toolbar_var.append(self.btnx)
                ui_object_complete.append(self.btnx)
                self.btnx.installEventFilter(self.filter)

                # automatically position
                if i_x == 0:
                    self.btnx.move( 8, 6 + titlebar_height)
                else:
                    self.btnx.move( 8 + (title_bar_toolbar_w * i_x) + (title_bar_toolbar_sp * i_x), 6 + titlebar_height)

                # automatically create a function and plug
                if auto_setup is True:
                    with open('./auto_gen_btnx_title_toolbar_functions.py', 'a') as fo:
                        fo.write('def ' + btnx_name + '_function():' + '\n')
                        fo.write("    print(str('[' + str(datetime.datetime.now()) + '] clicked: " + btnx_name + "'))\n\n")
                    fo.close()
                i_x += 1
            
            import auto_gen_btnx_title_toolbar_functions
            auto_gen_btnx_title_toolbar_functions.var.append(btnx_titlebar_toolbar_var)
            i = 0
            for _ in btnx_titlebar_toolbar_var:
                btnx_titlebar_toolbar_var[i].clicked.connect(getattr(auto_gen_btnx_title_toolbar_functions, 'title_toolbar_' + str(i) + '_function'))
                i += 1

        # Create objects automatically
        def automatic_object_generator():
            global btnx_var, ui_object_complete, debug_messages, debug_enable_bool, app_width_static, app_height_static, pin_to_taskbar, btnx_master
            global auto_generate_lbl, auto_generate_btn, auto_generate_btn_double, auto_generate_qle
            global btnx_var, lblx_var, btnx_double_var, qlex_var, qlex_double_var, tbx_var, tbx_message, tb_timer
            global reserve_btnx
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] plugged in: generateButtonFunction'))

            """

            INDEX KEY [btnx_master]
            self.btnx_gen_max =                0
            self.btnx_row_idx_max =            1
            self.btnx_position_initialize_x =  2
            self.btnx_position_initialize_y =  3
            self.btnx_height =                 4
            self.btnx_height_Y =               5
            self.btnx_sp_height =              6
            self.btnx_sp_height_Y =            7
            
            """

            # wipe/create automatically generated function and plug files
            if auto_setup is True:
                open('./auto_gen_btnx_function.py', 'w').close()
                with open('./auto_gen_btnx_function.py', 'a') as fo:
                    fo.write('import datetime\n')
                    fo.write('var = []\n\n')
                fo.close()
                
                open('./auto_gen_btnx_double_function.py', 'w').close()
                with open('./auto_gen_btnx_double_function.py', 'a') as fo:
                    fo.write('import datetime\n')
                    fo.write('var = []\n\n')
                fo.close()
                
                open('./auto_gen_qle_returnpressed_connect_function.py', 'w').close()
                with open('./auto_gen_qle_returnpressed_connect_function.py', 'a') as fo:
                    fo.write('import datetime\n')
                    fo.write('var = []\n\n')
                fo.close()

                open('./auto_gen_qle_double_returnpressed_connect_function.py', 'w').close()
                with open('./auto_gen_qle_double_returnpressed_connect_function.py', 'a') as fo:
                    fo.write('import datetime\n')
                    fo.write('var = []\n\n')
                fo.close()
                
                open('./auto_gen_tbx_update_function.py', 'w').close()
                with open('./auto_gen_tbx_update_function.py', 'a') as fo:
                    fo.write('import datetime\n')
                    fo.write('from PyQt5 import QtCore\n')
                    fo.write('var_0 = []\n')
                    fo.write('var_1 = []\n\n')
                fo.close()
                
                open('./auto_gen_tbx_timers.py', 'w').close()

            # step through btnx_master
            layer_count = 0
            i_btnx_master = 0
            for _ in btnx_master:

                # bring in variables from btnx_master
                btnx_gen_max = btnx_master[i_btnx_master][0]
                btnx_row_idx_max = btnx_master[i_btnx_master][1]
                btnx_position_initialize_x, btnx_position_initialize_y = btnx_master[i_btnx_master][2], btnx_master[i_btnx_master][3]
                btnx_height = btnx_master[i_btnx_master][4]
                btnx_height_Y = btnx_master[i_btnx_master][5]
                btnx_sp_height = btnx_master[i_btnx_master][6]
                btnx_sp_height_Y = btnx_master[i_btnx_master][7]

                # automatically generate objects in a loop
                lbl_i = 0
                i = 0
                i_x = 0
                while i_x < btnx_gen_max:

                    # button intitiation using values from btnx_master
                    if auto_generate_btn is True:
                        btnx_name = 'btnx_' + str(i_x)
                        self.btnx = btnx_name
                        self.btnx = QPushButton(self)
                        self.btnx.resize(btnx_height, btnx_height)
                        self.btnx.setStyleSheet(style.btnx_style)
                        self.btnx.setText(btnx_name)
                        btnx_var.append(self.btnx)
                        ui_object_complete.append(self.btnx)
                        self.btnx.installEventFilter(self.filter)
                        self.btnx.hide()

                        # automatically position
                        if i == 0:
                            self.btnx.move( btnx_position_initialize_x + btnx_sp_height + (btnx_sp_height * i ), btnx_position_initialize_y + btnx_height_Y + (btnx_sp_height_Y) )
                        elif i >= 1:
                            self.btnx.move( btnx_position_initialize_x + btnx_sp_height + (btnx_sp_height * i ) + (btnx_height * i), btnx_position_initialize_x + btnx_height_Y + (btnx_sp_height_Y) )

##                        if debug_enable_bool is True:
##                            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.__init__] created: ' + str(self.btnx)))

                        # automatically create a function and plug
                        if auto_setup is True:
                            with open('./auto_gen_btnx_function.py', 'a') as fo:
                                fo.write('def ' + btnx_name + '_function():' + '\n')
                                fo.write("    print(str('[' + str(datetime.datetime.now()) + '] clicked: " + btnx_name + "'))\n\n")
                            fo.close()

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_height)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_height)
                            app_width_static = ((btnx_row_idx_max) * btnx_height)
                            app_width_static = app_width_static + (btnx_row_idx_max * btnx_sp_height) + btnx_sp_height

                    # button double intitiation using values from btnx_master
                    if auto_generate_btn_double is True:
                        btnx_name = 'btnx_double_' + str(i_x)
                        self.btnx = btnx_name
                        self.btnx = QPushButton(self)
                        self.btnx.resize((btnx_height * 2) + btnx_sp_height, btnx_height)
                        self.btnx.setStyleSheet(style.btnx_style)
                        self.btnx.setText(btnx_name)
                        btnx_double_var.append(self.btnx)
                        ui_object_complete.append(self.btnx)
                        self.btnx.installEventFilter(self.filter)
                        self.btnx.hide()

                        # automatically position
                        if i == 0:
                            self.btnx.move( btnx_position_initialize_x + btnx_sp_height + (btnx_sp_height * i ), btnx_position_initialize_y + btnx_height_Y + (btnx_sp_height_Y) )
                        elif i >= 1:
                            self.btnx.move( btnx_position_initialize_x + btnx_sp_height + (btnx_sp_height * i ) + (btnx_height * i), btnx_position_initialize_x + btnx_height_Y + (btnx_sp_height_Y) )

##                        if debug_enable_bool is True:
##                            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.__init__] created: ' + str(self.btnx)))

                        # automatically create a function and plug
                        if auto_setup is True:
                            with open('./auto_gen_btnx_double_function.py', 'a') as fo:
                                fo.write('def ' + btnx_name + '_function():' + '\n')
                                fo.write("    print(str('[' + str(datetime.datetime.now()) + '] clicked: " + btnx_name + "'))\n\n")
                            fo.close()

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_height)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_height)
                            app_width_static = ((btnx_row_idx_max) * btnx_height)
                            app_width_static = app_width_static + (btnx_row_idx_max * btnx_sp_height) + btnx_sp_height
                    
                    # label intitiation using values from btnx_master and multiplied
                    if auto_generate_lbl is True:
                        lblx_name = 'lblx_' + str(i_x)
                        self.lblx = lblx_name
                        self.lblx = QLabel(self)
                        self.lblx.resize((btnx_height * 2) + btnx_sp_height, btnx_height)
                        self.lblx.setStyleSheet(style.lblx_style)
                        self.lblx.setText(lblx_name)
                        lblx_var.append(self.lblx)
                        ui_object_complete.append(self.lblx)
                        self.lblx.installEventFilter(self.filter)
                        self.lblx.hide()

                        # automatically position
                        if i == 0:
                            self.lblx.move( btnx_position_initialize_x + btnx_sp_height + (btnx_sp_height * i ), btnx_position_initialize_y + btnx_height_Y + (btnx_sp_height_Y) )
                        elif i >= 1:
                            self.lblx.move( btnx_position_initialize_x + btnx_sp_height + ((btnx_sp_height*1) * i ) + ((btnx_height*1) * i), btnx_position_initialize_x + btnx_height_Y + (btnx_sp_height_Y) )

##                        if debug_enable_bool is True:
##                            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.__init__] created: ' + str(self.lblx)))

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_height)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_height)
                            app_width_static = ((btnx_row_idx_max) * (btnx_height*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_height*1)) + btnx_sp_height

                    # qlineedit intitiation using values from btnx_master and multiplied  returnPressed.connect
                    if auto_generate_qle is True:
                        qlex_name = 'qlex_' + str(i_x)
                        self.qlex = qlex_name
                        self.qlex = QLineEdit(self)
                        self.qlex.resize(btnx_height, int(btnx_height / 2))
                        self.qlex.setStyleSheet(style.qlex_style)
                        self.qlex.setText(qlex_name)
                        qlex_var.append(self.qlex)
                        ui_object_complete.append(self.qlex)
                        self.qlex.installEventFilter(self.filter)
                        self.qlex.hide()

                        # automatically position button
                        if i == 0:
                            self.qlex.move( btnx_position_initialize_x + btnx_sp_height + (btnx_sp_height * i ), btnx_position_initialize_y + btnx_height_Y + (btnx_sp_height_Y) )
                        elif i >= 1:
                            self.qlex.move( btnx_position_initialize_x + btnx_sp_height + (btnx_sp_height * i ) + (btnx_height * i), btnx_position_initialize_x + btnx_height_Y + (btnx_sp_height_Y) )

                        # automatically create a function and plug
                        if auto_setup is True:
                            with open('./auto_gen_qle_returnpressed_connect_function.py', 'a') as fo:
                                fo.write('def ' + qlex_name + '_returnPressed_connect_function():' + '\n')
                                fo.write("    print(str('[' + str(datetime.datetime.now()) + '] return pressed: " + qlex_name + "'))\n\n")
                            fo.close()

##                        if debug_enable_bool is True:
##                            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.__init__] created: ' + str(self.qlex)))

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_height)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_height)
                            app_width_static = ((btnx_row_idx_max) * (btnx_height*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_height*1)) + btnx_sp_height

                    # qlineedit double intitiation using values from btnx_master and multiplied
                    if auto_generate_qle_double is True:
                        qlex_name = 'qlex_double_' + str(i_x)
                        self.qlex = qlex_name
                        self.qlex = QLineEdit(self)
                        self.qlex.resize((btnx_height * 2) + btnx_sp_height, int(btnx_height / 2))
                        self.qlex.setStyleSheet(style.qlex_style)
                        self.qlex.setText(qlex_name)
                        qlex_double_var.append(self.qlex)
                        ui_object_complete.append(self.qlex)
                        self.qlex.installEventFilter(self.filter)
                        self.qlex.hide()

                        # automatically position qlineedit
                        if i == 0:
                            self.qlex.move( btnx_position_initialize_x + btnx_sp_height + (btnx_sp_height * i ), btnx_position_initialize_y + btnx_height_Y + (btnx_sp_height_Y) )
                        elif i >= 1:
                            self.qlex.move( btnx_position_initialize_x + btnx_sp_height + ((btnx_sp_height*1) * i ) + ((btnx_height*1) * i), btnx_position_initialize_x + btnx_height_Y + (btnx_sp_height_Y) )

                        # automatically create a function and plug
                        if auto_setup is True:
                            with open('./auto_gen_qle_double_returnpressed_connect_function.py', 'a') as fo:
                                fo.write('def ' + qlex_name + '_returnPressed_connect_function():' + '\n')
                                fo.write("    print(str('[' + str(datetime.datetime.now()) + '] return pressed: " + qlex_name + "'))\n\n")
                            fo.close()

##                        if debug_enable_bool is True:
##                            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.__init__] created: ' + str(self.qlex)))

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_height)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_height)
                            app_width_static = ((btnx_row_idx_max) * (btnx_height*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_height*1)) + btnx_sp_height

                    # auto_generate_tb
                    if auto_generate_tb is True:
                        tbx_name = 'tbx_' + str(i_x)
                        self.tbx = tbx_name
                        self.tbx = QTextBrowser(self)
                        self.tbx.resize((btnx_height * 2) + btnx_sp_height, btnx_height)
                        self.tbx.setStyleSheet(style.textbox_stylesheet_default)
                        self.tbx.setText(tbx_name)
                        tbx_var.append(self.tbx)
                        ui_object_complete.append(self.tbx)
                        self.tbx.installEventFilter(self.filter)
                        self.tbx.hide()

                        # automatically position qlineedit
                        if i == 0:
                            self.tbx.move( btnx_position_initialize_x + btnx_sp_height + (btnx_sp_height * i ), btnx_position_initialize_y + btnx_height_Y + (btnx_sp_height_Y) )
                        elif i >= 1:
                            self.tbx.move( btnx_position_initialize_x + btnx_sp_height + ((btnx_sp_height*1) * i ) + ((btnx_height*1) * i), btnx_position_initialize_x + btnx_height_Y + (btnx_sp_height_Y) )

                        # automatically create a function and plug @QtCore.pyqtSlot()
                        if auto_setup is True:
                            with open('./auto_gen_tbx_update_function.py', 'a') as fo:

                                # start timer
                                fo.write('@QtCore.pyqtSlot()' + '\n')
                                fo.write('def ' + tbx_name + '_start_timer_function():' + '\n')
                                fo.write("    global var_1\n")
                                fo.write("    var_1[0][" + str(i_x) + "].start()" + '\n\n')

                                # stop timer
                                fo.write('@QtCore.pyqtSlot()' + '\n')
                                fo.write('def ' + tbx_name + '_stop_timer_function():' + '\n')
                                fo.write("    global var_1\n")
                                fo.write("    var_1[0][" + str(i_x) + "].stop()" + '\n\n')

                                # update tbx
                                fo.write('message_'+str(i_x)+' = []\n')
                                fo.write('@QtCore.pyqtSlot()' + '\n')
                                fo.write('def ' + tbx_name + '_timer_append_function():' + '\n')
                                fo.write("    global message_" + str(i_x) + '\n')
                                fo.write("    global var_0\n")
                                fo.write("    if message_" + str(i_x) + ':' + '\n')
                                fo.write("        var_0[0][" + str(i_x) + "].append(" + "message_" + str(i_x) + '[0])' + '\n')
                                fo.write("        message_"+str(i_x)+".remove(message_" + str(i_x) + '[0])' + '\n\n')
                                
                            fo.close()

                            # plugs
##                            with open('./auto_gen_tbx_timers.py', 'a') as fo:
##                                fo.write('self.' + tbx_name + '_timer = QTimer(self)' + '\n')
##                                fo.write('self.' + tbx_name + '_timer.setInterval(0)' + '\n')
##                                fo.write('self.' + tbx_name + '_timer.timeout.connect(self.'+ tbx_name + '_timer_append_function)' + '\n')
##                                fo.write('#  self.' + tbx_name + '_start_timer_function()' + '\n\n')
##                            fo.close()

                            tbx_name_timer = tbx_name + '_timer'
                            tbx_name_timer = QTimer(self)
                            tbx_name_timer.setInterval(0)
                            tb_timer.append(tbx_name_timer)

##                        if debug_enable_bool is True:
##                            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.__init__] created: ' + str(self.tbx)))

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_height)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_height)
                            app_width_static = ((btnx_row_idx_max) * (btnx_height*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_height*1)) + btnx_sp_height

                    # add one to row index
                    i += 1

                    # adjust height position for objects after reaching row index max
                    if i == btnx_row_idx_max:
                        i = 0
                        layer_count += 1
                        btnx_height_Y = btnx_height_Y + btnx_height
                        btnx_sp_height_Y = btnx_sp_height_Y + btnx_sp_height

                    # add one every time a button is created
                    i_x += 1

                i_btnx_master += 1

            # FINALLY - set application window geometry and position some extras
##            if configuration_override_size is False:

            # attatch to taskbar
            if pin_to_taskbar is True:
                app_height_pos = int(QDesktopWidget().availableGeometry().height()) - int(app_height_static)
                self.setGeometry(0, app_height_pos, app_width_static, app_height_static)

            # position application center screen
            elif pin_to_taskbar is False:
                app_height_pos = int(QDesktopWidget().availableGeometry().height() / 2) - int(app_height_static / 2)
                app_width_pos = int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2)
                self.setGeometry(app_width_pos, app_height_pos, app_width_static, app_height_static)

            # close, minimize
            self.btn_minimize.move((app_width_static - (titlebar_height + main_border_height) * 2), main_border_height)
            self.btn_quit.move((app_width_static - (titlebar_height + main_border_height)), main_border_height)

            if auto_generate_btn is True:
                import auto_gen_btnx_function
                auto_gen_btnx_function.var.append(btnx_var)
                i = 0
                for _ in btnx_var:
                    btnx_var[i].clicked.connect(getattr(auto_gen_btnx_function, 'btnx_' + str(i) + '_function'))
                    i += 1

            if auto_generate_btn_double is True:
                import auto_gen_btnx_double_function
                auto_gen_btnx_double_function.var.append(btnx_double_var)
                i = 0
                for _ in btnx_double_var:
                    btnx_double_var[i].clicked.connect(getattr(auto_gen_btnx_double_function, 'btnx_double_' + str(i) + '_function'))
                    i += 1

            if auto_generate_qle is True:
                import auto_gen_qle_returnpressed_connect_function
                auto_gen_qle_returnpressed_connect_function.var.append(qlex_var)
                i = 0
                for _ in qlex_var:
                    qlex_var[i].returnPressed.connect(getattr(auto_gen_qle_returnpressed_connect_function, 'qlex_' + str(i) + '_returnPressed_connect_function'))
                    i += 1

            if auto_generate_qle_double is True:
                import auto_gen_qle_double_returnpressed_connect_function
                auto_gen_qle_double_returnpressed_connect_function.var.append(qlex_double_var)
                i = 0
                for _ in qlex_double_var:
                    qlex_double_var[i].returnPressed.connect(getattr(auto_gen_qle_double_returnpressed_connect_function, 'qlex_double_' + str(i) + '_returnPressed_connect_function'))
                    i += 1

            # tbx_name_timer.timeout.connect(tbx_0_timer_append_function)
            if auto_generate_tb is True:
                import auto_gen_tbx_update_function
                auto_gen_tbx_update_function.var_0.append(tbx_var)
                auto_gen_tbx_update_function.var_1.append(tb_timer)
                i = 0
                for _ in tb_timer:
                    tb_timer[i].timeout.connect(getattr(auto_gen_tbx_update_function, 'tbx_' + str(i) + '_timer_append_function'))
                    i += 1
                
                # START TIMERS HERE
##                tbx_var[10].show()
##                tbx_var[18].show()
##                auto_gen_tbx_update_function.tbx_10_start_timer_function()
##                auto_gen_tbx_update_function.tbx_18_start_timer_function()
            
        if auto_title_bar_toolbar is True:
            automatic_title_toolbar_generator()
        if auto_generate is True:
            automatic_object_generator()

        # HIDE ALL
        def hide_all_lblx():
            global lblx_var
            for _ in lblx_var:
                _.hide()

        def hide_all_btnx():
            global btnx_var
            for _ in btnx_var:
                _.hide()

        def hide_all_btnx_double():
            global btnx_double_var
            for _ in btnx_double_var:
                _.hide()

        def hide_all_qlex():
            global qlex_var
            for _ in qlex_var:
                _.hide()

        def hide_all_qlex_double():
            global qlex_double_var
            for _ in qlex_double_var:
                _.hide()

        def hide_all_tbx():
            global tbx_var
            for _ in tbx_var:
                _.hide()

        def hide_all_exclude_title():
            hide_all_lblx()
            hide_all_btnx()
            hide_all_btnx_double()
            hide_all_qlex()
            hide_all_qlex_double()
            hide_all_tbx()

        # SHOW ALL
        def show_all_lblx():
            global lblx_var
            for _ in lblx_var:
                _.show()

        def show_all_btnx():
            global btnx_var
            for _ in btnx_var:
                _.show()

        def show_all_btnx_double():
            global btnx_double_var
            for _ in btnx_double_var:
                _.show()

        def show_all_qlex():
            global qlex_var
            for _ in qlex_var:
                _.show()

        def show_all_qlex_double():
            global qlex_double_var
            for _ in qlex_double_var:
                _.show()

        def show_all_tbx():
            global tbx_var
            for _ in tbx_var:
                _.show()

        # SHOW RESERVED
        def show_reserved_btnx():
            global reserve_btnx, btnx_var
            i = 0
            for _ in btnx_var:
                if i in reserve_btnx:
                    _.show()
                i += 1

        def show_reserved_btnx_double():
            global reserve_btnx_double, btnx_double_var
            i = 0
            for _ in btnx_double_var:
                if i in reserve_btnx_double:
                    _.show()
                i += 1

        def show_reserved_lblx():
            global reserve_lblx, lblx_var
            i = 0
            for _ in lblx_var:
                if i in reserve_lblx:
                    _.show()
                i += 1

        def show_reserved_qlex():
            global reserve_qlex, qlex_var
            i = 0
            for _ in qlex_var:
                if i in reserve_qlex:
                    _.show()
                i += 1

        def show_reserved_qlex_double():
            global reserve_qlex_double, qlex_double_var
            i = 0
            for _ in qlex_double_var:
                if i in reserve_qlex_double:
                    _.show()
                i += 1

        def show_reserved_tbx():
            global reserve_tbx, tbx_var
            i = 0
            for _ in tbx_var:
                if i in reserve_tbx:
                    _.show()
                i += 1

        # TITLE BAR - LOGO BUTTON FUNCTION
        def btn_title_logo_function_0():
            global debug_enable_bool, debug_messages
            if debug_enable_bool is True:
                debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.btn_title_logo_function_0] clicked logo button'))

        # ATTATCH TO TASKBAR FUNCTIO
        def attatch_to_taskbar():
            global pin_to_taskbar, pos_w_prev, pos_h_prev, btnx_double_var
            if pin_to_taskbar is False:
                pin_to_taskbar = True
                pos_w_prev = int()
            elif pin_to_taskbar is True:
                pin_to_taskbar = False
                pos_w_prev = int()
        
        # plugin: title bar basics
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_title_logo.clicked.connect(btn_title_logo_function_0)

        if auto_title_bar_toolbar is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [auto_title_bar_toolbar] True'))

        if auto_generate_btn is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [auto_generate_btn] True'))

        if auto_generate_btn_double is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [auto_generate_btn_double] True'))

        if auto_generate_qle is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [auto_generate_qle] True'))

        if auto_generate_qle_double is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [auto_generate_qle_double] True'))

        if auto_generate_tb is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [auto_generate_tb] True'))

        # display reserved buttons (could be main menu button(s))
        show_reserved_btnx_double()

        # install an event filter to self
        self.installEventFilter(self.filter)

        self.debug_timer_0 = QTimer(self)
        self.debug_timer_0.setInterval(0)
        self.debug_timer_0.timeout.connect(self.debug_timer_0_function)
        self.debug_timer_0_start_function()

        self.initUI()

    def initUI(self):
        global debug_enable_bool, debug_messages
        import sol_loading
        sol_loading.loading_bool = False

        if debug_enable_bool is True:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.initUI] displaying application'))
        self.show()

    @QtCore.pyqtSlot()
    def debug_timer_0_start_function(self):
        self.debug_timer_0.start()

    @QtCore.pyqtSlot()
    def debug_timer_0_stop_function(self):
        self.debug_timer_0.stop()

    @QtCore.pyqtSlot()
    def debug_timer_0_function(self):
        global debug_messages
        if debug_messages:
            print(debug_messages[0])
            debug_messages.remove(debug_messages[0])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.prev_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        global pin_to_taskbar, titlebar_range_xy, prev_event
        delta = QPoint(event.globalPos() - self.prev_pos)
        
        if pin_to_taskbar is False:

            # function: move application using cursor tracking
            # if titlebar_range_xy is True:
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.prev_pos = event.globalPos()


    def poll_cursor(self):
        global user_mouse_activity
        pos = QCursor.pos()
        if pos != self.cursor:
            user_mouse_activity = True
            self.cursor = pos
            self.cursorMove.emit(pos)
        elif pos == self.cursor:
            user_mouse_activity = False

    def get_xy_wh(self):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h
        
        # Cursor position xy
        cur_pos_x = int(self.cursor.x())
        cur_pos_y = int(self.cursor.y())

        # Application position xy
        self_pos_x = int(self.x())
        self_pos_y = int(self.y())

        # Application size wh
        app_w = int(app_width_static)
        app_h = int(app_height_static)

    def is_cursor_app_range_xy(self):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h
        
        global app_x_range, app_y_range, app_range_xy

        # get xy wh
        self.get_xy_wh()

        # check x range
        if cur_pos_x > self_pos_x and cur_pos_x < (self_pos_x + app_w):
            app_x_range = True
        else:
            app_x_range = False
            app_range_xy = False
            
        # check y range
        if cur_pos_y > self_pos_y and cur_pos_y < (self_pos_y + app_h):
            app_y_range = True
        else:
            app_x_range = False
            app_range_xy = False
            
        # set app range xy
        if app_x_range is True and app_y_range is True:
            app_range_xy = True
        else:
            app_range_xy = False

    def is_cursor_title_bar_range_xy(self):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h
        global titlebar_range_xy

        self.get_xy_wh()
        titlebar_range_xy = False

        if cur_pos_x > self_pos_x and cur_pos_x < (self_pos_x + app_w):
            if cur_pos_y > self_pos_y and cur_pos_y < (self_pos_y + titlebar_height):
                titlebar_range_xy = True

    def handle_cursor_move(self):
        global app_x_range, app_y_range, app_range_xy

        try:
            if self.isMinimized() is False:
                self.is_cursor_app_range_xy()
                self.is_cursor_title_bar_range_xy()
                
        except Exception as e:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + ']' + str(e)))


class Class0(QThread):
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        print('-- plugged in: Class0')
        time.sleep(5)

        i = 0
        while i < 100000:
            auto_gen_tbx_update_function.message_10.append(str(i))
            auto_gen_tbx_update_function.message_18.append(str(i))
            i += 1

    def stop_thread(self):
        print('-- plugged in: Class0(stop_thread)')
        self.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
