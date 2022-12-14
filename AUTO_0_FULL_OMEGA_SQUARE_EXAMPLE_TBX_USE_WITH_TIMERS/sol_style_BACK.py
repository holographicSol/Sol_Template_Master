"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""

lblx_style = """QLabel{background-color: rgb(16, 16, 16);
                color: rgb(255, 255, 255);
                border-top:4px solid rgb(14, 14, 14);
                border-bottom:4px solid rgb(14, 14, 14);
                border-right:4px solid rgb(14, 14, 14);
                border-left:4px solid rgb(14, 14, 14);}"""

lblx_bg_blend_style = """QLabel{background-color: rgb(0, 0, 0);
                color: rgb(255, 255, 255);
                border-top:4px solid rgb(0, 0, 0);
                border-bottom:4px solid rgb(0, 0, 0);
                border-right:4px solid rgb(0, 0, 0);
                border-left:4px solid rgb(0, 0, 0);}"""

qlex_style = """QLineEdit{background-color: rgb(16, 16, 16);
                color: rgb(255, 255, 255);
                border-top:4px solid rgb(14, 14, 14);
                border-bottom:4px solid rgb(14, 14, 14);
                border-right:4px solid rgb(14, 14, 14);
                border-left:4px solid rgb(14, 14, 14);}"""

btn_title_bar_style = """QPushButton{background-color: rgb(0, 0, 0);
                border:0px solid rgb(0, 0, 0);}"""

btnx_style = """QPushButton{background-color: rgb(16, 16, 16);
                color: rgb(255, 255, 255);
                border-top:4px solid rgb(14, 14, 14);
                border-bottom:4px solid rgb(14, 14, 14);
                border-right:4px solid rgb(14, 14, 14);
                border-left:4px solid rgb(14, 14, 14);}"""

btn_disabled_style = """QPushButton{background-color: rgb(0, 0, 0);
                color: rgb(255, 255, 255);
                border-top:0px solid rgb(0, 0, 0);
                border-bottom:4px solid rgb(45, 45, 45);
                border-right:4px solid rgb(0, 0, 0);
                border-left:4px solid rgb(45, 45, 45);}"""

btn_disabled_text_low_style = """QPushButton{background-color: rgb(0, 0, 0);
                color: rgb(45, 45, 45);
                border-top:0px solid rgb(0, 0, 0);
                border-bottom:4px solid rgb(45, 45, 45);
                border-right:4px solid rgb(0, 0, 0);
                border-left:4px solid rgb(45, 45, 45);}"""

btn_enabled_text_low_style = """QPushButton{background-color: rgb(0, 0, 0);
                color: rgb(228, 228, 228);
                border-top:4px solid rgb(0, 0, 0);
                border-bottom:4px solid rgb(45, 45, 45);
                border-right:4px solid rgb(0, 0, 0);
                border-left:4px solid rgb(45, 45, 45);}"""

debug_enabled_style = """QPushButton{background-color: rgb(0, 0, 0);
                color: rgb(228, 228, 228);
                border-top:4px solid rgb(0, 0, 0);
                border-bottom:4px solid rgb(45, 45, 45);
                border-right:4px solid rgb(0, 0, 0);
                border-left:4px solid rgb(0, 255, 0);}"""

debug_kill_enabled_style = """QPushButton{background-color: rgb(0, 0, 0);
                color: rgb(255, 0, 0);
                border-top:4px solid rgb(0, 0, 0);
                border-bottom:4px solid rgb(45, 45, 45);
                border-right:4px solid rgb(0, 0, 0);
                border-left:4px solid rgb(45, 45, 45);}"""

self_style = """

                QMainWindow {background-color: rgb(0, 0, 0);
                color: rgb(200, 200, 200);
                border-top:0px solid rgb(20, 20, 20);
                border-bottom:0px solid rgb(20, 20, 20);
                border-right:0px solid rgb(20, 20, 20);
                border-left:0px solid rgb(20, 20, 20);
                }

                QToolTip {background-color: rgb(35, 35, 35);
                color: rgb(200, 200, 200);
                border-top:0px solid rgb(35, 35, 35);
                border-bottom:0px solid rgb(35, 35, 35);
                border-right:0px solid rgb(0, 0, 0);
                border-left:0px solid rgb(0, 0, 0);
                }
                
                QScrollBar:vertical {
                width: 20px;
                margin: 20px 0px 20px 0px;
                background-color: rgb(18, 18, 18);
                }
                QScrollBar:horizontal {
                height: 20px;
                margin: 0px 20px 0px 20px;
                background-color: rgb(18, 18, 18);
                }

                QScrollBar::handle:vertical {
                background-color: rgb(18, 18, 18);
                border-bottom:4px solid rgb(0, 0, 0);
                border-top:4px solid rgb(0, 0, 0);
                min-height: 10px;
                }
                QScrollBar::handle:horizontal {
                background-color: rgb(18, 18, 18);
                border-left:4px solid rgb(0, 0, 0);
                border-right:4px solid rgb(0, 0, 0);
                min-width: 10px;
                }

                QScrollBar::add-line:vertical {
                background-color: rgb(18, 18, 18);
                height: 20px;
                width: 20px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                }
                QScrollBar::sub-line:vertical {
                background-color: rgb(18, 18, 18);
                height: 20px;
                width: 20px;
                subcontrol-position: top;
                subcontrol-origin: margin;
                }
                
                QScrollBar::add-line:horizontal {
                background-color: rgb(18, 18, 18);
                height: 20px;
                width: 20px;
                subcontrol-position: right;
                subcontrol-origin: margin;
                }
                QScrollBar::sub-line:horizontal {
                background-color: rgb(20, 20, 20);
                height: 20px;
                width: 20px;
                subcontrol-position: top left;
                subcontrol-origin: margin;
                }

                QScrollBar::up-arrow:vertical {
                image:url('./resources/image/scroll_white.png');
                height: 20px;
                width: 20px;
                }
                QScrollBar::down-arrow:vertical {
                image:url('./resources/image/scroll_white.png');
                height: 20px;
                width: 20px;
                }

                QScrollBar::left-arrow:horizontal {
                image:url('./resources/image/scroll_white.png');
                height: 20px;
                width: 20px;
                }
                QScrollBar::right-arrow:horizontal {
                image:url('./resources/image/scroll_white.png');
                height: 20px;
                width: 20px;
                }

                QScrollBar::add-page:vertical {
                background-color: rgb(0, 0, 0);
                width: 20px;
                height: 20px;
                }
                QScrollBar::sub-page:vertical {
                background-color: rgb(8, 8, 8);
                width: 20px;
                height: 20px;
                }
                
                QScrollBar::add-page:horizontal {
                background-color: rgb(8, 8, 8);
                width: 20px;
                height: 20px;
                }
                QScrollBar::sub-page:horizontal {
                background-color: rgb(8, 8, 8);
                width: 20px;
                height: 20px;
                }
                
                """

textbox_stylesheet_default = """QTextBrowser {background-color: rgb(0, 0, 0);
                selection-color: black;
                selection-background-color: rgb(0, 180, 0);
                color: rgb(0, 255, 0);
                border-bottom:0px solid rgb(5, 5, 5);
                border-right:0px solid rgb(5, 5, 5);
                border-top:0px solid rgb(5, 5, 5);
                border-left:0px solid rgb(5, 5, 5);}"""
"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""

lblx_style = """QLabel{background-color: rgb(16, 16, 16);
color: rgb(255, 255, 255);
border-top:4px solid rgb(14, 14, 14);
border-bottom:4px solid rgb(14, 14, 14);
border-right:4px solid rgb(14, 14, 14);
border-left:4px solid rgb(14, 14, 14);}"""

lblx_bg_blend_style = """QLabel{background-color: rgb(0, 0, 0);
color: rgb(255, 255, 255);
border-top:4px solid rgb(0, 0, 0);
border-bottom:4px solid rgb(0, 0, 0);
border-right:4px solid rgb(0, 0, 0);
border-left:4px solid rgb(0, 0, 0);}"""

qlex_style = """QLineEdit{background-color: rgb(16, 16, 16);
color: rgb(255, 255, 255);
border-top:4px solid rgb(14, 14, 14);
border-bottom:4px solid rgb(14, 14, 14);
border-right:4px solid rgb(14, 14, 14);
border-left:4px solid rgb(14, 14, 14);}"""

btn_title_bar_style = """QPushButton{background-color: rgb(0, 0, 0);
border:0px solid rgb(0, 0, 0);}"""

btnx_style = """QPushButton{background-color: rgb(16, 16, 16);
color: rgb(255, 255, 255);
border-top:4px solid rgb(14, 14, 14);
border-bottom:4px solid rgb(14, 14, 14);
border-right:4px solid rgb(14, 14, 14);
border-left:4px solid rgb(14, 14, 14);}"""

btn_disabled_style = """QPushButton{background-color: rgb(0, 0, 0);
color: rgb(255, 255, 255);
border-top:0px solid rgb(0, 0, 0);
border-bottom:4px solid rgb(45, 45, 45);
border-right:4px solid rgb(0, 0, 0);
border-left:4px solid rgb(45, 45, 45);}"""

btn_disabled_text_low_style = """QPushButton{background-color: rgb(0, 0, 0);
color: rgb(45, 45, 45);
border-top:0px solid rgb(0, 0, 0);
border-bottom:4px solid rgb(45, 45, 45);
border-right:4px solid rgb(0, 0, 0);
border-left:4px solid rgb(45, 45, 45);}"""

btn_enabled_text_low_style = """QPushButton{background-color: rgb(0, 0, 0);
color: rgb(228, 228, 228);
border-top:4px solid rgb(0, 0, 0);
border-bottom:4px solid rgb(45, 45, 45);
border-right:4px solid rgb(0, 0, 0);
border-left:4px solid rgb(45, 45, 45);}"""

debug_enabled_style = """QPushButton{background-color: rgb(0, 0, 0);
color: rgb(228, 228, 228);
border-top:4px solid rgb(0, 0, 0);
border-bottom:4px solid rgb(45, 45, 45);
border-right:4px solid rgb(0, 0, 0);
border-left:4px solid rgb(0, 255, 0);}"""

debug_kill_enabled_style = """QPushButton{background-color: rgb(0, 0, 0);
color: rgb(255, 0, 0);
border-top:4px solid rgb(0, 0, 0);
border-bottom:4px solid rgb(45, 45, 45);
border-right:4px solid rgb(0, 0, 0);
border-left:4px solid rgb(45, 45, 45);}"""


main_border_height = 0
self_style = """

QMainWindow {background-color: rgb(0, 0, 0);
color: rgb(200, 200, 200);
border-top:"""+str(main_border_height)+"""px solid rgb(20, 20, 20);
border-bottom:"""+str(main_border_height)+"""px solid rgb(20, 20, 20);
border-right:"""+str(main_border_height)+"""px solid rgb(20, 20, 20);
border-left:"""+str(main_border_height)+"""px solid rgb(20, 20, 20);
}

QToolTip {background-color: rgb(35, 35, 35);
color: rgb(200, 200, 200);
border-top:0px solid rgb(35, 35, 35);
border-bottom:0px solid rgb(35, 35, 35);
border-right:0px solid rgb(0, 0, 0);
border-left:0px solid rgb(0, 0, 0);
}

QScrollBar:vertical {
width: 20px;
margin: 20px 0px 20px 0px;
background-color: rgb(18, 18, 18);
}
QScrollBar:horizontal {
height: 20px;
margin: 0px 20px 0px 20px;
background-color: rgb(18, 18, 18);
}

QScrollBar::handle:vertical {
background-color: rgb(18, 18, 18);
border-bottom:4px solid rgb(0, 0, 0);
border-top:4px solid rgb(0, 0, 0);
min-height: 10px;
}
QScrollBar::handle:horizontal {
background-color: rgb(18, 18, 18);
border-left:4px solid rgb(0, 0, 0);
border-right:4px solid rgb(0, 0, 0);
min-width: 10px;
}

QScrollBar::add-line:vertical {
background-color: rgb(18, 18, 18);
height: 20px;
width: 20px;
subcontrol-position: bottom;
subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
background-color: rgb(18, 18, 18);
height: 20px;
width: 20px;
subcontrol-position: top;
subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal {
background-color: rgb(18, 18, 18);
height: 20px;
width: 20px;
subcontrol-position: right;
subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
background-color: rgb(20, 20, 20);
height: 20px;
width: 20px;
subcontrol-position: top left;
subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical {
image:url('./resources/image/scroll_white.png');
height: 20px;
width: 20px;
}
QScrollBar::down-arrow:vertical {
image:url('./resources/image/scroll_white.png');
height: 20px;
width: 20px;
}

QScrollBar::left-arrow:horizontal {
image:url('./resources/image/scroll_white.png');
height: 20px;
width: 20px;
}
QScrollBar::right-arrow:horizontal {
image:url('./resources/image/scroll_white.png');
height: 20px;
width: 20px;
}

QScrollBar::add-page:vertical {
background-color: rgb(0, 0, 0);
width: 20px;
height: 20px;
}
QScrollBar::sub-page:vertical {
background-color: rgb(8, 8, 8);
width: 20px;
height: 20px;
}

QScrollBar::add-page:horizontal {
background-color: rgb(8, 8, 8);
width: 20px;
height: 20px;
}
QScrollBar::sub-page:horizontal {
background-color: rgb(8, 8, 8);
width: 20px;
height: 20px;
}

"""

textbox_stylesheet_default = """QTextBrowser {background-color: rgb(0, 0, 0);
selection-color: black;
selection-background-color: rgb(0, 180, 0);
color: rgb(0, 255, 0);
border-bottom:0px solid rgb(5, 5, 5);
border-right:0px solid rgb(5, 5, 5);
border-top:0px solid rgb(5, 5, 5);
border-left:0px solid rgb(5, 5, 5);}"""
