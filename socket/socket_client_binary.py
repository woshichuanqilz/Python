import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8300)
sock.connect(server_address)

values = (1, 2, 3)
packer = struct.Struct('B B !H')
packed_data = packer.pack(*values)

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % binascii.hexlify(packed_data), values
    sock.sendall(packed_data)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()