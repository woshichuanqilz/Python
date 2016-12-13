# encoding: utf-8
import re
# p = re.compile('ab*')
# m = p.match("abc")
# print m.group()
# p = re.compile('(?<=<strong>).*(?=</strong>)')
p = re.compile('(ab*)')
teststring = "abccabb"
m = p.match(teststring)
print m.group(0)

# string replace
s = "start foo end"
# s = re.sub("foo.*", "replaced", s)
s = re.sub("foo|en", "replaced", s)
print s # output is 'foo repalced'

print '---------------------------'

s = "alpha.Customer[cus_Y4o9qMEZAugtnW] ..."
m = re.search(r"\[([A-Za-z0-9_]+)\]", s)
print m.group(1)
