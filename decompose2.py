#!/usr/bin/python
#coding:utf-8
import sys   ##加载sys这个模块。
for i in range(len(sys.argv)):
    print "第%d个参数是：%s" % (i,sys.argv[i])
