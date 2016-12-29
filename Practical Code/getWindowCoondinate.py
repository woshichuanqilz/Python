import win32gui
import re

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    title = win32gui.GetWindowText(hwnd)
    m = re.search(r"- Google Chrome", title)
    if m is not None:
        print "\t%s : Location: (%d, %d)" % (title, x, y)
        print "\t%s : Size: (%d, %d)" % (title, w, h)
        print "---------------"

def main():
    win32gui.EnumWindows(callback, None)

if __name__ == '__main__':
    main()
