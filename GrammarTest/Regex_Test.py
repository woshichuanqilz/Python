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


# string replace
import re
s = "start foo end"
# s = re.sub("foo.*", "replaced", s)
s = re.sub("foo|en", "replaced", s)
print s # output is 'foo repalced'
