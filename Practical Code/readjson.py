import json
import time
import win32com.client as comclt

wsh= comclt.Dispatch("WScript.Shell")
wsh.SendKeys("{enter}") # send the keys you want

time.sleep(10)

with open('colorxy.json') as data_file:    
    data = json.load(data_file)
for colorxyitem in data["colorxy"]:
    for i in xrange(len(colorxyitem["sendkey"])):
        # print 'key is ' + colorxyitem["sendkey"][i]
        sendcmd = colorxyitem["sendkey"][i]
        wsh.SendKeys(sendcmd) # send the keys you want

print len(data["colorxy"])
print data["colorxy"][0]["x"]



