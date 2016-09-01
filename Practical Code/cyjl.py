#-*- coding: utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"



with open('idiom.txt') as f:
    lines = f.read().splitlines()
for line in lines:
    # line = line.decode('utf-8')
    linegbk = line.decode('gbk')
    print '-------------------------'
    print linegbk[0]
    print linegbk[1]
    # print type(line)
    # print len(line)
    # print line[0:2]
    # print '---'
    # whatisthis(line)
