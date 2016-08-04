d = {}
with open("file.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[int(key)] = val

for key, value in d.iteritems():
    print str(key) + ' is ' + d[key]
