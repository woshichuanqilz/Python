#coding=utf-8
import subprocess
#This's a sample of operate the clipboard
 
# import win32clipboard as wincb
# import win32con
 
# wincb.OpenClipboard()
# wincb.EmptyClipboard()
# wincb.SetClipboardData(win32con.CF_TEXT, "Hello World!")  #复制文本内容到剪贴板，系统后台会返回内存地址
# # print wincb.GetClipboardData(win32con.CF_TEXT).encoding()  #'Hello World!'
# wincb.CloseClipboard()

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
copy2clip('lizhe clipboard test')


