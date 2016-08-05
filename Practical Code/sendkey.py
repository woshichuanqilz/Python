import win32com.client as comclt
wsh= comclt.Dispatch("WScript.Shell")
wsh.AppActivate("Notepad") # select another application
wsh.SendKeys("{enter}") # send the keys you want
wsh.SendKeys("{f1}") # send the keys you want
