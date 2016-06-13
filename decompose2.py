#!/usr/bin/python
#coding:utf-8
import sys   ##加载sys这个模块。
decomposeNum = (int)(sys.argv[1])
for num in range(0, 10):
    if decomposeNum & 2 ** num != 0:
        print 2 ** num
