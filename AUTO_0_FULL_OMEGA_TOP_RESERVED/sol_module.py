import os
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
from win32api import GetMonitorInfo, MonitorFromPoint
from pywinauto import application
from platform import system as platform_name
from Crypto import Random
from Crypto.Cipher import AES
import base64
import unicodedata
import distutils.dir_util
import fileinput
import ctypes
from ctypes import *
from distutils import spawn
from mutagen import File
import codecs
from PIL import Image
import random
import string
import encodings

from importlib import reload
from superglobals import *
import sol_style as style

shell = win32com.client.Dispatch("WScript.Shell")
app = application.Application()

# ------------------------- PRINT
def p(text):
    var = '['+str(datetime.datetime.now())+'] '+text
    print(var)

def prow(digit):
    var = '-' * int(digit)
    print(var)

def ptitle(text):
    prow(50)
    var = str('[ ') + text + str(' ]\n')
    print(var)

# ------------------------- SOL MODULE
def solList():
    p('[sol_module.solList]')
    with open('./sol_module.py', 'r') as fo:
        for line in fo:
            line = line.strip()
            if line.startswith('def ') and line.endswith('):'):
                p('[sol_module.solList] ' + line)
    fo.close()

# ------------------------- ADMIN CHECK
def admin_check():
    _bool = None
    if os.name == 'nt':
        if ctypes.windll.shell32.IsUserAnAdmin():
            print('-- [Admin]: True')
            _bool = True
            
        else:
            print('-- [Admin]: False')
            _bool = False
    return _bool

# ------------------------- SYSTEM
def work_area():
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    work_area = monitor_info.get("Work")
    return work_area[2], work_area[3]


# ------------------------- FILES AND DIRECTORIES
def makeD(text):
    distutils.dir_util.mkpath(text)

def makeF(text):
    if not os.path.exists(text):
        open(text, 'w').close()

def find_exe(text):
    return spawn.find_executable(text)

def extract_apic_cover(text, path):
    file = File(text)
    artwork = file.tags['APIC:cover'].data
    with open(path, 'wb') as img:
        img.write(artwork)

# takes (list, list)
def count_lines_recursively(path, ext):
    
    full_results = []
    f_item = []
    i = 0
    for paths in path:
        for dirName, subdirList, fileList in os.walk(path[i]):
            for fname in fileList:
                if ext != None:
                    if fname.endswith(tuple(ext)):
                        fullpath = os.path.join(dirName, fname)
                        print(fullpath)
                        f_item.append(fullpath)
                else:
                    fullpath = os.path.join(dirName, fname)
                    print(fullpath)
                    f_item.append(fullpath)
        i += 1
    total_line_count = 0
    line_count = 0
    i = 0
    for f_items in f_item:
        try:
            with codecs.open(f_item[i], 'r', encoding='utf-8') as fo:
                for lines in fo:
                    line_count += 1
            full_results.append( [f_item[i], line_count] )
        except Exception as e:
            print(e)
        i += 1
        total_line_count = (line_count + total_line_count)
        line_count = 0

    full_results.append(['Total files scanned:', len(f_item)])

    full_results.append(['Total lines:', total_line_count])

    return full_results

def file_most_recent_index(text, digit):
    dated_files = [(os.path.getmtime(fn), os.path.basename(fn)) 
               for fn in os.listdir(text) if fn.lower().endswith('.py')]
    dated_files.sort()
    dated_files.reverse()
    if dated_files:
        newest = dated_files[digit]
        return newest

def file_most_recent_list(text):
    dated_files = [(os.path.getmtime(fn), os.path.basename(fn)) 
               for fn in os.listdir(text) if fn.lower().endswith('.py')]
    dated_files.sort()
    dated_files.reverse()
    return dated_files

def file_size(path):
    if os.path.isfile(path):
        file_info = os.stat(path)
        return file_info.st_size

def file_size_total(path):
    bytes_count = 0
    i = 0
    for dirname, subdirlist, filelist in os.walk(path):
            for fname in filelist:
                    path_0 = os.path.join(dirname, fname)
                    siz_src = str(os.path.getsize(path_0))
                    siz_src_int = int(siz_src)
                    bytes_count = bytes_count + siz_src_int
                    i += 1
    return ['Files:', i, 'bytes:', bytes_count]

def file_size_total_list(path):
    full_list = []
    bytes_count = 0
    i = 0
    for dirname, subdirlist, filelist in os.walk(path):
            for fname in filelist:
                    path_0 = os.path.join(dirname, fname)
                    siz_src = str(os.path.getsize(path_0))
                    siz_src_int = int(siz_src)
                    bytes_count = bytes_count + siz_src_int
                    full_list.append([path_0, siz_src_int])
                    i += 1
    bytes_count_str = str(bytes_count)
    return full_list

# ------------------------- Images
def image_resize_hq(path, dest, x, y):
    if os.path.exists(path):
        image = Image.open(path)
        image.thumbnail((x, y), Image.ANTIALIAS)
        image.save(dest, quality=100)

# ------------------------- STRINGS
def NFD(text):
    return unicodedata.normalize('NFD', text)


def noCase(text):
    return NFD(NFD(text).casefold())



# ------------------------- LOGGING
def logW(text):
    # set file and file input
    file = './log/log.txt'
    var = '['+str(datetime.datetime.now())+'] '+text

    # create file if not exists
    makeD('./log/')
    makeF(file)

    # if file exists write entry
    if os.path.exists(file):
        with open(file, 'a') as fo:
            fo.write(var+'\n')
        fo.close()

def logP(text):
    # set file and file input
    file = './log/log.txt'
    var = '['+str(datetime.datetime.now())+'] '+text

    # create file if not exists
    makeD('./log/')
    makeF(file)

    # if file exists write log entry
    if os.path.exists(file):
        with open(file, 'a') as fo:
            p(var)
            fo.write(var+'\n')
        fo.close()

def logD():
    file = './log/log.txt'
    if os.path.exists(file):
        os.remove(file)

# ------------------------- CONFIGURATION FILES
def conOff(text):
    # set file and file input
    file = './data/config.txt'
    var = '['+str(datetime.datetime.now())+'] '+text

    # create file if not exists
    makeD('./data/')

    # if file exists write entry
    if os.path.exists(file):
        for line in fileinput.input(file, inplace=True):
            p(line.rstrip().replace(text+' ENABLED', text+' DISABLED')),

def conOn(text):
    # set file and file input
    file = './data/config.txt'
    var = '['+str(datetime.datetime.now())+'] '+text

    # create file if not exists
    makeD('./data/')

    # if file exists write entry
    if os.path.exists(file):
        for line in fileinput.input(file, inplace=True):
            p(line.rstrip().replace(text+' DISABLED', text+' ENABLED')),

def conMake(text):
    # set file and file input
    file = './data/config.txt'
    var = text

    # create file if not exists
    makeD('./data/')
    makeF(file)

    # if file exists write entry
    if os.path.exists(file):
        with open(file, 'a') as fo:
            fo.write(var+'\n')
        fo.close()

def conD(text):
    # set file and file input
    file = './data/config.txt'
    var = text

    # create file if not exists
    makeD('./data/')

    # if file exists write entry
    if os.path.exists(file):
        
        with open(file, 'r') as fo:
            for line in fo:
                line = line.strip()
                line_split = line.split(' ')
                if line_split[0] == str(text).strip():
                    p('removing configuration entry:', line_split[0])
        fo.close()

# ------------------------- POWER FILES
def cleanFile(text):
    # set file and file input
    file = text

    # if file exists write entry
    if os.path.exists(file):

        # read file
        line_ = []
        with open(file, 'r') as fo:
            for line in fo:
                line = line.strip()
                if line != '':
                    line_.append(line)
        fo.close()

        # write temporary file
        makeF(file+'.tmp')

        # check if tmp file exists
        success = False
        if os.path.exists(file+'.tmp'):
            for _ in line_:

                # write to temp
                with open(file+'.tmp', 'a') as fo:
                    fo.write(_+'\n')
                fo.close()

            # replace file contents with tmp contents
            os.replace(file+'.tmp', file)

            # check file exists after replace
            if os.path.exists(file):

                # initiate counter
                success_write = 0

                # check replacement file
                with open(file, 'r') as fo:
                    for line in fo:
                        line = line.strip()
                        if line in line_:
                            success_write += 1
                fo.close()
                if success_write == len(line_):
                    p('[cleanFile] cleaned file: success')
                    success = True

        if success is False:
            p('[cleanFile] cleaned file: failed')


# ------------------------- AUTOMATION
def lclick(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def start(text):
    app.Start(text)

def start_outline(text):
    app.Start(text)
    app.Notepad.draw_outline()

def app_activate(text):
    shell.AppActivate(text)

def type_keys(text):
    shell.TypeKeys(text, with_spaces = True)

def send_keys(text):
    SendKeys(text)

def block_input():
    ok = windll.user32.BlockInput(True)

def unblock_input():
    ok = windll.user32.BlockInput(False)

def get_foreground_window_pid():
    user32 = ctypes.windll.user32
    return user32.GetForegroundWindow()

def is_win_locked():
    process_name = 'LogonUI.exe'
    callall = 'TASKLIST'
    outputall = subprocess.check_output(callall)
    outputstringall = str(outputall)
    if process_name in outputstringall:
        return True
    else:
        return False

list_enumerate_open_windows = []
def _enumerate_open_windows_1(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    list_enumerate_open_windows.append([str(win32gui.GetWindowText(hwnd)), (x, y), (w, h)])

def enumerate_open_windows():
    time.sleep(1)
    win32gui.EnumWindows(_enumerate_open_windows_1, None)
    print('done')
    return list_enumerate_open_windows

# ------------------------- CONSOLE
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# ------------------------- KEYBOARD
def get_state_caps():
    vk_capital = 0x14
    return win32api.GetKeyState(vk_capital)

def get_state_numlock():
    vk_numlock = 0x90
    return win32api.GetKeyState(vk_numlock)

def get_state_numlock():
    vk_numlock = 0x90
    return win32api.GetKeyState(vk_numlock)

# ------------------------- CONVERSIONS
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if num < 1024.0:
            return ("%3.1f %s" % (num, x))
        num /= 1024.0

# ------------------------- OS
platforms_dictionary = {
            "Windows": {
                "open": 'ctypes.windll.WINMM.mciSendStringW(u"open H: type CDAudio alias L_drive", None, 0, None); ctypes.windll.WINMM.mciSendStringW(u"set L_drive door open", None, 0, None)',
                "close": 'ctypes.windll.WINMM.mciSendStringW(u"open H: type CDAudio alias L_drive", None, 0, None); ctypes.windll.WINMM.mciSendStringW(u"set L_drive door closed", None, 0, None)'
            },
            "Darwin": {
                "open": 'system("drutil tray open")',
                "close": 'system("drutil tray closed")'
            },
            "Linux": {
                "open": 'system("eject cdrom")',
                "close": 'system("eject -t cdrom")'
            },
            "NetBSD": {
                "open": 'system("eject cd")',
                "close": 'system("eject -t cd")'
            },
            "FreeBSD": {
                "open": 'system("sudo cdcontrol eject")',
                "close": 'system("sudo cdcontrol close")'
            }
        }
def get_platform():
    return platform_name()

# ------------------------- DISKS
def eject_cd_dvd(value):
    if platform_name() in platforms_dictionary:
        print('-- ejecting')
        try:
            if value == True:
                exec(platforms_dictionary[platform_name()]["open"])
            elif value == False:
                exec(platforms_dictionary[platform_name()]["close"])
        except Exception as e:
            print('-- eject: may have failed:', e)
            pass
    else:
        print("-- eject error: supported OS not found")


# ------------------------- NUMBERS
def is_prime(num):
    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               return False
       else:
           return True
    else:
       return False

# ------------------------- ENCRYPTION
class AESCipher:

    # Example encrypt:
    # cipher = AESCipher(bytes('&AR!i_XyxuBF+bVfURg`S&BgPfKx.?^=', 'utf-8'))
    # ciphertext = cipher.encrypt(str('foobar'))

    def __init__(self, KEY):
        self.key = KEY

        self.BS = 16
        self.pad = lambda s: bytes(s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS), 'utf-8')
        self.unpad = lambda s: s[0:-ord(s[-1:])]

    def encrypt(self, raw):
        try:
            raw = self.pad(raw)
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return base64.b64encode(iv + cipher.encrypt(raw))

        except Exception as e:
            print('AESCipher.encrypt:', e)

    def decrypt(self, enc):
        try:
            enc = base64.b64decode(enc)
            iv = enc[:16]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return self.unpad(cipher.decrypt(enc[16:])).decode('utf-8')

        except Exception as e:
            print('AESCipher.decrypt:', e)

# ------------------------- STRINGS
def rand_str_upper_digits(num):
    global iter_rand_num
    iter_rand_num = num
    chars=string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(iter_rand_num))

def list_encodings():
    communicator_codecs = encodings._aliases
    actual_codec = []
    for k, v in communicator_codecs.items():
        if v not in actual_codec:
            actual_codec.append(v)
    return actual_codec

# ------------------------- WMI
