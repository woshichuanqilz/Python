# -*- coding: utf-8 -*-
str = "请将文件拖曳到本脚本！".decode('utf-8').encode('gbk')
print len(str)
print str[0:3]
print "请将文件拖曳到本脚本！".decode('utf-8').encode('gbk')
print "请将文件拖曳到本脚本！"
print "李哲"
    

###########
# -*- coding: utf-8 -*-
utf8string = "\u64cd\u4f5c\uff1b\u8fd0\u8f6c\uff1b\u7ecf\u8425\uff1b\u884c\u52a8\uff1b\u624b\u672f\uff1b\u8fd0\u7b97\uff1b\u751f\u6548\uff1b\uff08\u590d\uff09\u8fd0\u7b79\u5b66"
plainstring1 = unicode(utf8string, "utf-8")
print(plainstring1)


def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"

a = '李哲'
b = u'李哲'
a = a.decode('utf-8')
whatisthis(a)
whatisthis(b)


#######

# -*- coding: utf-8 -*-
import urllib
import sys
def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"

UniStr = '\u4e11\u6367\u5fc3'.decode('unicode_escape')
print UniStr

# print sys.argv[0]
# print sys.argv[1]
# # a = u'里'
# # whatisthis(sys.argv[1])
# sys.argv[1].decode('ascii').encode('utf-8')
# ctt = urllib.quote(a.encode('gb2312'))
# url = 'http://chengyu.t086.com/chaxun.php?q1=' + ctt + '&q2=&q3=&q4='
# print url
