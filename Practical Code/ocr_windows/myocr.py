import os
import re
import sys
import win32gui
import subprocess
import pyscreenshot as ImageGrab

global WindowX
global WindowY
global WindowW
global WindowH

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    title = win32gui.GetWindowText(hwnd)
    m = re.search(r"^Total Commander$", title)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y

    global WindowX
    global WindowY
    global WindowW
    global WindowH

#   Assign the value
    if m is not None and h != 0:
        WindowX = rect[0]
        WindowY = rect[1]
        WindowW = rect[2] - WindowX
        WindowH = rect[3] - WindowY
        print "\t%s : Location: (%d, %d)" % (title, WindowX, WindowY)
        print "\t%s : Size: (%d, %d)" % (title, WindowW, WindowH)
        print "---------------"

if __name__ == '__main__':
    WindowX = 0
    WindowY = 0
    WindowW = 0
    WindowH = 0

    win32gui.EnumWindows(callback, None)
    # part of the screen
    print str(WindowX)+ " " + str(WindowY) + " " + str(WindowW) + " " + str(WindowH)

    #Extend distance
    x1 = 140
    y1 = 221
    x2 = 343
    y2 = 247
    print str(WindowX + x1)+ " " + str(WindowY + y1) + " " + str(WindowX + x2) + " " + str(WindowY + y2)

    im=ImageGrab.grab(bbox=(WindowX + x1,WindowY + y1,WindowX + x2, WindowY + y2)) # X1,Y1,X2,Y2
    im.save('screencapture.png', 'png')
#-#
    os.system("tesseract.exe screencapture.png ocrres")
    os.system("clickButton.exe")

