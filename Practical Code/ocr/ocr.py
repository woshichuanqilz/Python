from PIL import Image
from pytesser import *


image_file = 'myimage.tif'
image_file = 'phototest.tif'
image_file = 'helloworld.tif'
image_file = 'test1.tif'
im = Image.open(image_file)
text = image_to_string(im)
text = image_file_to_string(image_file)
text = image_file_to_string(image_file, graceful_errors=True)
print "=====output=======\n"
print text
