# client
from struct import *
import socket
import sys

# address = ('127.0.0.1', 31500)
address = ('127.0.0.1', 8300)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

# pack a package here

pk = pack('BBHHH',
          5, # socket version
          2, # check code
          8, # package size
          4, #
          5)  # socket version , check code, package size
print sys.getsizeof(pk)
s.send(pk)
# data = s.recv(512)
# print('the data received is',data)


s.close()
