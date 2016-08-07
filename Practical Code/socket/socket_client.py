# client
from struct import *
import socket
import sys
import os



# address = ('127.0.0.1', 31500)
address = ('127.0.0.1', 8300)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

# pack a package here
s.send("just kidding")
data = s.recv(512)
if data == 'authentication success program start':
	print 'signal matched work start'
	os.system('RunP_exe.exe roger')
	
	
# print('the data received is',data)

s.close()
