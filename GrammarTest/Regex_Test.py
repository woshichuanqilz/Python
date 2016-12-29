# encoding: utf-8
import re
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
m = re.search(r"xxxx", s)
if m is not None:
    print m.group(1)


# If And Search By The Regex
s = '98787This is correct'
for words in ['This is correct', 'This', 'is', 'correct']:
    if re.search(r'\b' + words + r'\b', s):
        print('{0} found'.format(words))


print "__________string replace__________"
cmdString = "What do you like, done"
cmdString = re.sub(r"[^a-zA-Z]+DONE.{0,1}$", "", cmdString, flags=re.IGNORECASE)
print cmdString # output is 'foo repalced'
