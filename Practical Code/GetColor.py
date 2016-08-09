#coding:utf-8
from PIL import ImageGrab
from PIL import Image
import json
from pprint import pprint
import time
import sys
import win32com.client as comclt
import datetime

# Time Lock
import datetime
now = datetime.datetime.now()
if 5 != now.day:
    print "time lock active"
    sys.exit(1)

# para rectify
# if len()

# Init WScript
wsh= comclt.Dispatch("WScript.Shell")

# Init Logger File 
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('colorxy.log')
fh.setLevel(logging.DEBUG)
# Enable Or Disable The Logger
# logger.disabled = True
# Format The Logger
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Hex to Decimal
_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'

def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]
def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)

#  read the json file
with open('colorxy.json') as data_file:    
    data = json.load(data_file)

image = ImageGrab.grab()

for colorxyitem in data["colorxy"]:
    color = image.getpixel((int(colorxyitem["x"]), int(colorxyitem["y"])))
    # print type(triplet(color))
    # print type(str(colorxyitem["pos"]))
    # print triplet(color)
    # print str(colorxyitem["pos"])
    if triplet(color) == str(colorxyitem["pos"]):
        for i in xrange(len(colorxyitem["sendkey"])):
            # print 'key is ' + colorxyitem["sendkey"][i]
            # print 'go send key'
            sendcmd = colorxyitem["sendkey"][i]
            wsh.SendKeys(sendcmd) # send the keys you want



# print rgb('3200AD')
# print triplet()


#######################################
    # print 'x = ' + colorxyitem["x"]
    # print 'y = ' + colorxyitem["y"]
    # print color
    # print type(color)
# print data["colorxy"][0]["x"]
# print 'size of the image : height is %d, width is %d' % (image.height, image.width)
# print color
# print type(color)
# put the dec to hex
# for i in xrange(1, 20 , 2):
    # color = image.getpixel((i * 10, i * 5))
    # print triplet(color)

