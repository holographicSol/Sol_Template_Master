import os
import PyQt5
import PyQt5.QtCore
import datetime
import sol_style
import auto_gen_main_page
import auto_gen_btnx_function
import auto_gen_btnx_double_function
import auto_gen_qle_returnpressed_connect_function
import auto_gen_qle_double_returnpressed_connect_function
import auto_gen_tbx_update_function
import auto_gen_btnx_bool
import auto_gen_btnx_double_bool
import auto_gen_qle_bool
import auto_gen_qle_double_bool

var_btnx = []
var_btnx_double = []
var_lblx = []
var_qlex = []
var_qlex_double = []
var_tbx = []
var_tbx_timer = []
var_btnx_double_timer = []
var_btnx_double_timer_sub = []
var_btnx_timer = []
var_btnx_timer_sub = []
var_self = []

@PyQt5.QtCore.pyqtSlot()
def btnx_double_0_start_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_0_stop_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_0_timer_clicked_function():
    print(btnx_double_0_timer_clicked_function)

def btnx_double_0_function():
    auto_gen_main_page.main_page = 0
    if auto_gen_btnx_double_bool.btnx_double_0_bool is True:
        auto_gen_btnx_double_bool.btnx_double_0_bool = False
        # btnx_double_0_stop_timer_function()
    elif auto_gen_btnx_double_bool.btnx_double_0_bool is False:
        auto_gen_btnx_double_bool.btnx_double_0_bool = True
        # btnx_double_0_start_timer_function()
    print('[btnx_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_0_bool) + ']')

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_0_timer_clicked_function():
    print(btnx_double_1_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[1].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[1].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_1_timer_clicked_function():
    print(btnx_double_1_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[2].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[2].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_2_timer_clicked_function():
    print(btnx_double_1_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[3].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[3].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_3_timer_clicked_function():
    print(btnx_double_1_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[4].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[4].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_4_timer_clicked_function():
    print(btnx_double_1_4_timer_clicked_function)

def btnx_double_1_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_1_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_1_0_bool = False
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_0_bool) + ']')
            # btnx_double_1_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_1_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_1_0_bool = True
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_0_bool) + ']')
            # btnx_double_1_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_1_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_1_1_bool = False
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_1_bool) + ']')
            # btnx_double_1_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_1_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_1_1_bool = True
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_1_bool) + ']')
            # btnx_double_1_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_1_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_1_2_bool = False
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_2_bool) + ']')
            # btnx_double_1_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_1_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_1_2_bool = True
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_2_bool) + ']')
            # btnx_double_1_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_1_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_1_3_bool = False
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_3_bool) + ']')
            # btnx_double_1_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_1_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_1_3_bool = True
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_3_bool) + ']')
            # btnx_double_1_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_1_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_1_4_bool = False
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_4_bool) + ']')
            # btnx_double_1_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_1_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_1_4_bool = True
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_4_bool) + ']')
            # btnx_double_1_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[5].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[5].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_0_timer_clicked_function():
    print(btnx_double_2_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[6].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[6].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_1_timer_clicked_function():
    print(btnx_double_2_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[7].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[7].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_2_timer_clicked_function():
    print(btnx_double_2_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[8].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[8].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_3_timer_clicked_function():
    print(btnx_double_2_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[9].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[9].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_4_timer_clicked_function():
    print(btnx_double_2_4_timer_clicked_function)

def btnx_double_2_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_2_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_2_0_bool = False
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_0_bool) + ']')
            # btnx_double_2_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_2_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_2_0_bool = True
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_0_bool) + ']')
            # btnx_double_2_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_2_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_2_1_bool = False
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_1_bool) + ']')
            # btnx_double_2_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_2_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_2_1_bool = True
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_1_bool) + ']')
            # btnx_double_2_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_2_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_2_2_bool = False
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_2_bool) + ']')
            # btnx_double_2_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_2_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_2_2_bool = True
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_2_bool) + ']')
            # btnx_double_2_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_2_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_2_3_bool = False
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_3_bool) + ']')
            # btnx_double_2_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_2_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_2_3_bool = True
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_3_bool) + ']')
            # btnx_double_2_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_2_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_2_4_bool = False
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_4_bool) + ']')
            # btnx_double_2_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_2_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_2_4_bool = True
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_4_bool) + ']')
            # btnx_double_2_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[10].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[10].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_0_timer_clicked_function():
    print(btnx_double_3_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[11].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[11].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_1_timer_clicked_function():
    print(btnx_double_3_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[12].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[12].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_2_timer_clicked_function():
    print(btnx_double_3_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[13].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[13].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_3_timer_clicked_function():
    print(btnx_double_3_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[14].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[14].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_4_timer_clicked_function():
    print(btnx_double_3_4_timer_clicked_function)

def btnx_double_3_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_3_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_3_0_bool = False
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_0_bool) + ']')
            # btnx_double_3_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_3_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_3_0_bool = True
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_0_bool) + ']')
            # btnx_double_3_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_3_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_3_1_bool = False
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_1_bool) + ']')
            # btnx_double_3_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_3_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_3_1_bool = True
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_1_bool) + ']')
            # btnx_double_3_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_3_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_3_2_bool = False
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_2_bool) + ']')
            # btnx_double_3_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_3_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_3_2_bool = True
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_2_bool) + ']')
            # btnx_double_3_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_3_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_3_3_bool = False
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_3_bool) + ']')
            # btnx_double_3_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_3_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_3_3_bool = True
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_3_bool) + ']')
            # btnx_double_3_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_3_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_3_4_bool = False
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_4_bool) + ']')
            # btnx_double_3_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_3_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_3_4_bool = True
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_4_bool) + ']')
            # btnx_double_3_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[15].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[15].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_0_timer_clicked_function():
    print(btnx_double_4_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[16].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[16].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_1_timer_clicked_function():
    print(btnx_double_4_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[17].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[17].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_2_timer_clicked_function():
    print(btnx_double_4_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[18].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[18].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_3_timer_clicked_function():
    print(btnx_double_4_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[19].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[19].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_4_timer_clicked_function():
    print(btnx_double_4_4_timer_clicked_function)

def btnx_double_4_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_4_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_4_0_bool = False
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_0_bool) + ']')
            # btnx_double_4_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_4_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_4_0_bool = True
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_0_bool) + ']')
            # btnx_double_4_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_4_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_4_1_bool = False
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_1_bool) + ']')
            # btnx_double_4_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_4_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_4_1_bool = True
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_1_bool) + ']')
            # btnx_double_4_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_4_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_4_2_bool = False
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_2_bool) + ']')
            # btnx_double_4_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_4_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_4_2_bool = True
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_2_bool) + ']')
            # btnx_double_4_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_4_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_4_3_bool = False
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_3_bool) + ']')
            # btnx_double_4_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_4_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_4_3_bool = True
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_3_bool) + ']')
            # btnx_double_4_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_4_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_4_4_bool = False
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_4_bool) + ']')
            # btnx_double_4_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_4_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_4_4_bool = True
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_4_bool) + ']')
            # btnx_double_4_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[20].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[20].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_0_timer_clicked_function():
    print(btnx_double_5_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[21].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[21].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_1_timer_clicked_function():
    print(btnx_double_5_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[22].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[22].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_2_timer_clicked_function():
    print(btnx_double_5_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[23].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[23].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_3_timer_clicked_function():
    print(btnx_double_5_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[24].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[24].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_4_timer_clicked_function():
    print(btnx_double_5_4_timer_clicked_function)

def btnx_double_5_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_5_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_5_0_bool = False
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_0_bool) + ']')
            # btnx_double_5_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_5_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_5_0_bool = True
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_0_bool) + ']')
            # btnx_double_5_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_5_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_5_1_bool = False
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_1_bool) + ']')
            # btnx_double_5_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_5_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_5_1_bool = True
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_1_bool) + ']')
            # btnx_double_5_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_5_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_5_2_bool = False
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_2_bool) + ']')
            # btnx_double_5_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_5_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_5_2_bool = True
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_2_bool) + ']')
            # btnx_double_5_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_5_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_5_3_bool = False
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_3_bool) + ']')
            # btnx_double_5_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_5_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_5_3_bool = True
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_3_bool) + ']')
            # btnx_double_5_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_5_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_5_4_bool = False
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_4_bool) + ']')
            # btnx_double_5_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_5_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_5_4_bool = True
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_4_bool) + ']')
            # btnx_double_5_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[25].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[25].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_0_timer_clicked_function():
    print(btnx_double_6_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[26].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[26].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_1_timer_clicked_function():
    print(btnx_double_6_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[27].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[27].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_2_timer_clicked_function():
    print(btnx_double_6_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[28].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[28].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_3_timer_clicked_function():
    print(btnx_double_6_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[29].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[29].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_4_timer_clicked_function():
    print(btnx_double_6_4_timer_clicked_function)

def btnx_double_6_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_6_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_6_0_bool = False
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_0_bool) + ']')
            # btnx_double_6_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_6_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_6_0_bool = True
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_0_bool) + ']')
            # btnx_double_6_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_6_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_6_1_bool = False
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_1_bool) + ']')
            # btnx_double_6_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_6_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_6_1_bool = True
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_1_bool) + ']')
            # btnx_double_6_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_6_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_6_2_bool = False
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_2_bool) + ']')
            # btnx_double_6_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_6_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_6_2_bool = True
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_2_bool) + ']')
            # btnx_double_6_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_6_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_6_3_bool = False
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_3_bool) + ']')
            # btnx_double_6_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_6_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_6_3_bool = True
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_3_bool) + ']')
            # btnx_double_6_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_6_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_6_4_bool = False
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_4_bool) + ']')
            # btnx_double_6_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_6_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_6_4_bool = True
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_4_bool) + ']')
            # btnx_double_6_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[30].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[30].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_0_timer_clicked_function():
    print(btnx_double_7_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[31].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[31].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_1_timer_clicked_function():
    print(btnx_double_7_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[32].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[32].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_2_timer_clicked_function():
    print(btnx_double_7_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[33].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[33].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_3_timer_clicked_function():
    print(btnx_double_7_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[34].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[34].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_4_timer_clicked_function():
    print(btnx_double_7_4_timer_clicked_function)

def btnx_double_7_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_7_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_7_0_bool = False
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_0_bool) + ']')
            # btnx_double_7_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_7_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_7_0_bool = True
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_0_bool) + ']')
            # btnx_double_7_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_7_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_7_1_bool = False
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_1_bool) + ']')
            # btnx_double_7_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_7_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_7_1_bool = True
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_1_bool) + ']')
            # btnx_double_7_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_7_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_7_2_bool = False
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_2_bool) + ']')
            # btnx_double_7_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_7_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_7_2_bool = True
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_2_bool) + ']')
            # btnx_double_7_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_7_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_7_3_bool = False
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_3_bool) + ']')
            # btnx_double_7_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_7_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_7_3_bool = True
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_3_bool) + ']')
            # btnx_double_7_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_7_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_7_4_bool = False
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_4_bool) + ']')
            # btnx_double_7_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_7_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_7_4_bool = True
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_4_bool) + ']')
            # btnx_double_7_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[35].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[35].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_0_timer_clicked_function():
    print(btnx_double_8_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[36].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[36].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_1_timer_clicked_function():
    print(btnx_double_8_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[37].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[37].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_2_timer_clicked_function():
    print(btnx_double_8_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[38].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[38].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_3_timer_clicked_function():
    print(btnx_double_8_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[39].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[39].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_4_timer_clicked_function():
    print(btnx_double_8_4_timer_clicked_function)

def btnx_double_8_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_8_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_8_0_bool = False
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_0_bool) + ']')
            # btnx_double_8_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_8_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_8_0_bool = True
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_0_bool) + ']')
            # btnx_double_8_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_8_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_8_1_bool = False
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_1_bool) + ']')
            # btnx_double_8_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_8_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_8_1_bool = True
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_1_bool) + ']')
            # btnx_double_8_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_8_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_8_2_bool = False
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_2_bool) + ']')
            # btnx_double_8_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_8_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_8_2_bool = True
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_2_bool) + ']')
            # btnx_double_8_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_8_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_8_3_bool = False
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_3_bool) + ']')
            # btnx_double_8_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_8_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_8_3_bool = True
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_3_bool) + ']')
            # btnx_double_8_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_8_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_8_4_bool = False
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_4_bool) + ']')
            # btnx_double_8_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_8_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_8_4_bool = True
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_4_bool) + ']')
            # btnx_double_8_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[40].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[40].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_0_timer_clicked_function():
    print(btnx_double_9_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[41].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[41].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_1_timer_clicked_function():
    print(btnx_double_9_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[42].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[42].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_2_timer_clicked_function():
    print(btnx_double_9_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[43].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[43].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_3_timer_clicked_function():
    print(btnx_double_9_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[44].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[44].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_4_timer_clicked_function():
    print(btnx_double_9_4_timer_clicked_function)

def btnx_double_9_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_9_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_9_0_bool = False
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_0_bool) + ']')
            # btnx_double_9_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_9_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_9_0_bool = True
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_0_bool) + ']')
            # btnx_double_9_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_9_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_9_1_bool = False
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_1_bool) + ']')
            # btnx_double_9_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_9_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_9_1_bool = True
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_1_bool) + ']')
            # btnx_double_9_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_9_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_9_2_bool = False
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_2_bool) + ']')
            # btnx_double_9_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_9_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_9_2_bool = True
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_2_bool) + ']')
            # btnx_double_9_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_9_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_9_3_bool = False
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_3_bool) + ']')
            # btnx_double_9_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_9_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_9_3_bool = True
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_3_bool) + ']')
            # btnx_double_9_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_9_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_9_4_bool = False
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_4_bool) + ']')
            # btnx_double_9_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_9_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_9_4_bool = True
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_4_bool) + ']')
            # btnx_double_9_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[45].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[45].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_0_timer_clicked_function():
    print(btnx_double_10_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[46].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[46].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_1_timer_clicked_function():
    print(btnx_double_10_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[47].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[47].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_2_timer_clicked_function():
    print(btnx_double_10_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[48].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[48].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_3_timer_clicked_function():
    print(btnx_double_10_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[49].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[49].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_4_timer_clicked_function():
    print(btnx_double_10_4_timer_clicked_function)

def btnx_double_10_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_10_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_10_0_bool = False
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_0_bool) + ']')
            # btnx_double_10_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_10_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_10_0_bool = True
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_0_bool) + ']')
            # btnx_double_10_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_10_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_10_1_bool = False
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_1_bool) + ']')
            # btnx_double_10_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_10_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_10_1_bool = True
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_1_bool) + ']')
            # btnx_double_10_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_10_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_10_2_bool = False
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_2_bool) + ']')
            # btnx_double_10_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_10_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_10_2_bool = True
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_2_bool) + ']')
            # btnx_double_10_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_10_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_10_3_bool = False
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_3_bool) + ']')
            # btnx_double_10_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_10_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_10_3_bool = True
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_3_bool) + ']')
            # btnx_double_10_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_10_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_10_4_bool = False
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_4_bool) + ']')
            # btnx_double_10_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_10_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_10_4_bool = True
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_4_bool) + ']')
            # btnx_double_10_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[50].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[50].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_0_timer_clicked_function():
    print(btnx_double_11_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[51].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[51].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_1_timer_clicked_function():
    print(btnx_double_11_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[52].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[52].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_2_timer_clicked_function():
    print(btnx_double_11_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[53].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[53].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_3_timer_clicked_function():
    print(btnx_double_11_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[54].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[54].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_4_timer_clicked_function():
    print(btnx_double_11_4_timer_clicked_function)

def btnx_double_11_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_11_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_11_0_bool = False
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_0_bool) + ']')
            # btnx_double_11_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_11_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_11_0_bool = True
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_0_bool) + ']')
            # btnx_double_11_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_11_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_11_1_bool = False
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_1_bool) + ']')
            # btnx_double_11_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_11_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_11_1_bool = True
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_1_bool) + ']')
            # btnx_double_11_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_11_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_11_2_bool = False
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_2_bool) + ']')
            # btnx_double_11_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_11_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_11_2_bool = True
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_2_bool) + ']')
            # btnx_double_11_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_11_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_11_3_bool = False
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_3_bool) + ']')
            # btnx_double_11_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_11_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_11_3_bool = True
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_3_bool) + ']')
            # btnx_double_11_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_11_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_11_4_bool = False
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_4_bool) + ']')
            # btnx_double_11_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_11_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_11_4_bool = True
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_4_bool) + ']')
            # btnx_double_11_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_12_start_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[1].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_12_stop_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[1].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_12_timer_clicked_function():
    print(btnx_double_12_timer_clicked_function)

def btnx_double_12_function():
    auto_gen_main_page.main_page = 1
    if auto_gen_btnx_double_bool.btnx_double_12_bool is True:
        auto_gen_btnx_double_bool.btnx_double_12_bool = False
        # btnx_double_12_stop_timer_function()
    elif auto_gen_btnx_double_bool.btnx_double_12_bool is False:
        auto_gen_btnx_double_bool.btnx_double_12_bool = True
        # btnx_double_12_start_timer_function()
    print('[btnx_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_12_bool) + ']')

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[55].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[55].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_0_timer_clicked_function():
    print(btnx_double_13_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[56].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[56].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_1_timer_clicked_function():
    print(btnx_double_13_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[57].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[57].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_2_timer_clicked_function():
    print(btnx_double_13_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[58].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[58].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_3_timer_clicked_function():
    print(btnx_double_13_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[59].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[59].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_4_timer_clicked_function():
    print(btnx_double_13_4_timer_clicked_function)

def btnx_double_13_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_13_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_13_0_bool = False
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_0_bool) + ']')
            # btnx_double_13_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_13_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_13_0_bool = True
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_0_bool) + ']')
            # btnx_double_13_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_13_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_13_1_bool = False
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_1_bool) + ']')
            # btnx_double_13_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_13_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_13_1_bool = True
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_1_bool) + ']')
            # btnx_double_13_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_13_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_13_2_bool = False
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_2_bool) + ']')
            # btnx_double_13_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_13_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_13_2_bool = True
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_2_bool) + ']')
            # btnx_double_13_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_13_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_13_3_bool = False
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_3_bool) + ']')
            # btnx_double_13_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_13_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_13_3_bool = True
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_3_bool) + ']')
            # btnx_double_13_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_13_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_13_4_bool = False
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_4_bool) + ']')
            # btnx_double_13_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_13_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_13_4_bool = True
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_4_bool) + ']')
            # btnx_double_13_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[60].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[60].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_0_timer_clicked_function():
    print(btnx_double_14_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[61].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[61].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_1_timer_clicked_function():
    print(btnx_double_14_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[62].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[62].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_2_timer_clicked_function():
    print(btnx_double_14_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[63].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[63].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_3_timer_clicked_function():
    print(btnx_double_14_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[64].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[64].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_4_timer_clicked_function():
    print(btnx_double_14_4_timer_clicked_function)

def btnx_double_14_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_14_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_14_0_bool = False
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_0_bool) + ']')
            # btnx_double_14_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_14_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_14_0_bool = True
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_0_bool) + ']')
            # btnx_double_14_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_14_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_14_1_bool = False
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_1_bool) + ']')
            # btnx_double_14_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_14_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_14_1_bool = True
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_1_bool) + ']')
            # btnx_double_14_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_14_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_14_2_bool = False
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_2_bool) + ']')
            # btnx_double_14_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_14_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_14_2_bool = True
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_2_bool) + ']')
            # btnx_double_14_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_14_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_14_3_bool = False
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_3_bool) + ']')
            # btnx_double_14_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_14_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_14_3_bool = True
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_3_bool) + ']')
            # btnx_double_14_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_14_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_14_4_bool = False
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_4_bool) + ']')
            # btnx_double_14_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_14_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_14_4_bool = True
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_4_bool) + ']')
            # btnx_double_14_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[65].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[65].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_0_timer_clicked_function():
    print(btnx_double_15_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[66].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[66].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_1_timer_clicked_function():
    print(btnx_double_15_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[67].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[67].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_2_timer_clicked_function():
    print(btnx_double_15_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[68].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[68].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_3_timer_clicked_function():
    print(btnx_double_15_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[69].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[69].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_4_timer_clicked_function():
    print(btnx_double_15_4_timer_clicked_function)

def btnx_double_15_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_15_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_15_0_bool = False
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_0_bool) + ']')
            # btnx_double_15_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_15_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_15_0_bool = True
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_0_bool) + ']')
            # btnx_double_15_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_15_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_15_1_bool = False
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_1_bool) + ']')
            # btnx_double_15_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_15_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_15_1_bool = True
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_1_bool) + ']')
            # btnx_double_15_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_15_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_15_2_bool = False
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_2_bool) + ']')
            # btnx_double_15_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_15_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_15_2_bool = True
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_2_bool) + ']')
            # btnx_double_15_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_15_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_15_3_bool = False
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_3_bool) + ']')
            # btnx_double_15_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_15_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_15_3_bool = True
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_3_bool) + ']')
            # btnx_double_15_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_15_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_15_4_bool = False
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_4_bool) + ']')
            # btnx_double_15_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_15_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_15_4_bool = True
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_4_bool) + ']')
            # btnx_double_15_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[70].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[70].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_0_timer_clicked_function():
    print(btnx_double_16_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[71].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[71].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_1_timer_clicked_function():
    print(btnx_double_16_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[72].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[72].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_2_timer_clicked_function():
    print(btnx_double_16_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[73].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[73].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_3_timer_clicked_function():
    print(btnx_double_16_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[74].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[74].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_4_timer_clicked_function():
    print(btnx_double_16_4_timer_clicked_function)

def btnx_double_16_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_16_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_16_0_bool = False
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_0_bool) + ']')
            # btnx_double_16_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_16_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_16_0_bool = True
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_0_bool) + ']')
            # btnx_double_16_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_16_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_16_1_bool = False
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_1_bool) + ']')
            # btnx_double_16_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_16_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_16_1_bool = True
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_1_bool) + ']')
            # btnx_double_16_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_16_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_16_2_bool = False
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_2_bool) + ']')
            # btnx_double_16_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_16_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_16_2_bool = True
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_2_bool) + ']')
            # btnx_double_16_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_16_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_16_3_bool = False
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_3_bool) + ']')
            # btnx_double_16_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_16_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_16_3_bool = True
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_3_bool) + ']')
            # btnx_double_16_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_16_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_16_4_bool = False
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_4_bool) + ']')
            # btnx_double_16_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_16_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_16_4_bool = True
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_4_bool) + ']')
            # btnx_double_16_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[75].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[75].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_0_timer_clicked_function():
    print(btnx_double_17_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[76].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[76].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_1_timer_clicked_function():
    print(btnx_double_17_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[77].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[77].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_2_timer_clicked_function():
    print(btnx_double_17_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[78].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[78].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_3_timer_clicked_function():
    print(btnx_double_17_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[79].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[79].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_4_timer_clicked_function():
    print(btnx_double_17_4_timer_clicked_function)

def btnx_double_17_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_17_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_17_0_bool = False
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_0_bool) + ']')
            # btnx_double_17_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_17_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_17_0_bool = True
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_0_bool) + ']')
            # btnx_double_17_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_17_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_17_1_bool = False
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_1_bool) + ']')
            # btnx_double_17_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_17_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_17_1_bool = True
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_1_bool) + ']')
            # btnx_double_17_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_17_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_17_2_bool = False
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_2_bool) + ']')
            # btnx_double_17_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_17_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_17_2_bool = True
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_2_bool) + ']')
            # btnx_double_17_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_17_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_17_3_bool = False
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_3_bool) + ']')
            # btnx_double_17_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_17_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_17_3_bool = True
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_3_bool) + ']')
            # btnx_double_17_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_17_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_17_4_bool = False
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_4_bool) + ']')
            # btnx_double_17_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_17_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_17_4_bool = True
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_4_bool) + ']')
            # btnx_double_17_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[80].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[80].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_0_timer_clicked_function():
    print(btnx_double_18_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[81].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[81].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_1_timer_clicked_function():
    print(btnx_double_18_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[82].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[82].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_2_timer_clicked_function():
    print(btnx_double_18_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[83].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[83].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_3_timer_clicked_function():
    print(btnx_double_18_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[84].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[84].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_4_timer_clicked_function():
    print(btnx_double_18_4_timer_clicked_function)

def btnx_double_18_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_18_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_18_0_bool = False
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_0_bool) + ']')
            # btnx_double_18_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_18_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_18_0_bool = True
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_0_bool) + ']')
            # btnx_double_18_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_18_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_18_1_bool = False
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_1_bool) + ']')
            # btnx_double_18_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_18_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_18_1_bool = True
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_1_bool) + ']')
            # btnx_double_18_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_18_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_18_2_bool = False
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_2_bool) + ']')
            # btnx_double_18_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_18_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_18_2_bool = True
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_2_bool) + ']')
            # btnx_double_18_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_18_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_18_3_bool = False
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_3_bool) + ']')
            # btnx_double_18_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_18_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_18_3_bool = True
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_3_bool) + ']')
            # btnx_double_18_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_18_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_18_4_bool = False
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_4_bool) + ']')
            # btnx_double_18_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_18_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_18_4_bool = True
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_4_bool) + ']')
            # btnx_double_18_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[85].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[85].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_0_timer_clicked_function():
    print(btnx_double_19_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[86].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[86].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_1_timer_clicked_function():
    print(btnx_double_19_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[87].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[87].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_2_timer_clicked_function():
    print(btnx_double_19_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[88].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[88].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_3_timer_clicked_function():
    print(btnx_double_19_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[89].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[89].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_4_timer_clicked_function():
    print(btnx_double_19_4_timer_clicked_function)

def btnx_double_19_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_19_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_19_0_bool = False
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_0_bool) + ']')
            # btnx_double_19_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_19_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_19_0_bool = True
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_0_bool) + ']')
            # btnx_double_19_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_19_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_19_1_bool = False
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_1_bool) + ']')
            # btnx_double_19_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_19_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_19_1_bool = True
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_1_bool) + ']')
            # btnx_double_19_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_19_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_19_2_bool = False
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_2_bool) + ']')
            # btnx_double_19_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_19_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_19_2_bool = True
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_2_bool) + ']')
            # btnx_double_19_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_19_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_19_3_bool = False
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_3_bool) + ']')
            # btnx_double_19_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_19_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_19_3_bool = True
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_3_bool) + ']')
            # btnx_double_19_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_19_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_19_4_bool = False
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_4_bool) + ']')
            # btnx_double_19_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_19_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_19_4_bool = True
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_4_bool) + ']')
            # btnx_double_19_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[90].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[90].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_0_timer_clicked_function():
    print(btnx_double_20_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[91].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[91].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_1_timer_clicked_function():
    print(btnx_double_20_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[92].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[92].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_2_timer_clicked_function():
    print(btnx_double_20_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[93].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[93].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_3_timer_clicked_function():
    print(btnx_double_20_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[94].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[94].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_4_timer_clicked_function():
    print(btnx_double_20_4_timer_clicked_function)

def btnx_double_20_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_20_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_20_0_bool = False
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_0_bool) + ']')
            # btnx_double_20_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_20_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_20_0_bool = True
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_0_bool) + ']')
            # btnx_double_20_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_20_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_20_1_bool = False
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_1_bool) + ']')
            # btnx_double_20_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_20_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_20_1_bool = True
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_1_bool) + ']')
            # btnx_double_20_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_20_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_20_2_bool = False
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_2_bool) + ']')
            # btnx_double_20_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_20_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_20_2_bool = True
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_2_bool) + ']')
            # btnx_double_20_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_20_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_20_3_bool = False
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_3_bool) + ']')
            # btnx_double_20_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_20_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_20_3_bool = True
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_3_bool) + ']')
            # btnx_double_20_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_20_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_20_4_bool = False
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_4_bool) + ']')
            # btnx_double_20_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_20_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_20_4_bool = True
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_4_bool) + ']')
            # btnx_double_20_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[95].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[95].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_0_timer_clicked_function():
    print(btnx_double_21_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[96].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[96].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_1_timer_clicked_function():
    print(btnx_double_21_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[97].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[97].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_2_timer_clicked_function():
    print(btnx_double_21_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[98].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[98].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_3_timer_clicked_function():
    print(btnx_double_21_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[99].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[99].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_4_timer_clicked_function():
    print(btnx_double_21_4_timer_clicked_function)

def btnx_double_21_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_21_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_21_0_bool = False
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_0_bool) + ']')
            # btnx_double_21_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_21_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_21_0_bool = True
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_0_bool) + ']')
            # btnx_double_21_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_21_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_21_1_bool = False
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_1_bool) + ']')
            # btnx_double_21_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_21_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_21_1_bool = True
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_1_bool) + ']')
            # btnx_double_21_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_21_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_21_2_bool = False
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_2_bool) + ']')
            # btnx_double_21_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_21_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_21_2_bool = True
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_2_bool) + ']')
            # btnx_double_21_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_21_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_21_3_bool = False
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_3_bool) + ']')
            # btnx_double_21_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_21_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_21_3_bool = True
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_3_bool) + ']')
            # btnx_double_21_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_21_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_21_4_bool = False
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_4_bool) + ']')
            # btnx_double_21_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_21_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_21_4_bool = True
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_4_bool) + ']')
            # btnx_double_21_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[100].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[100].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_0_timer_clicked_function():
    print(btnx_double_22_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[101].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[101].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_1_timer_clicked_function():
    print(btnx_double_22_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[102].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[102].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_2_timer_clicked_function():
    print(btnx_double_22_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[103].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[103].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_3_timer_clicked_function():
    print(btnx_double_22_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[104].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[104].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_4_timer_clicked_function():
    print(btnx_double_22_4_timer_clicked_function)

def btnx_double_22_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_22_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_22_0_bool = False
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_0_bool) + ']')
            # btnx_double_22_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_22_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_22_0_bool = True
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_0_bool) + ']')
            # btnx_double_22_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_22_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_22_1_bool = False
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_1_bool) + ']')
            # btnx_double_22_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_22_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_22_1_bool = True
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_1_bool) + ']')
            # btnx_double_22_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_22_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_22_2_bool = False
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_2_bool) + ']')
            # btnx_double_22_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_22_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_22_2_bool = True
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_2_bool) + ']')
            # btnx_double_22_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_22_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_22_3_bool = False
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_3_bool) + ']')
            # btnx_double_22_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_22_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_22_3_bool = True
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_3_bool) + ']')
            # btnx_double_22_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_22_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_22_4_bool = False
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_4_bool) + ']')
            # btnx_double_22_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_22_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_22_4_bool = True
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_4_bool) + ']')
            # btnx_double_22_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[105].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[105].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_0_timer_clicked_function():
    print(btnx_double_23_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[106].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[106].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_1_timer_clicked_function():
    print(btnx_double_23_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[107].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[107].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_2_timer_clicked_function():
    print(btnx_double_23_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[108].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[108].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_3_timer_clicked_function():
    print(btnx_double_23_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[109].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[109].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_4_timer_clicked_function():
    print(btnx_double_23_4_timer_clicked_function)

def btnx_double_23_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_23_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_23_0_bool = False
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_0_bool) + ']')
            # btnx_double_23_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_23_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_23_0_bool = True
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_0_bool) + ']')
            # btnx_double_23_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_23_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_23_1_bool = False
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_1_bool) + ']')
            # btnx_double_23_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_23_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_23_1_bool = True
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_1_bool) + ']')
            # btnx_double_23_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_23_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_23_2_bool = False
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_2_bool) + ']')
            # btnx_double_23_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_23_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_23_2_bool = True
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_2_bool) + ']')
            # btnx_double_23_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_23_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_23_3_bool = False
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_3_bool) + ']')
            # btnx_double_23_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_23_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_23_3_bool = True
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_3_bool) + ']')
            # btnx_double_23_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_23_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_23_4_bool = False
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_4_bool) + ']')
            # btnx_double_23_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_23_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_23_4_bool = True
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_4_bool) + ']')
            # btnx_double_23_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_24_start_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[2].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_24_stop_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[2].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_24_timer_clicked_function():
    print(btnx_double_24_timer_clicked_function)

def btnx_double_24_function():
    auto_gen_main_page.main_page = 2
    if auto_gen_btnx_double_bool.btnx_double_24_bool is True:
        auto_gen_btnx_double_bool.btnx_double_24_bool = False
        # btnx_double_24_stop_timer_function()
    elif auto_gen_btnx_double_bool.btnx_double_24_bool is False:
        auto_gen_btnx_double_bool.btnx_double_24_bool = True
        # btnx_double_24_start_timer_function()
    print('[btnx_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_24_bool) + ']')

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[110].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[110].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_0_timer_clicked_function():
    print(btnx_double_25_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[111].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[111].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_1_timer_clicked_function():
    print(btnx_double_25_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[112].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[112].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_2_timer_clicked_function():
    print(btnx_double_25_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[113].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[113].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_3_timer_clicked_function():
    print(btnx_double_25_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[114].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[114].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_4_timer_clicked_function():
    print(btnx_double_25_4_timer_clicked_function)

def btnx_double_25_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_25_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_25_0_bool = False
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_0_bool) + ']')
            # btnx_double_25_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_25_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_25_0_bool = True
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_0_bool) + ']')
            # btnx_double_25_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_25_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_25_1_bool = False
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_1_bool) + ']')
            # btnx_double_25_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_25_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_25_1_bool = True
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_1_bool) + ']')
            # btnx_double_25_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_25_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_25_2_bool = False
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_2_bool) + ']')
            # btnx_double_25_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_25_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_25_2_bool = True
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_2_bool) + ']')
            # btnx_double_25_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_25_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_25_3_bool = False
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_3_bool) + ']')
            # btnx_double_25_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_25_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_25_3_bool = True
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_3_bool) + ']')
            # btnx_double_25_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_25_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_25_4_bool = False
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_4_bool) + ']')
            # btnx_double_25_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_25_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_25_4_bool = True
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_4_bool) + ']')
            # btnx_double_25_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[115].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[115].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_0_timer_clicked_function():
    print(btnx_double_26_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[116].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[116].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_1_timer_clicked_function():
    print(btnx_double_26_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[117].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[117].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_2_timer_clicked_function():
    print(btnx_double_26_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[118].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[118].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_3_timer_clicked_function():
    print(btnx_double_26_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[119].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[119].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_4_timer_clicked_function():
    print(btnx_double_26_4_timer_clicked_function)

def btnx_double_26_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_26_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_26_0_bool = False
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_0_bool) + ']')
            # btnx_double_26_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_26_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_26_0_bool = True
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_0_bool) + ']')
            # btnx_double_26_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_26_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_26_1_bool = False
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_1_bool) + ']')
            # btnx_double_26_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_26_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_26_1_bool = True
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_1_bool) + ']')
            # btnx_double_26_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_26_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_26_2_bool = False
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_2_bool) + ']')
            # btnx_double_26_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_26_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_26_2_bool = True
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_2_bool) + ']')
            # btnx_double_26_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_26_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_26_3_bool = False
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_3_bool) + ']')
            # btnx_double_26_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_26_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_26_3_bool = True
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_3_bool) + ']')
            # btnx_double_26_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_26_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_26_4_bool = False
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_4_bool) + ']')
            # btnx_double_26_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_26_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_26_4_bool = True
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_4_bool) + ']')
            # btnx_double_26_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[120].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[120].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_0_timer_clicked_function():
    print(btnx_double_27_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[121].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[121].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_1_timer_clicked_function():
    print(btnx_double_27_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[122].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[122].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_2_timer_clicked_function():
    print(btnx_double_27_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[123].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[123].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_3_timer_clicked_function():
    print(btnx_double_27_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[124].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[124].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_4_timer_clicked_function():
    print(btnx_double_27_4_timer_clicked_function)

def btnx_double_27_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_27_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_27_0_bool = False
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_0_bool) + ']')
            # btnx_double_27_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_27_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_27_0_bool = True
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_0_bool) + ']')
            # btnx_double_27_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_27_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_27_1_bool = False
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_1_bool) + ']')
            # btnx_double_27_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_27_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_27_1_bool = True
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_1_bool) + ']')
            # btnx_double_27_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_27_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_27_2_bool = False
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_2_bool) + ']')
            # btnx_double_27_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_27_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_27_2_bool = True
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_2_bool) + ']')
            # btnx_double_27_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_27_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_27_3_bool = False
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_3_bool) + ']')
            # btnx_double_27_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_27_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_27_3_bool = True
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_3_bool) + ']')
            # btnx_double_27_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_27_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_27_4_bool = False
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_4_bool) + ']')
            # btnx_double_27_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_27_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_27_4_bool = True
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_4_bool) + ']')
            # btnx_double_27_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[125].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[125].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_0_timer_clicked_function():
    print(btnx_double_28_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[126].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[126].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_1_timer_clicked_function():
    print(btnx_double_28_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[127].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[127].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_2_timer_clicked_function():
    print(btnx_double_28_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[128].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[128].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_3_timer_clicked_function():
    print(btnx_double_28_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[129].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[129].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_4_timer_clicked_function():
    print(btnx_double_28_4_timer_clicked_function)

def btnx_double_28_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_28_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_28_0_bool = False
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_0_bool) + ']')
            # btnx_double_28_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_28_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_28_0_bool = True
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_0_bool) + ']')
            # btnx_double_28_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_28_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_28_1_bool = False
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_1_bool) + ']')
            # btnx_double_28_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_28_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_28_1_bool = True
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_1_bool) + ']')
            # btnx_double_28_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_28_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_28_2_bool = False
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_2_bool) + ']')
            # btnx_double_28_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_28_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_28_2_bool = True
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_2_bool) + ']')
            # btnx_double_28_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_28_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_28_3_bool = False
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_3_bool) + ']')
            # btnx_double_28_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_28_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_28_3_bool = True
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_3_bool) + ']')
            # btnx_double_28_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_28_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_28_4_bool = False
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_4_bool) + ']')
            # btnx_double_28_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_28_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_28_4_bool = True
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_4_bool) + ']')
            # btnx_double_28_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[130].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[130].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_0_timer_clicked_function():
    print(btnx_double_29_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[131].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[131].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_1_timer_clicked_function():
    print(btnx_double_29_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[132].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[132].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_2_timer_clicked_function():
    print(btnx_double_29_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[133].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[133].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_3_timer_clicked_function():
    print(btnx_double_29_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[134].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[134].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_4_timer_clicked_function():
    print(btnx_double_29_4_timer_clicked_function)

def btnx_double_29_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_29_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_29_0_bool = False
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_0_bool) + ']')
            # btnx_double_29_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_29_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_29_0_bool = True
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_0_bool) + ']')
            # btnx_double_29_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_29_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_29_1_bool = False
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_1_bool) + ']')
            # btnx_double_29_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_29_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_29_1_bool = True
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_1_bool) + ']')
            # btnx_double_29_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_29_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_29_2_bool = False
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_2_bool) + ']')
            # btnx_double_29_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_29_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_29_2_bool = True
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_2_bool) + ']')
            # btnx_double_29_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_29_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_29_3_bool = False
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_3_bool) + ']')
            # btnx_double_29_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_29_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_29_3_bool = True
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_3_bool) + ']')
            # btnx_double_29_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_29_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_29_4_bool = False
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_4_bool) + ']')
            # btnx_double_29_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_29_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_29_4_bool = True
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_4_bool) + ']')
            # btnx_double_29_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[135].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[135].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_0_timer_clicked_function():
    print(btnx_double_30_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[136].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[136].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_1_timer_clicked_function():
    print(btnx_double_30_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[137].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[137].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_2_timer_clicked_function():
    print(btnx_double_30_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[138].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[138].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_3_timer_clicked_function():
    print(btnx_double_30_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[139].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[139].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_4_timer_clicked_function():
    print(btnx_double_30_4_timer_clicked_function)

def btnx_double_30_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_30_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_30_0_bool = False
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_0_bool) + ']')
            # btnx_double_30_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_30_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_30_0_bool = True
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_0_bool) + ']')
            # btnx_double_30_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_30_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_30_1_bool = False
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_1_bool) + ']')
            # btnx_double_30_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_30_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_30_1_bool = True
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_1_bool) + ']')
            # btnx_double_30_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_30_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_30_2_bool = False
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_2_bool) + ']')
            # btnx_double_30_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_30_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_30_2_bool = True
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_2_bool) + ']')
            # btnx_double_30_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_30_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_30_3_bool = False
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_3_bool) + ']')
            # btnx_double_30_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_30_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_30_3_bool = True
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_3_bool) + ']')
            # btnx_double_30_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_30_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_30_4_bool = False
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_4_bool) + ']')
            # btnx_double_30_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_30_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_30_4_bool = True
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_4_bool) + ']')
            # btnx_double_30_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[140].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[140].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_0_timer_clicked_function():
    print(btnx_double_31_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[141].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[141].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_1_timer_clicked_function():
    print(btnx_double_31_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[142].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[142].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_2_timer_clicked_function():
    print(btnx_double_31_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[143].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[143].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_3_timer_clicked_function():
    print(btnx_double_31_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[144].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[144].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_4_timer_clicked_function():
    print(btnx_double_31_4_timer_clicked_function)

def btnx_double_31_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_31_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_31_0_bool = False
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_0_bool) + ']')
            # btnx_double_31_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_31_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_31_0_bool = True
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_0_bool) + ']')
            # btnx_double_31_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_31_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_31_1_bool = False
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_1_bool) + ']')
            # btnx_double_31_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_31_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_31_1_bool = True
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_1_bool) + ']')
            # btnx_double_31_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_31_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_31_2_bool = False
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_2_bool) + ']')
            # btnx_double_31_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_31_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_31_2_bool = True
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_2_bool) + ']')
            # btnx_double_31_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_31_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_31_3_bool = False
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_3_bool) + ']')
            # btnx_double_31_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_31_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_31_3_bool = True
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_3_bool) + ']')
            # btnx_double_31_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_31_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_31_4_bool = False
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_4_bool) + ']')
            # btnx_double_31_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_31_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_31_4_bool = True
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_4_bool) + ']')
            # btnx_double_31_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[145].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[145].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_0_timer_clicked_function():
    print(btnx_double_32_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[146].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[146].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_1_timer_clicked_function():
    print(btnx_double_32_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[147].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[147].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_2_timer_clicked_function():
    print(btnx_double_32_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[148].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[148].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_3_timer_clicked_function():
    print(btnx_double_32_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[149].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[149].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_4_timer_clicked_function():
    print(btnx_double_32_4_timer_clicked_function)

def btnx_double_32_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_32_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_32_0_bool = False
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_0_bool) + ']')
            # btnx_double_32_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_32_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_32_0_bool = True
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_0_bool) + ']')
            # btnx_double_32_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_32_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_32_1_bool = False
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_1_bool) + ']')
            # btnx_double_32_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_32_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_32_1_bool = True
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_1_bool) + ']')
            # btnx_double_32_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_32_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_32_2_bool = False
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_2_bool) + ']')
            # btnx_double_32_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_32_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_32_2_bool = True
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_2_bool) + ']')
            # btnx_double_32_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_32_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_32_3_bool = False
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_3_bool) + ']')
            # btnx_double_32_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_32_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_32_3_bool = True
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_3_bool) + ']')
            # btnx_double_32_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_32_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_32_4_bool = False
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_4_bool) + ']')
            # btnx_double_32_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_32_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_32_4_bool = True
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_4_bool) + ']')
            # btnx_double_32_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[150].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[150].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_0_timer_clicked_function():
    print(btnx_double_33_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[151].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[151].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_1_timer_clicked_function():
    print(btnx_double_33_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[152].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[152].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_2_timer_clicked_function():
    print(btnx_double_33_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[153].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[153].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_3_timer_clicked_function():
    print(btnx_double_33_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[154].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[154].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_4_timer_clicked_function():
    print(btnx_double_33_4_timer_clicked_function)

def btnx_double_33_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_33_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_33_0_bool = False
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_0_bool) + ']')
            # btnx_double_33_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_33_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_33_0_bool = True
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_0_bool) + ']')
            # btnx_double_33_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_33_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_33_1_bool = False
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_1_bool) + ']')
            # btnx_double_33_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_33_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_33_1_bool = True
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_1_bool) + ']')
            # btnx_double_33_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_33_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_33_2_bool = False
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_2_bool) + ']')
            # btnx_double_33_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_33_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_33_2_bool = True
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_2_bool) + ']')
            # btnx_double_33_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_33_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_33_3_bool = False
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_3_bool) + ']')
            # btnx_double_33_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_33_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_33_3_bool = True
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_3_bool) + ']')
            # btnx_double_33_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_33_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_33_4_bool = False
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_4_bool) + ']')
            # btnx_double_33_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_33_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_33_4_bool = True
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_4_bool) + ']')
            # btnx_double_33_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[155].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[155].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_0_timer_clicked_function():
    print(btnx_double_34_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[156].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[156].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_1_timer_clicked_function():
    print(btnx_double_34_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[157].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[157].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_2_timer_clicked_function():
    print(btnx_double_34_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[158].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[158].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_3_timer_clicked_function():
    print(btnx_double_34_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[159].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[159].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_4_timer_clicked_function():
    print(btnx_double_34_4_timer_clicked_function)

def btnx_double_34_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_34_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_34_0_bool = False
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_0_bool) + ']')
            # btnx_double_34_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_34_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_34_0_bool = True
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_0_bool) + ']')
            # btnx_double_34_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_34_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_34_1_bool = False
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_1_bool) + ']')
            # btnx_double_34_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_34_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_34_1_bool = True
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_1_bool) + ']')
            # btnx_double_34_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_34_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_34_2_bool = False
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_2_bool) + ']')
            # btnx_double_34_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_34_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_34_2_bool = True
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_2_bool) + ']')
            # btnx_double_34_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_34_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_34_3_bool = False
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_3_bool) + ']')
            # btnx_double_34_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_34_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_34_3_bool = True
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_3_bool) + ']')
            # btnx_double_34_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_34_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_34_4_bool = False
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_4_bool) + ']')
            # btnx_double_34_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_34_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_34_4_bool = True
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_4_bool) + ']')
            # btnx_double_34_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[160].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[160].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_0_timer_clicked_function():
    print(btnx_double_35_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[161].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[161].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_1_timer_clicked_function():
    print(btnx_double_35_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[162].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[162].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_2_timer_clicked_function():
    print(btnx_double_35_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[163].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[163].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_3_timer_clicked_function():
    print(btnx_double_35_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[164].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[164].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_4_timer_clicked_function():
    print(btnx_double_35_4_timer_clicked_function)

def btnx_double_35_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_35_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_35_0_bool = False
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_0_bool) + ']')
            # btnx_double_35_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_35_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_35_0_bool = True
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_0_bool) + ']')
            # btnx_double_35_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_35_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_35_1_bool = False
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_1_bool) + ']')
            # btnx_double_35_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_35_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_35_1_bool = True
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_1_bool) + ']')
            # btnx_double_35_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_35_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_35_2_bool = False
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_2_bool) + ']')
            # btnx_double_35_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_35_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_35_2_bool = True
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_2_bool) + ']')
            # btnx_double_35_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_35_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_35_3_bool = False
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_3_bool) + ']')
            # btnx_double_35_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_35_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_35_3_bool = True
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_3_bool) + ']')
            # btnx_double_35_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_35_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_35_4_bool = False
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_4_bool) + ']')
            # btnx_double_35_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_35_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_35_4_bool = True
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_4_bool) + ']')
            # btnx_double_35_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_36_start_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[3].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_36_stop_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[3].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_36_timer_clicked_function():
    print(btnx_double_36_timer_clicked_function)

def btnx_double_36_function():
    auto_gen_main_page.main_page = 3
    if auto_gen_btnx_double_bool.btnx_double_36_bool is True:
        auto_gen_btnx_double_bool.btnx_double_36_bool = False
        # btnx_double_36_stop_timer_function()
    elif auto_gen_btnx_double_bool.btnx_double_36_bool is False:
        auto_gen_btnx_double_bool.btnx_double_36_bool = True
        # btnx_double_36_start_timer_function()
    print('[btnx_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_36_bool) + ']')

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[165].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[165].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_0_timer_clicked_function():
    print(btnx_double_37_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[166].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[166].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_1_timer_clicked_function():
    print(btnx_double_37_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[167].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[167].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_2_timer_clicked_function():
    print(btnx_double_37_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[168].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[168].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_3_timer_clicked_function():
    print(btnx_double_37_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[169].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[169].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_4_timer_clicked_function():
    print(btnx_double_37_4_timer_clicked_function)

def btnx_double_37_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_37_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_37_0_bool = False
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_0_bool) + ']')
            # btnx_double_37_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_37_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_37_0_bool = True
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_0_bool) + ']')
            # btnx_double_37_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_37_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_37_1_bool = False
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_1_bool) + ']')
            # btnx_double_37_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_37_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_37_1_bool = True
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_1_bool) + ']')
            # btnx_double_37_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_37_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_37_2_bool = False
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_2_bool) + ']')
            # btnx_double_37_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_37_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_37_2_bool = True
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_2_bool) + ']')
            # btnx_double_37_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_37_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_37_3_bool = False
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_3_bool) + ']')
            # btnx_double_37_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_37_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_37_3_bool = True
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_3_bool) + ']')
            # btnx_double_37_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_37_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_37_4_bool = False
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_4_bool) + ']')
            # btnx_double_37_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_37_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_37_4_bool = True
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_4_bool) + ']')
            # btnx_double_37_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[170].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[170].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_0_timer_clicked_function():
    print(btnx_double_38_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[171].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[171].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_1_timer_clicked_function():
    print(btnx_double_38_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[172].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[172].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_2_timer_clicked_function():
    print(btnx_double_38_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[173].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[173].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_3_timer_clicked_function():
    print(btnx_double_38_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[174].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[174].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_4_timer_clicked_function():
    print(btnx_double_38_4_timer_clicked_function)

def btnx_double_38_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_38_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_38_0_bool = False
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_0_bool) + ']')
            # btnx_double_38_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_38_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_38_0_bool = True
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_0_bool) + ']')
            # btnx_double_38_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_38_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_38_1_bool = False
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_1_bool) + ']')
            # btnx_double_38_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_38_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_38_1_bool = True
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_1_bool) + ']')
            # btnx_double_38_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_38_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_38_2_bool = False
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_2_bool) + ']')
            # btnx_double_38_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_38_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_38_2_bool = True
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_2_bool) + ']')
            # btnx_double_38_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_38_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_38_3_bool = False
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_3_bool) + ']')
            # btnx_double_38_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_38_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_38_3_bool = True
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_3_bool) + ']')
            # btnx_double_38_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_38_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_38_4_bool = False
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_4_bool) + ']')
            # btnx_double_38_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_38_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_38_4_bool = True
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_4_bool) + ']')
            # btnx_double_38_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[175].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[175].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_0_timer_clicked_function():
    print(btnx_double_39_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[176].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[176].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_1_timer_clicked_function():
    print(btnx_double_39_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[177].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[177].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_2_timer_clicked_function():
    print(btnx_double_39_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[178].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[178].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_3_timer_clicked_function():
    print(btnx_double_39_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[179].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[179].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_4_timer_clicked_function():
    print(btnx_double_39_4_timer_clicked_function)

def btnx_double_39_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_39_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_39_0_bool = False
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_0_bool) + ']')
            # btnx_double_39_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_39_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_39_0_bool = True
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_0_bool) + ']')
            # btnx_double_39_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_39_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_39_1_bool = False
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_1_bool) + ']')
            # btnx_double_39_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_39_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_39_1_bool = True
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_1_bool) + ']')
            # btnx_double_39_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_39_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_39_2_bool = False
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_2_bool) + ']')
            # btnx_double_39_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_39_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_39_2_bool = True
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_2_bool) + ']')
            # btnx_double_39_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_39_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_39_3_bool = False
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_3_bool) + ']')
            # btnx_double_39_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_39_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_39_3_bool = True
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_3_bool) + ']')
            # btnx_double_39_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_39_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_39_4_bool = False
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_4_bool) + ']')
            # btnx_double_39_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_39_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_39_4_bool = True
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_4_bool) + ']')
            # btnx_double_39_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[180].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[180].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_0_timer_clicked_function():
    print(btnx_double_40_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[181].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[181].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_1_timer_clicked_function():
    print(btnx_double_40_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[182].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[182].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_2_timer_clicked_function():
    print(btnx_double_40_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[183].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[183].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_3_timer_clicked_function():
    print(btnx_double_40_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[184].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[184].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_4_timer_clicked_function():
    print(btnx_double_40_4_timer_clicked_function)

def btnx_double_40_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_40_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_40_0_bool = False
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_0_bool) + ']')
            # btnx_double_40_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_40_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_40_0_bool = True
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_0_bool) + ']')
            # btnx_double_40_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_40_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_40_1_bool = False
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_1_bool) + ']')
            # btnx_double_40_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_40_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_40_1_bool = True
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_1_bool) + ']')
            # btnx_double_40_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_40_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_40_2_bool = False
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_2_bool) + ']')
            # btnx_double_40_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_40_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_40_2_bool = True
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_2_bool) + ']')
            # btnx_double_40_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_40_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_40_3_bool = False
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_3_bool) + ']')
            # btnx_double_40_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_40_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_40_3_bool = True
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_3_bool) + ']')
            # btnx_double_40_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_40_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_40_4_bool = False
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_4_bool) + ']')
            # btnx_double_40_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_40_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_40_4_bool = True
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_4_bool) + ']')
            # btnx_double_40_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[185].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[185].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_0_timer_clicked_function():
    print(btnx_double_41_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[186].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[186].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_1_timer_clicked_function():
    print(btnx_double_41_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[187].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[187].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_2_timer_clicked_function():
    print(btnx_double_41_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[188].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[188].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_3_timer_clicked_function():
    print(btnx_double_41_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[189].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[189].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_4_timer_clicked_function():
    print(btnx_double_41_4_timer_clicked_function)

def btnx_double_41_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_41_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_41_0_bool = False
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_0_bool) + ']')
            # btnx_double_41_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_41_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_41_0_bool = True
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_0_bool) + ']')
            # btnx_double_41_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_41_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_41_1_bool = False
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_1_bool) + ']')
            # btnx_double_41_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_41_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_41_1_bool = True
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_1_bool) + ']')
            # btnx_double_41_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_41_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_41_2_bool = False
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_2_bool) + ']')
            # btnx_double_41_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_41_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_41_2_bool = True
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_2_bool) + ']')
            # btnx_double_41_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_41_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_41_3_bool = False
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_3_bool) + ']')
            # btnx_double_41_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_41_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_41_3_bool = True
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_3_bool) + ']')
            # btnx_double_41_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_41_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_41_4_bool = False
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_4_bool) + ']')
            # btnx_double_41_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_41_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_41_4_bool = True
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_4_bool) + ']')
            # btnx_double_41_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[190].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[190].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_0_timer_clicked_function():
    print(btnx_double_42_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[191].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[191].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_1_timer_clicked_function():
    print(btnx_double_42_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[192].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[192].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_2_timer_clicked_function():
    print(btnx_double_42_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[193].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[193].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_3_timer_clicked_function():
    print(btnx_double_42_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[194].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[194].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_4_timer_clicked_function():
    print(btnx_double_42_4_timer_clicked_function)

def btnx_double_42_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_42_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_42_0_bool = False
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_0_bool) + ']')
            # btnx_double_42_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_42_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_42_0_bool = True
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_0_bool) + ']')
            # btnx_double_42_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_42_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_42_1_bool = False
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_1_bool) + ']')
            # btnx_double_42_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_42_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_42_1_bool = True
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_1_bool) + ']')
            # btnx_double_42_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_42_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_42_2_bool = False
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_2_bool) + ']')
            # btnx_double_42_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_42_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_42_2_bool = True
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_2_bool) + ']')
            # btnx_double_42_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_42_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_42_3_bool = False
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_3_bool) + ']')
            # btnx_double_42_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_42_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_42_3_bool = True
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_3_bool) + ']')
            # btnx_double_42_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_42_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_42_4_bool = False
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_4_bool) + ']')
            # btnx_double_42_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_42_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_42_4_bool = True
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_4_bool) + ']')
            # btnx_double_42_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[195].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[195].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_0_timer_clicked_function():
    print(btnx_double_43_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[196].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[196].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_1_timer_clicked_function():
    print(btnx_double_43_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[197].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[197].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_2_timer_clicked_function():
    print(btnx_double_43_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[198].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[198].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_3_timer_clicked_function():
    print(btnx_double_43_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[199].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[199].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_4_timer_clicked_function():
    print(btnx_double_43_4_timer_clicked_function)

def btnx_double_43_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_43_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_43_0_bool = False
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_0_bool) + ']')
            # btnx_double_43_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_43_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_43_0_bool = True
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_0_bool) + ']')
            # btnx_double_43_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_43_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_43_1_bool = False
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_1_bool) + ']')
            # btnx_double_43_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_43_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_43_1_bool = True
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_1_bool) + ']')
            # btnx_double_43_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_43_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_43_2_bool = False
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_2_bool) + ']')
            # btnx_double_43_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_43_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_43_2_bool = True
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_2_bool) + ']')
            # btnx_double_43_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_43_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_43_3_bool = False
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_3_bool) + ']')
            # btnx_double_43_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_43_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_43_3_bool = True
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_3_bool) + ']')
            # btnx_double_43_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_43_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_43_4_bool = False
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_4_bool) + ']')
            # btnx_double_43_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_43_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_43_4_bool = True
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_4_bool) + ']')
            # btnx_double_43_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[200].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[200].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_0_timer_clicked_function():
    print(btnx_double_44_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[201].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[201].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_1_timer_clicked_function():
    print(btnx_double_44_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[202].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[202].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_2_timer_clicked_function():
    print(btnx_double_44_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[203].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[203].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_3_timer_clicked_function():
    print(btnx_double_44_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[204].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[204].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_4_timer_clicked_function():
    print(btnx_double_44_4_timer_clicked_function)

def btnx_double_44_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_44_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_44_0_bool = False
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_0_bool) + ']')
            # btnx_double_44_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_44_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_44_0_bool = True
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_0_bool) + ']')
            # btnx_double_44_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_44_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_44_1_bool = False
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_1_bool) + ']')
            # btnx_double_44_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_44_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_44_1_bool = True
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_1_bool) + ']')
            # btnx_double_44_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_44_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_44_2_bool = False
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_2_bool) + ']')
            # btnx_double_44_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_44_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_44_2_bool = True
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_2_bool) + ']')
            # btnx_double_44_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_44_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_44_3_bool = False
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_3_bool) + ']')
            # btnx_double_44_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_44_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_44_3_bool = True
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_3_bool) + ']')
            # btnx_double_44_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_44_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_44_4_bool = False
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_4_bool) + ']')
            # btnx_double_44_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_44_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_44_4_bool = True
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_4_bool) + ']')
            # btnx_double_44_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[205].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[205].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_0_timer_clicked_function():
    print(btnx_double_45_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[206].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[206].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_1_timer_clicked_function():
    print(btnx_double_45_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[207].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[207].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_2_timer_clicked_function():
    print(btnx_double_45_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[208].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[208].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_3_timer_clicked_function():
    print(btnx_double_45_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[209].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[209].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_4_timer_clicked_function():
    print(btnx_double_45_4_timer_clicked_function)

def btnx_double_45_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_45_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_45_0_bool = False
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_0_bool) + ']')
            # btnx_double_45_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_45_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_45_0_bool = True
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_0_bool) + ']')
            # btnx_double_45_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_45_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_45_1_bool = False
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_1_bool) + ']')
            # btnx_double_45_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_45_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_45_1_bool = True
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_1_bool) + ']')
            # btnx_double_45_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_45_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_45_2_bool = False
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_2_bool) + ']')
            # btnx_double_45_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_45_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_45_2_bool = True
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_2_bool) + ']')
            # btnx_double_45_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_45_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_45_3_bool = False
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_3_bool) + ']')
            # btnx_double_45_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_45_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_45_3_bool = True
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_3_bool) + ']')
            # btnx_double_45_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_45_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_45_4_bool = False
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_4_bool) + ']')
            # btnx_double_45_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_45_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_45_4_bool = True
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_4_bool) + ']')
            # btnx_double_45_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[210].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[210].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_0_timer_clicked_function():
    print(btnx_double_46_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[211].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[211].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_1_timer_clicked_function():
    print(btnx_double_46_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[212].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[212].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_2_timer_clicked_function():
    print(btnx_double_46_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[213].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[213].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_3_timer_clicked_function():
    print(btnx_double_46_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[214].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[214].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_4_timer_clicked_function():
    print(btnx_double_46_4_timer_clicked_function)

def btnx_double_46_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_46_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_46_0_bool = False
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_0_bool) + ']')
            # btnx_double_46_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_46_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_46_0_bool = True
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_0_bool) + ']')
            # btnx_double_46_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_46_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_46_1_bool = False
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_1_bool) + ']')
            # btnx_double_46_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_46_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_46_1_bool = True
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_1_bool) + ']')
            # btnx_double_46_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_46_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_46_2_bool = False
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_2_bool) + ']')
            # btnx_double_46_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_46_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_46_2_bool = True
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_2_bool) + ']')
            # btnx_double_46_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_46_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_46_3_bool = False
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_3_bool) + ']')
            # btnx_double_46_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_46_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_46_3_bool = True
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_3_bool) + ']')
            # btnx_double_46_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_46_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_46_4_bool = False
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_4_bool) + ']')
            # btnx_double_46_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_46_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_46_4_bool = True
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_4_bool) + ']')
            # btnx_double_46_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[215].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[215].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_0_timer_clicked_function():
    print(btnx_double_47_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[216].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[216].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_1_timer_clicked_function():
    print(btnx_double_47_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[217].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[217].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_2_timer_clicked_function():
    print(btnx_double_47_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[218].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[218].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_3_timer_clicked_function():
    print(btnx_double_47_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[219].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[219].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_4_timer_clicked_function():
    print(btnx_double_47_4_timer_clicked_function)

def btnx_double_47_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_47_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_47_0_bool = False
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_0_bool) + ']')
            # btnx_double_47_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_47_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_47_0_bool = True
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_0_bool) + ']')
            # btnx_double_47_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_47_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_47_1_bool = False
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_1_bool) + ']')
            # btnx_double_47_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_47_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_47_1_bool = True
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_1_bool) + ']')
            # btnx_double_47_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_47_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_47_2_bool = False
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_2_bool) + ']')
            # btnx_double_47_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_47_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_47_2_bool = True
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_2_bool) + ']')
            # btnx_double_47_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_47_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_47_3_bool = False
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_3_bool) + ']')
            # btnx_double_47_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_47_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_47_3_bool = True
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_3_bool) + ']')
            # btnx_double_47_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_47_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_47_4_bool = False
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_4_bool) + ']')
            # btnx_double_47_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_47_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_47_4_bool = True
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_4_bool) + ']')
            # btnx_double_47_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_48_start_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[4].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_48_stop_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[4].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_48_timer_clicked_function():
    print(btnx_double_48_timer_clicked_function)

def btnx_double_48_function():
    auto_gen_main_page.main_page = 4
    if auto_gen_btnx_double_bool.btnx_double_48_bool is True:
        auto_gen_btnx_double_bool.btnx_double_48_bool = False
        # btnx_double_48_stop_timer_function()
    elif auto_gen_btnx_double_bool.btnx_double_48_bool is False:
        auto_gen_btnx_double_bool.btnx_double_48_bool = True
        # btnx_double_48_start_timer_function()
    print('[btnx_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_48_bool) + ']')

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[220].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[220].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_0_timer_clicked_function():
    print(btnx_double_49_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[221].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[221].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_1_timer_clicked_function():
    print(btnx_double_49_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[222].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[222].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_2_timer_clicked_function():
    print(btnx_double_49_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[223].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[223].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_3_timer_clicked_function():
    print(btnx_double_49_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[224].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[224].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_4_timer_clicked_function():
    print(btnx_double_49_4_timer_clicked_function)

def btnx_double_49_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_49_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_49_0_bool = False
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_0_bool) + ']')
            # btnx_double_49_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_49_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_49_0_bool = True
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_0_bool) + ']')
            # btnx_double_49_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_49_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_49_1_bool = False
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_1_bool) + ']')
            # btnx_double_49_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_49_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_49_1_bool = True
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_1_bool) + ']')
            # btnx_double_49_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_49_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_49_2_bool = False
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_2_bool) + ']')
            # btnx_double_49_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_49_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_49_2_bool = True
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_2_bool) + ']')
            # btnx_double_49_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_49_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_49_3_bool = False
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_3_bool) + ']')
            # btnx_double_49_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_49_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_49_3_bool = True
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_3_bool) + ']')
            # btnx_double_49_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_49_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_49_4_bool = False
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_4_bool) + ']')
            # btnx_double_49_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_49_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_49_4_bool = True
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_4_bool) + ']')
            # btnx_double_49_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[225].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[225].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_0_timer_clicked_function():
    print(btnx_double_50_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[226].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[226].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_1_timer_clicked_function():
    print(btnx_double_50_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[227].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[227].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_2_timer_clicked_function():
    print(btnx_double_50_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[228].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[228].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_3_timer_clicked_function():
    print(btnx_double_50_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[229].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[229].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_4_timer_clicked_function():
    print(btnx_double_50_4_timer_clicked_function)

def btnx_double_50_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_50_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_50_0_bool = False
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_0_bool) + ']')
            # btnx_double_50_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_50_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_50_0_bool = True
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_0_bool) + ']')
            # btnx_double_50_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_50_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_50_1_bool = False
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_1_bool) + ']')
            # btnx_double_50_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_50_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_50_1_bool = True
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_1_bool) + ']')
            # btnx_double_50_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_50_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_50_2_bool = False
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_2_bool) + ']')
            # btnx_double_50_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_50_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_50_2_bool = True
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_2_bool) + ']')
            # btnx_double_50_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_50_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_50_3_bool = False
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_3_bool) + ']')
            # btnx_double_50_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_50_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_50_3_bool = True
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_3_bool) + ']')
            # btnx_double_50_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_50_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_50_4_bool = False
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_4_bool) + ']')
            # btnx_double_50_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_50_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_50_4_bool = True
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_4_bool) + ']')
            # btnx_double_50_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[230].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[230].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_0_timer_clicked_function():
    print(btnx_double_51_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[231].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[231].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_1_timer_clicked_function():
    print(btnx_double_51_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[232].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[232].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_2_timer_clicked_function():
    print(btnx_double_51_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[233].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[233].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_3_timer_clicked_function():
    print(btnx_double_51_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[234].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[234].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_4_timer_clicked_function():
    print(btnx_double_51_4_timer_clicked_function)

def btnx_double_51_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_51_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_51_0_bool = False
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_0_bool) + ']')
            # btnx_double_51_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_51_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_51_0_bool = True
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_0_bool) + ']')
            # btnx_double_51_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_51_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_51_1_bool = False
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_1_bool) + ']')
            # btnx_double_51_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_51_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_51_1_bool = True
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_1_bool) + ']')
            # btnx_double_51_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_51_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_51_2_bool = False
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_2_bool) + ']')
            # btnx_double_51_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_51_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_51_2_bool = True
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_2_bool) + ']')
            # btnx_double_51_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_51_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_51_3_bool = False
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_3_bool) + ']')
            # btnx_double_51_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_51_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_51_3_bool = True
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_3_bool) + ']')
            # btnx_double_51_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_51_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_51_4_bool = False
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_4_bool) + ']')
            # btnx_double_51_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_51_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_51_4_bool = True
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_4_bool) + ']')
            # btnx_double_51_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[235].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[235].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_0_timer_clicked_function():
    print(btnx_double_52_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[236].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[236].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_1_timer_clicked_function():
    print(btnx_double_52_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[237].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[237].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_2_timer_clicked_function():
    print(btnx_double_52_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[238].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[238].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_3_timer_clicked_function():
    print(btnx_double_52_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[239].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[239].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_4_timer_clicked_function():
    print(btnx_double_52_4_timer_clicked_function)

def btnx_double_52_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_52_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_52_0_bool = False
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_0_bool) + ']')
            # btnx_double_52_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_52_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_52_0_bool = True
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_0_bool) + ']')
            # btnx_double_52_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_52_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_52_1_bool = False
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_1_bool) + ']')
            # btnx_double_52_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_52_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_52_1_bool = True
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_1_bool) + ']')
            # btnx_double_52_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_52_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_52_2_bool = False
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_2_bool) + ']')
            # btnx_double_52_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_52_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_52_2_bool = True
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_2_bool) + ']')
            # btnx_double_52_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_52_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_52_3_bool = False
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_3_bool) + ']')
            # btnx_double_52_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_52_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_52_3_bool = True
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_3_bool) + ']')
            # btnx_double_52_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_52_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_52_4_bool = False
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_4_bool) + ']')
            # btnx_double_52_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_52_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_52_4_bool = True
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_4_bool) + ']')
            # btnx_double_52_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[240].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[240].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_0_timer_clicked_function():
    print(btnx_double_53_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[241].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[241].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_1_timer_clicked_function():
    print(btnx_double_53_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[242].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[242].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_2_timer_clicked_function():
    print(btnx_double_53_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[243].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[243].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_3_timer_clicked_function():
    print(btnx_double_53_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[244].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[244].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_4_timer_clicked_function():
    print(btnx_double_53_4_timer_clicked_function)

def btnx_double_53_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_53_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_53_0_bool = False
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_0_bool) + ']')
            # btnx_double_53_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_53_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_53_0_bool = True
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_0_bool) + ']')
            # btnx_double_53_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_53_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_53_1_bool = False
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_1_bool) + ']')
            # btnx_double_53_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_53_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_53_1_bool = True
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_1_bool) + ']')
            # btnx_double_53_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_53_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_53_2_bool = False
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_2_bool) + ']')
            # btnx_double_53_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_53_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_53_2_bool = True
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_2_bool) + ']')
            # btnx_double_53_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_53_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_53_3_bool = False
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_3_bool) + ']')
            # btnx_double_53_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_53_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_53_3_bool = True
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_3_bool) + ']')
            # btnx_double_53_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_53_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_53_4_bool = False
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_4_bool) + ']')
            # btnx_double_53_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_53_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_53_4_bool = True
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_4_bool) + ']')
            # btnx_double_53_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[245].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[245].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_0_timer_clicked_function():
    print(btnx_double_54_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[246].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[246].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_1_timer_clicked_function():
    print(btnx_double_54_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[247].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[247].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_2_timer_clicked_function():
    print(btnx_double_54_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[248].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[248].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_3_timer_clicked_function():
    print(btnx_double_54_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[249].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[249].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_4_timer_clicked_function():
    print(btnx_double_54_4_timer_clicked_function)

def btnx_double_54_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_54_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_54_0_bool = False
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_0_bool) + ']')
            # btnx_double_54_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_54_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_54_0_bool = True
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_0_bool) + ']')
            # btnx_double_54_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_54_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_54_1_bool = False
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_1_bool) + ']')
            # btnx_double_54_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_54_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_54_1_bool = True
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_1_bool) + ']')
            # btnx_double_54_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_54_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_54_2_bool = False
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_2_bool) + ']')
            # btnx_double_54_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_54_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_54_2_bool = True
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_2_bool) + ']')
            # btnx_double_54_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_54_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_54_3_bool = False
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_3_bool) + ']')
            # btnx_double_54_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_54_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_54_3_bool = True
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_3_bool) + ']')
            # btnx_double_54_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_54_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_54_4_bool = False
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_4_bool) + ']')
            # btnx_double_54_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_54_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_54_4_bool = True
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_4_bool) + ']')
            # btnx_double_54_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[250].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[250].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_0_timer_clicked_function():
    print(btnx_double_55_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[251].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[251].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_1_timer_clicked_function():
    print(btnx_double_55_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[252].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[252].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_2_timer_clicked_function():
    print(btnx_double_55_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[253].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[253].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_3_timer_clicked_function():
    print(btnx_double_55_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[254].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[254].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_4_timer_clicked_function():
    print(btnx_double_55_4_timer_clicked_function)

def btnx_double_55_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_55_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_55_0_bool = False
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_0_bool) + ']')
            # btnx_double_55_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_55_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_55_0_bool = True
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_0_bool) + ']')
            # btnx_double_55_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_55_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_55_1_bool = False
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_1_bool) + ']')
            # btnx_double_55_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_55_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_55_1_bool = True
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_1_bool) + ']')
            # btnx_double_55_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_55_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_55_2_bool = False
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_2_bool) + ']')
            # btnx_double_55_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_55_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_55_2_bool = True
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_2_bool) + ']')
            # btnx_double_55_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_55_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_55_3_bool = False
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_3_bool) + ']')
            # btnx_double_55_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_55_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_55_3_bool = True
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_3_bool) + ']')
            # btnx_double_55_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_55_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_55_4_bool = False
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_4_bool) + ']')
            # btnx_double_55_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_55_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_55_4_bool = True
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_4_bool) + ']')
            # btnx_double_55_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[255].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[255].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_0_timer_clicked_function():
    print(btnx_double_56_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[256].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[256].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_1_timer_clicked_function():
    print(btnx_double_56_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[257].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[257].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_2_timer_clicked_function():
    print(btnx_double_56_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[258].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[258].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_3_timer_clicked_function():
    print(btnx_double_56_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[259].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[259].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_4_timer_clicked_function():
    print(btnx_double_56_4_timer_clicked_function)

def btnx_double_56_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_56_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_56_0_bool = False
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_0_bool) + ']')
            # btnx_double_56_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_56_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_56_0_bool = True
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_0_bool) + ']')
            # btnx_double_56_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_56_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_56_1_bool = False
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_1_bool) + ']')
            # btnx_double_56_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_56_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_56_1_bool = True
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_1_bool) + ']')
            # btnx_double_56_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_56_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_56_2_bool = False
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_2_bool) + ']')
            # btnx_double_56_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_56_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_56_2_bool = True
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_2_bool) + ']')
            # btnx_double_56_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_56_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_56_3_bool = False
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_3_bool) + ']')
            # btnx_double_56_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_56_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_56_3_bool = True
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_3_bool) + ']')
            # btnx_double_56_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_56_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_56_4_bool = False
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_4_bool) + ']')
            # btnx_double_56_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_56_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_56_4_bool = True
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_4_bool) + ']')
            # btnx_double_56_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[260].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[260].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_0_timer_clicked_function():
    print(btnx_double_57_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[261].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[261].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_1_timer_clicked_function():
    print(btnx_double_57_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[262].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[262].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_2_timer_clicked_function():
    print(btnx_double_57_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[263].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[263].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_3_timer_clicked_function():
    print(btnx_double_57_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[264].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[264].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_4_timer_clicked_function():
    print(btnx_double_57_4_timer_clicked_function)

def btnx_double_57_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_57_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_57_0_bool = False
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_0_bool) + ']')
            # btnx_double_57_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_57_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_57_0_bool = True
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_0_bool) + ']')
            # btnx_double_57_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_57_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_57_1_bool = False
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_1_bool) + ']')
            # btnx_double_57_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_57_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_57_1_bool = True
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_1_bool) + ']')
            # btnx_double_57_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_57_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_57_2_bool = False
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_2_bool) + ']')
            # btnx_double_57_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_57_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_57_2_bool = True
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_2_bool) + ']')
            # btnx_double_57_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_57_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_57_3_bool = False
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_3_bool) + ']')
            # btnx_double_57_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_57_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_57_3_bool = True
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_3_bool) + ']')
            # btnx_double_57_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_57_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_57_4_bool = False
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_4_bool) + ']')
            # btnx_double_57_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_57_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_57_4_bool = True
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_4_bool) + ']')
            # btnx_double_57_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[265].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[265].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_0_timer_clicked_function():
    print(btnx_double_58_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[266].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[266].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_1_timer_clicked_function():
    print(btnx_double_58_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[267].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[267].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_2_timer_clicked_function():
    print(btnx_double_58_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[268].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[268].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_3_timer_clicked_function():
    print(btnx_double_58_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[269].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[269].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_4_timer_clicked_function():
    print(btnx_double_58_4_timer_clicked_function)

def btnx_double_58_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_58_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_58_0_bool = False
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_0_bool) + ']')
            # btnx_double_58_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_58_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_58_0_bool = True
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_0_bool) + ']')
            # btnx_double_58_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_58_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_58_1_bool = False
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_1_bool) + ']')
            # btnx_double_58_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_58_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_58_1_bool = True
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_1_bool) + ']')
            # btnx_double_58_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_58_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_58_2_bool = False
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_2_bool) + ']')
            # btnx_double_58_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_58_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_58_2_bool = True
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_2_bool) + ']')
            # btnx_double_58_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_58_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_58_3_bool = False
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_3_bool) + ']')
            # btnx_double_58_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_58_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_58_3_bool = True
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_3_bool) + ']')
            # btnx_double_58_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_58_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_58_4_bool = False
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_4_bool) + ']')
            # btnx_double_58_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_58_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_58_4_bool = True
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_4_bool) + ']')
            # btnx_double_58_4_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[270].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[270].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_0_timer_clicked_function():
    print(btnx_double_59_0_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_1_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[271].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_1_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[271].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_1_timer_clicked_function():
    print(btnx_double_59_1_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_2_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[272].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_2_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[272].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_2_timer_clicked_function():
    print(btnx_double_59_2_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_3_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[273].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_3_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[273].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_3_timer_clicked_function():
    print(btnx_double_59_3_timer_clicked_function)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_4_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[274].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_4_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[274].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_4_timer_clicked_function():
    print(btnx_double_59_4_timer_clicked_function)

def btnx_double_59_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_59_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_59_0_bool = False
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_0_bool) + ']')
            # btnx_double_59_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_59_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_59_0_bool = True
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_0_bool) + ']')
            # btnx_double_59_0_start_timer_function()

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_btnx_double_bool.btnx_double_59_1_bool is True:
            auto_gen_btnx_double_bool.btnx_double_59_1_bool = False
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_1_bool) + ']')
            # btnx_double_59_1_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_59_1_bool is False:
            auto_gen_btnx_double_bool.btnx_double_59_1_bool = True
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_1_bool) + ']')
            # btnx_double_59_1_start_timer_function()

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_btnx_double_bool.btnx_double_59_2_bool is True:
            auto_gen_btnx_double_bool.btnx_double_59_2_bool = False
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_2_bool) + ']')
            # btnx_double_59_2_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_59_2_bool is False:
            auto_gen_btnx_double_bool.btnx_double_59_2_bool = True
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_2_bool) + ']')
            # btnx_double_59_2_start_timer_function()

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_btnx_double_bool.btnx_double_59_3_bool is True:
            auto_gen_btnx_double_bool.btnx_double_59_3_bool = False
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_3_bool) + ']')
            # btnx_double_59_3_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_59_3_bool is False:
            auto_gen_btnx_double_bool.btnx_double_59_3_bool = True
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_3_bool) + ']')
            # btnx_double_59_3_start_timer_function()

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_btnx_double_bool.btnx_double_59_4_bool is True:
            auto_gen_btnx_double_bool.btnx_double_59_4_bool = False
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_4_bool) + ']')
            # btnx_double_59_4_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_59_4_bool is False:
            auto_gen_btnx_double_bool.btnx_double_59_4_bool = True
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_4_bool) + ']')
            # btnx_double_59_4_start_timer_function()

