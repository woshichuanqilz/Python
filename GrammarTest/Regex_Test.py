# encoding: utf-8
import re
# p = re.compile('ab*')
# m = p.match("abc")
# print m.group()
# p = re.compile('(?<=<strong>).*(?=</strong>)')
p = re.compile('ab*')
teststring = "abcc"
m = p.match(teststring)
print m.group()


