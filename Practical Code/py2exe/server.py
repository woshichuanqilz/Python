# server

import socket

# address = ('127.0.0.1', 31500)
address = ('127.0.0.1', 8300)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = socket.socket()
s.bind(address)
s.listen(5)

while True:
    ss, addr = s.accept()
    print('got connected from',addr)

    # ss.send('byebye')
    ra = ss.recv(512)
    if ra == 'just kidding':
		ss.send('authentication success program start')
		print 'authentication success'
		break
		ss.close()
	

s.close()
