#coding:utf-8
from PIL import ImageGrab
from PIL import Image
import json
from pprint import pprint
import time
import sys
import win32com.client as comclt
import datetime


# Hex to Decimal
_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'

def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]
def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)
image = ImageGrab.grab()

color = image.getpixel((int(sys.argv[1]), int(sys.argv[2])))
print triplet(color)
if triplet(color) == str(sys.argv[3]):
    print 'Get It'
    exit(1)
print 'miss it'
exit(0)
