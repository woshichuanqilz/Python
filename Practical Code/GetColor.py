#coding:utf-8
from PIL import ImageGrab
from PIL import Image
import json
from pprint import pprint
import time
import sys
time.clock()
import sys  
# if len()
for i in range(len(sys.argv)):
    print "the para is %d : %s" % (i,sys.argv[i])
image = ImageGrab.grab()
print 'size of the image : height is %d, width is %d' % (image.height, image.width)
color = image.getpixel((int(sys.argv[1]), int(sys.argv[2])))
print color
print type(color)
print(time.clock())

sys.exit(72)


with open('data2.json') as data_file:    
    data = json.load(data_file)


print data["colorxy"][0]["x"]
