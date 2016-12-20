# client
from struct import *
import socket
import sys
import os



# address = ('127.0.0.1', 31500)
address = ('192.168.1.104', 8300)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

# pack a package here
s.send("Hello There!")
data = s.recv(512)
if data == 'authentication success program start':
	print 'signal matched work start'
	# os.system('RunP_exe.exe roger')
	
	
# print('the data received is',data)

s.close()
