#coding:utf-8
from PIL import ImageGrab
from PIL import Image
import time
import sys
time.clock()
import sys  
for i in range(len(sys.argv)):
    print "the para is %d : %s" % (i,sys.argv[i])
image = ImageGrab.grab()
color = image.getpixel((int(sys.argv[1]), int(sys.argv[2])))
print color
print type(color)
print(time.clock())

sys.exit(72)
