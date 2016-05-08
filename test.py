# client
from struct import *
import socket
import sys

# class
class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

def dicpara(dict):
    print(dict['Alice'])

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# dicpara(dict)


# pack a package here

pk1 = pack('BBH',1, 2, 3)
print "pk1"
print sys.getsizeof(pk1)
pk2 = pack('BB',1,2)
print "pk2"
print sys.getsizeof(pk2)

pk3 = 3
print "pk3"
print sys.getsizeof(pk3)

