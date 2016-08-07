# client
from struct import *
import socket
import sys
import os
import thread
import time
import inspect

# name judgement
# filename = os.path.basename(__file__)
# filename = filename.replace(".py", "")
# if filename != "wherecho.exe":
	# print 'wrong product name'
	# print filename
	
	# sys.exit(1)
	

filename = inspect.stack()[0][1]
filename = filename.replace(".py", "")	

if filename != "wherecho":
	print 'wrong product name'
	print filename
	
	sys.exit(1)	
def start_server( threadName, delay):
   os.system('server.exe')


   
# Create two threads as follows
thread.start_new_thread( start_server, ("Thread-1", 2, ) )
time.sleep(1)

print 'already start'

# address = ('127.0.0.1', 31500)
address = ('127.0.0.1', 8300)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

# pack a package here
s.send("just kidding")
data = s.recv(512)
if data == 'authentication success program start':
	print 'signal matched work start\n'
	rv = os.system('RunP_exe.exe roger')
	# print rv
	
# print('the data received is',data)

s.close()
