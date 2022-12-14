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

def qlex_double_0_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_0'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_0_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_0_0_bool = False
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_0_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_0_0_bool = True
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_0_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_0_1_bool = False
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_0_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_0_1_bool = True
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_0_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_0_2_bool = False
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_0_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_0_2_bool = True
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_0_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_0_3_bool = False
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_0_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_0_3_bool = True
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_0_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_0_4_bool = False
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_0_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_0_4_bool = True
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_4_bool) + ']')

def qlex_double_1_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_1'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_1_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_1_0_bool = False
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_1_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_1_0_bool = True
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_1_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_1_1_bool = False
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_1_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_1_1_bool = True
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_1_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_1_2_bool = False
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_1_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_1_2_bool = True
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_1_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_1_3_bool = False
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_1_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_1_3_bool = True
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_1_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_1_4_bool = False
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_1_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_1_4_bool = True
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_4_bool) + ']')

def qlex_double_2_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_2'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_2_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_2_0_bool = False
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_2_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_2_0_bool = True
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_2_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_2_1_bool = False
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_2_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_2_1_bool = True
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_2_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_2_2_bool = False
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_2_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_2_2_bool = True
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_2_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_2_3_bool = False
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_2_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_2_3_bool = True
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_2_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_2_4_bool = False
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_2_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_2_4_bool = True
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_4_bool) + ']')

def qlex_double_3_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_3'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_3_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_3_0_bool = False
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_3_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_3_0_bool = True
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_3_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_3_1_bool = False
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_3_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_3_1_bool = True
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_3_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_3_2_bool = False
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_3_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_3_2_bool = True
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_3_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_3_3_bool = False
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_3_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_3_3_bool = True
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_3_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_3_4_bool = False
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_3_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_3_4_bool = True
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_4_bool) + ']')

def qlex_double_4_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_4'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_4_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_4_0_bool = False
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_4_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_4_0_bool = True
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_4_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_4_1_bool = False
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_4_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_4_1_bool = True
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_4_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_4_2_bool = False
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_4_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_4_2_bool = True
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_4_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_4_3_bool = False
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_4_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_4_3_bool = True
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_4_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_4_4_bool = False
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_4_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_4_4_bool = True
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_4_bool) + ']')

def qlex_double_5_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_5'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_5_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_5_0_bool = False
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_5_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_5_0_bool = True
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_5_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_5_1_bool = False
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_5_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_5_1_bool = True
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_5_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_5_2_bool = False
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_5_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_5_2_bool = True
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_5_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_5_3_bool = False
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_5_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_5_3_bool = True
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_5_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_5_4_bool = False
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_5_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_5_4_bool = True
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_4_bool) + ']')

def qlex_double_6_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_6'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_6_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_6_0_bool = False
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_6_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_6_0_bool = True
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_6_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_6_1_bool = False
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_6_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_6_1_bool = True
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_6_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_6_2_bool = False
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_6_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_6_2_bool = True
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_6_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_6_3_bool = False
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_6_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_6_3_bool = True
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_6_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_6_4_bool = False
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_6_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_6_4_bool = True
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_4_bool) + ']')

def qlex_double_7_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_7'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_7_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_7_0_bool = False
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_7_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_7_0_bool = True
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_7_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_7_1_bool = False
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_7_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_7_1_bool = True
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_7_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_7_2_bool = False
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_7_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_7_2_bool = True
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_7_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_7_3_bool = False
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_7_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_7_3_bool = True
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_7_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_7_4_bool = False
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_7_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_7_4_bool = True
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_4_bool) + ']')

def qlex_double_8_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_8'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_8_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_8_0_bool = False
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_8_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_8_0_bool = True
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_8_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_8_1_bool = False
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_8_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_8_1_bool = True
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_8_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_8_2_bool = False
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_8_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_8_2_bool = True
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_8_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_8_3_bool = False
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_8_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_8_3_bool = True
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_8_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_8_4_bool = False
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_8_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_8_4_bool = True
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_4_bool) + ']')

def qlex_double_9_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_9'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_9_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_9_0_bool = False
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_9_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_9_0_bool = True
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_9_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_9_1_bool = False
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_9_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_9_1_bool = True
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_9_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_9_2_bool = False
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_9_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_9_2_bool = True
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_9_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_9_3_bool = False
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_9_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_9_3_bool = True
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_9_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_9_4_bool = False
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_9_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_9_4_bool = True
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_4_bool) + ']')

def qlex_double_10_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_10'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_10_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_10_0_bool = False
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_10_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_10_0_bool = True
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_10_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_10_1_bool = False
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_10_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_10_1_bool = True
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_10_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_10_2_bool = False
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_10_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_10_2_bool = True
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_10_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_10_3_bool = False
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_10_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_10_3_bool = True
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_10_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_10_4_bool = False
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_10_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_10_4_bool = True
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_4_bool) + ']')

def qlex_double_11_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_11'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_11_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_11_0_bool = False
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_11_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_11_0_bool = True
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_11_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_11_1_bool = False
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_11_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_11_1_bool = True
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_11_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_11_2_bool = False
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_11_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_11_2_bool = True
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_11_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_11_3_bool = False
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_11_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_11_3_bool = True
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_11_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_11_4_bool = False
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_11_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_11_4_bool = True
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_4_bool) + ']')

def qlex_double_12_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_12'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_12_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_12_0_bool = False
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_12_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_12_0_bool = True
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_12_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_12_1_bool = False
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_12_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_12_1_bool = True
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_12_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_12_2_bool = False
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_12_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_12_2_bool = True
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_12_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_12_3_bool = False
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_12_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_12_3_bool = True
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_12_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_12_4_bool = False
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_12_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_12_4_bool = True
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_4_bool) + ']')

def qlex_double_13_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_13'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_13_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_13_0_bool = False
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_13_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_13_0_bool = True
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_13_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_13_1_bool = False
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_13_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_13_1_bool = True
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_13_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_13_2_bool = False
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_13_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_13_2_bool = True
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_13_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_13_3_bool = False
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_13_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_13_3_bool = True
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_13_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_13_4_bool = False
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_13_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_13_4_bool = True
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_4_bool) + ']')

def qlex_double_14_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_14'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_14_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_14_0_bool = False
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_14_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_14_0_bool = True
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_14_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_14_1_bool = False
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_14_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_14_1_bool = True
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_14_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_14_2_bool = False
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_14_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_14_2_bool = True
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_14_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_14_3_bool = False
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_14_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_14_3_bool = True
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_14_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_14_4_bool = False
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_14_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_14_4_bool = True
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_4_bool) + ']')

def qlex_double_15_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_15'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_15_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_15_0_bool = False
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_15_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_15_0_bool = True
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_15_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_15_1_bool = False
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_15_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_15_1_bool = True
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_15_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_15_2_bool = False
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_15_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_15_2_bool = True
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_15_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_15_3_bool = False
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_15_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_15_3_bool = True
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_15_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_15_4_bool = False
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_15_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_15_4_bool = True
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_4_bool) + ']')

def qlex_double_16_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_16'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_16_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_16_0_bool = False
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_16_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_16_0_bool = True
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_16_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_16_1_bool = False
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_16_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_16_1_bool = True
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_16_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_16_2_bool = False
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_16_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_16_2_bool = True
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_16_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_16_3_bool = False
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_16_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_16_3_bool = True
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_16_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_16_4_bool = False
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_16_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_16_4_bool = True
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_4_bool) + ']')

def qlex_double_17_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_17'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_17_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_17_0_bool = False
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_17_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_17_0_bool = True
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_17_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_17_1_bool = False
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_17_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_17_1_bool = True
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_17_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_17_2_bool = False
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_17_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_17_2_bool = True
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_17_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_17_3_bool = False
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_17_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_17_3_bool = True
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_17_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_17_4_bool = False
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_17_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_17_4_bool = True
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_4_bool) + ']')

def qlex_double_18_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_18'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_18_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_18_0_bool = False
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_18_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_18_0_bool = True
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_18_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_18_1_bool = False
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_18_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_18_1_bool = True
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_18_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_18_2_bool = False
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_18_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_18_2_bool = True
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_18_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_18_3_bool = False
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_18_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_18_3_bool = True
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_18_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_18_4_bool = False
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_18_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_18_4_bool = True
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_4_bool) + ']')

def qlex_double_19_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_19'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_19_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_19_0_bool = False
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_19_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_19_0_bool = True
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_19_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_19_1_bool = False
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_19_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_19_1_bool = True
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_19_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_19_2_bool = False
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_19_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_19_2_bool = True
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_19_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_19_3_bool = False
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_19_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_19_3_bool = True
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_19_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_19_4_bool = False
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_19_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_19_4_bool = True
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_4_bool) + ']')

def qlex_double_20_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_20'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_20_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_20_0_bool = False
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_20_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_20_0_bool = True
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_20_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_20_1_bool = False
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_20_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_20_1_bool = True
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_20_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_20_2_bool = False
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_20_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_20_2_bool = True
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_20_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_20_3_bool = False
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_20_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_20_3_bool = True
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_20_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_20_4_bool = False
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_20_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_20_4_bool = True
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_4_bool) + ']')

def qlex_double_21_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_21'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_21_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_21_0_bool = False
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_21_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_21_0_bool = True
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_21_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_21_1_bool = False
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_21_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_21_1_bool = True
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_21_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_21_2_bool = False
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_21_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_21_2_bool = True
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_21_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_21_3_bool = False
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_21_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_21_3_bool = True
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_21_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_21_4_bool = False
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_21_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_21_4_bool = True
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_4_bool) + ']')

def qlex_double_22_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_22'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_22_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_22_0_bool = False
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_22_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_22_0_bool = True
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_22_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_22_1_bool = False
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_22_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_22_1_bool = True
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_22_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_22_2_bool = False
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_22_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_22_2_bool = True
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_22_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_22_3_bool = False
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_22_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_22_3_bool = True
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_22_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_22_4_bool = False
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_22_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_22_4_bool = True
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_4_bool) + ']')

def qlex_double_23_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_23'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_23_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_23_0_bool = False
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_23_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_23_0_bool = True
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_23_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_23_1_bool = False
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_23_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_23_1_bool = True
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_23_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_23_2_bool = False
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_23_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_23_2_bool = True
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_23_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_23_3_bool = False
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_23_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_23_3_bool = True
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_23_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_23_4_bool = False
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_23_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_23_4_bool = True
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_4_bool) + ']')

def qlex_double_24_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_24'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_24_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_24_0_bool = False
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_24_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_24_0_bool = True
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_24_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_24_1_bool = False
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_24_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_24_1_bool = True
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_24_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_24_2_bool = False
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_24_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_24_2_bool = True
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_24_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_24_3_bool = False
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_24_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_24_3_bool = True
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_24_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_24_4_bool = False
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_24_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_24_4_bool = True
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_4_bool) + ']')

def qlex_double_25_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_25'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_25_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_25_0_bool = False
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_25_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_25_0_bool = True
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_25_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_25_1_bool = False
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_25_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_25_1_bool = True
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_25_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_25_2_bool = False
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_25_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_25_2_bool = True
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_25_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_25_3_bool = False
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_25_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_25_3_bool = True
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_25_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_25_4_bool = False
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_25_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_25_4_bool = True
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_4_bool) + ']')

def qlex_double_26_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_26'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_26_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_26_0_bool = False
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_26_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_26_0_bool = True
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_26_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_26_1_bool = False
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_26_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_26_1_bool = True
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_26_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_26_2_bool = False
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_26_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_26_2_bool = True
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_26_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_26_3_bool = False
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_26_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_26_3_bool = True
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_26_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_26_4_bool = False
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_26_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_26_4_bool = True
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_4_bool) + ']')

def qlex_double_27_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_27'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_27_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_27_0_bool = False
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_27_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_27_0_bool = True
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_27_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_27_1_bool = False
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_27_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_27_1_bool = True
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_27_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_27_2_bool = False
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_27_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_27_2_bool = True
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_27_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_27_3_bool = False
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_27_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_27_3_bool = True
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_27_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_27_4_bool = False
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_27_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_27_4_bool = True
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_4_bool) + ']')

def qlex_double_28_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_28'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_28_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_28_0_bool = False
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_28_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_28_0_bool = True
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_28_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_28_1_bool = False
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_28_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_28_1_bool = True
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_28_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_28_2_bool = False
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_28_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_28_2_bool = True
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_28_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_28_3_bool = False
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_28_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_28_3_bool = True
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_28_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_28_4_bool = False
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_28_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_28_4_bool = True
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_4_bool) + ']')

def qlex_double_29_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_29'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_29_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_29_0_bool = False
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_29_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_29_0_bool = True
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_29_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_29_1_bool = False
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_29_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_29_1_bool = True
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_29_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_29_2_bool = False
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_29_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_29_2_bool = True
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_29_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_29_3_bool = False
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_29_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_29_3_bool = True
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_29_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_29_4_bool = False
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_29_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_29_4_bool = True
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_4_bool) + ']')

def qlex_double_30_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_30'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_30_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_30_0_bool = False
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_30_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_30_0_bool = True
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_30_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_30_1_bool = False
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_30_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_30_1_bool = True
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_30_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_30_2_bool = False
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_30_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_30_2_bool = True
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_30_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_30_3_bool = False
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_30_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_30_3_bool = True
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_30_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_30_4_bool = False
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_30_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_30_4_bool = True
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_4_bool) + ']')

def qlex_double_31_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_31'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_31_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_31_0_bool = False
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_31_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_31_0_bool = True
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_31_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_31_1_bool = False
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_31_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_31_1_bool = True
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_31_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_31_2_bool = False
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_31_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_31_2_bool = True
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_31_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_31_3_bool = False
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_31_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_31_3_bool = True
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_31_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_31_4_bool = False
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_31_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_31_4_bool = True
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_4_bool) + ']')

def qlex_double_32_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_32'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_32_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_32_0_bool = False
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_32_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_32_0_bool = True
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_32_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_32_1_bool = False
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_32_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_32_1_bool = True
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_32_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_32_2_bool = False
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_32_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_32_2_bool = True
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_32_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_32_3_bool = False
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_32_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_32_3_bool = True
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_32_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_32_4_bool = False
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_32_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_32_4_bool = True
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_4_bool) + ']')

def qlex_double_33_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_33'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_33_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_33_0_bool = False
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_33_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_33_0_bool = True
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_33_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_33_1_bool = False
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_33_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_33_1_bool = True
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_33_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_33_2_bool = False
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_33_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_33_2_bool = True
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_33_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_33_3_bool = False
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_33_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_33_3_bool = True
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_33_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_33_4_bool = False
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_33_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_33_4_bool = True
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_4_bool) + ']')

def qlex_double_34_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_34'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_34_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_34_0_bool = False
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_34_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_34_0_bool = True
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_34_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_34_1_bool = False
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_34_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_34_1_bool = True
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_34_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_34_2_bool = False
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_34_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_34_2_bool = True
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_34_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_34_3_bool = False
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_34_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_34_3_bool = True
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_34_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_34_4_bool = False
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_34_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_34_4_bool = True
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_4_bool) + ']')

def qlex_double_35_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_35'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_35_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_35_0_bool = False
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_35_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_35_0_bool = True
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_35_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_35_1_bool = False
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_35_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_35_1_bool = True
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_35_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_35_2_bool = False
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_35_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_35_2_bool = True
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_35_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_35_3_bool = False
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_35_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_35_3_bool = True
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_35_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_35_4_bool = False
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_35_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_35_4_bool = True
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_4_bool) + ']')

def qlex_double_36_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_36'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_36_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_36_0_bool = False
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_36_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_36_0_bool = True
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_36_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_36_1_bool = False
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_36_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_36_1_bool = True
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_36_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_36_2_bool = False
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_36_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_36_2_bool = True
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_36_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_36_3_bool = False
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_36_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_36_3_bool = True
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_36_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_36_4_bool = False
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_36_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_36_4_bool = True
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_4_bool) + ']')

def qlex_double_37_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_37'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_37_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_37_0_bool = False
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_37_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_37_0_bool = True
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_37_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_37_1_bool = False
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_37_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_37_1_bool = True
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_37_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_37_2_bool = False
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_37_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_37_2_bool = True
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_37_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_37_3_bool = False
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_37_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_37_3_bool = True
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_37_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_37_4_bool = False
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_37_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_37_4_bool = True
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_4_bool) + ']')

def qlex_double_38_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_38'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_38_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_38_0_bool = False
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_38_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_38_0_bool = True
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_38_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_38_1_bool = False
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_38_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_38_1_bool = True
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_38_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_38_2_bool = False
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_38_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_38_2_bool = True
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_38_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_38_3_bool = False
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_38_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_38_3_bool = True
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_38_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_38_4_bool = False
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_38_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_38_4_bool = True
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_4_bool) + ']')

def qlex_double_39_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_39'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_39_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_39_0_bool = False
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_39_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_39_0_bool = True
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_39_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_39_1_bool = False
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_39_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_39_1_bool = True
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_39_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_39_2_bool = False
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_39_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_39_2_bool = True
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_39_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_39_3_bool = False
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_39_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_39_3_bool = True
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_39_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_39_4_bool = False
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_39_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_39_4_bool = True
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_4_bool) + ']')

def qlex_double_40_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_40'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_40_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_40_0_bool = False
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_40_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_40_0_bool = True
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_40_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_40_1_bool = False
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_40_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_40_1_bool = True
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_40_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_40_2_bool = False
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_40_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_40_2_bool = True
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_40_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_40_3_bool = False
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_40_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_40_3_bool = True
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_40_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_40_4_bool = False
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_40_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_40_4_bool = True
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_4_bool) + ']')

def qlex_double_41_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_41'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_41_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_41_0_bool = False
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_41_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_41_0_bool = True
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_41_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_41_1_bool = False
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_41_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_41_1_bool = True
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_41_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_41_2_bool = False
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_41_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_41_2_bool = True
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_41_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_41_3_bool = False
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_41_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_41_3_bool = True
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_41_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_41_4_bool = False
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_41_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_41_4_bool = True
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_4_bool) + ']')

def qlex_double_42_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_42'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_42_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_42_0_bool = False
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_42_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_42_0_bool = True
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_42_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_42_1_bool = False
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_42_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_42_1_bool = True
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_42_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_42_2_bool = False
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_42_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_42_2_bool = True
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_42_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_42_3_bool = False
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_42_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_42_3_bool = True
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_42_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_42_4_bool = False
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_42_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_42_4_bool = True
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_4_bool) + ']')

def qlex_double_43_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_43'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_43_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_43_0_bool = False
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_43_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_43_0_bool = True
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_43_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_43_1_bool = False
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_43_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_43_1_bool = True
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_43_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_43_2_bool = False
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_43_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_43_2_bool = True
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_43_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_43_3_bool = False
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_43_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_43_3_bool = True
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_43_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_43_4_bool = False
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_43_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_43_4_bool = True
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_4_bool) + ']')

def qlex_double_44_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_44'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_44_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_44_0_bool = False
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_44_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_44_0_bool = True
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_44_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_44_1_bool = False
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_44_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_44_1_bool = True
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_44_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_44_2_bool = False
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_44_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_44_2_bool = True
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_44_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_44_3_bool = False
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_44_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_44_3_bool = True
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_44_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_44_4_bool = False
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_44_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_44_4_bool = True
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_4_bool) + ']')

def qlex_double_45_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_45'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_45_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_45_0_bool = False
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_45_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_45_0_bool = True
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_45_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_45_1_bool = False
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_45_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_45_1_bool = True
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_45_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_45_2_bool = False
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_45_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_45_2_bool = True
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_45_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_45_3_bool = False
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_45_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_45_3_bool = True
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_45_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_45_4_bool = False
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_45_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_45_4_bool = True
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_4_bool) + ']')

def qlex_double_46_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_46'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_46_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_46_0_bool = False
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_46_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_46_0_bool = True
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_46_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_46_1_bool = False
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_46_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_46_1_bool = True
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_46_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_46_2_bool = False
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_46_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_46_2_bool = True
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_46_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_46_3_bool = False
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_46_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_46_3_bool = True
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_46_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_46_4_bool = False
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_46_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_46_4_bool = True
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_4_bool) + ']')

def qlex_double_47_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_47'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_47_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_47_0_bool = False
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_47_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_47_0_bool = True
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_47_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_47_1_bool = False
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_47_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_47_1_bool = True
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_47_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_47_2_bool = False
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_47_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_47_2_bool = True
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_47_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_47_3_bool = False
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_47_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_47_3_bool = True
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_47_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_47_4_bool = False
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_47_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_47_4_bool = True
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_4_bool) + ']')

def qlex_double_48_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_48'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_48_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_48_0_bool = False
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_48_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_48_0_bool = True
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_48_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_48_1_bool = False
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_48_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_48_1_bool = True
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_48_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_48_2_bool = False
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_48_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_48_2_bool = True
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_48_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_48_3_bool = False
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_48_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_48_3_bool = True
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_48_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_48_4_bool = False
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_48_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_48_4_bool = True
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_4_bool) + ']')

def qlex_double_49_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_49'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_49_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_49_0_bool = False
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_49_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_49_0_bool = True
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_49_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_49_1_bool = False
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_49_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_49_1_bool = True
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_49_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_49_2_bool = False
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_49_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_49_2_bool = True
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_49_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_49_3_bool = False
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_49_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_49_3_bool = True
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_49_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_49_4_bool = False
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_49_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_49_4_bool = True
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_4_bool) + ']')

def qlex_double_50_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_50'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_50_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_50_0_bool = False
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_50_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_50_0_bool = True
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_50_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_50_1_bool = False
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_50_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_50_1_bool = True
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_50_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_50_2_bool = False
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_50_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_50_2_bool = True
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_50_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_50_3_bool = False
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_50_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_50_3_bool = True
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_50_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_50_4_bool = False
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_50_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_50_4_bool = True
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_4_bool) + ']')

def qlex_double_51_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_51'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_51_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_51_0_bool = False
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_51_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_51_0_bool = True
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_51_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_51_1_bool = False
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_51_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_51_1_bool = True
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_51_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_51_2_bool = False
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_51_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_51_2_bool = True
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_51_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_51_3_bool = False
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_51_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_51_3_bool = True
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_51_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_51_4_bool = False
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_51_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_51_4_bool = True
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_4_bool) + ']')

def qlex_double_52_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_52'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_52_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_52_0_bool = False
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_52_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_52_0_bool = True
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_52_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_52_1_bool = False
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_52_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_52_1_bool = True
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_52_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_52_2_bool = False
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_52_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_52_2_bool = True
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_52_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_52_3_bool = False
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_52_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_52_3_bool = True
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_52_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_52_4_bool = False
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_52_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_52_4_bool = True
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_4_bool) + ']')

def qlex_double_53_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_53'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_53_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_53_0_bool = False
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_53_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_53_0_bool = True
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_53_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_53_1_bool = False
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_53_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_53_1_bool = True
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_53_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_53_2_bool = False
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_53_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_53_2_bool = True
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_53_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_53_3_bool = False
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_53_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_53_3_bool = True
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_53_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_53_4_bool = False
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_53_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_53_4_bool = True
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_4_bool) + ']')

def qlex_double_54_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_54'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_54_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_54_0_bool = False
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_54_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_54_0_bool = True
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_54_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_54_1_bool = False
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_54_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_54_1_bool = True
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_54_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_54_2_bool = False
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_54_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_54_2_bool = True
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_54_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_54_3_bool = False
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_54_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_54_3_bool = True
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_54_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_54_4_bool = False
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_54_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_54_4_bool = True
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_4_bool) + ']')

def qlex_double_55_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_55'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_55_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_55_0_bool = False
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_55_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_55_0_bool = True
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_55_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_55_1_bool = False
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_55_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_55_1_bool = True
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_55_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_55_2_bool = False
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_55_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_55_2_bool = True
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_55_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_55_3_bool = False
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_55_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_55_3_bool = True
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_55_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_55_4_bool = False
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_55_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_55_4_bool = True
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_4_bool) + ']')

def qlex_double_56_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_56'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_56_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_56_0_bool = False
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_56_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_56_0_bool = True
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_56_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_56_1_bool = False
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_56_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_56_1_bool = True
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_56_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_56_2_bool = False
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_56_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_56_2_bool = True
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_56_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_56_3_bool = False
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_56_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_56_3_bool = True
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_56_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_56_4_bool = False
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_56_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_56_4_bool = True
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_4_bool) + ']')

def qlex_double_57_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_57'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_57_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_57_0_bool = False
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_57_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_57_0_bool = True
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_57_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_57_1_bool = False
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_57_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_57_1_bool = True
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_57_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_57_2_bool = False
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_57_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_57_2_bool = True
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_57_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_57_3_bool = False
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_57_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_57_3_bool = True
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_57_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_57_4_bool = False
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_57_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_57_4_bool = True
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_4_bool) + ']')

def qlex_double_58_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_58'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_58_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_58_0_bool = False
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_58_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_58_0_bool = True
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_58_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_58_1_bool = False
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_58_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_58_1_bool = True
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_58_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_58_2_bool = False
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_58_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_58_2_bool = True
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_58_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_58_3_bool = False
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_58_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_58_3_bool = True
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_58_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_58_4_bool = False
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_58_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_58_4_bool = True
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_4_bool) + ']')

def qlex_double_59_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_59'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_59_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_59_0_bool = False
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_59_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_59_0_bool = True
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_0_bool) + ']')

    elif auto_gen_main_page.main_page == 1:
        if auto_gen_qle_double_bool.qlex_double_59_1_bool is True:
            auto_gen_qle_double_bool.qlex_double_59_1_bool = False
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_1_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_59_1_bool is False:
            auto_gen_qle_double_bool.qlex_double_59_1_bool = True
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_1_bool) + ']')

    elif auto_gen_main_page.main_page == 2:
        if auto_gen_qle_double_bool.qlex_double_59_2_bool is True:
            auto_gen_qle_double_bool.qlex_double_59_2_bool = False
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_2_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_59_2_bool is False:
            auto_gen_qle_double_bool.qlex_double_59_2_bool = True
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_2_bool) + ']')

    elif auto_gen_main_page.main_page == 3:
        if auto_gen_qle_double_bool.qlex_double_59_3_bool is True:
            auto_gen_qle_double_bool.qlex_double_59_3_bool = False
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_3_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_59_3_bool is False:
            auto_gen_qle_double_bool.qlex_double_59_3_bool = True
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_3_bool) + ']')

    elif auto_gen_main_page.main_page == 4:
        if auto_gen_qle_double_bool.qlex_double_59_4_bool is True:
            auto_gen_qle_double_bool.qlex_double_59_4_bool = False
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_4_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_59_4_bool is False:
            auto_gen_qle_double_bool.qlex_double_59_4_bool = True
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_4_bool) + ']')

