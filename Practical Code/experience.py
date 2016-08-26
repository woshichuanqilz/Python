#coding=UTF-8
import os
import sys
import random


# print sys.argv[1]

# a = int(sys.argv[1])
# b = int(sys.argv[2])
cnt = 0

while cnt < 10:
    a = random.randint(1, 100)  # Integer from 1 to 10, endpoints included
    b = random.randint(1, a)  # Integer from 1 to 10, endpoints included

    while True:
        c = a % b
        if c == 0:
            break
        if c > b:
            c = c - b
        else:
            c = b - c
        a = b
        b = c

    print 'final :a = ' + str(a) + ' b = ' + str(b) + ' c = ' + str(c)
    cnt = cnt + 1

