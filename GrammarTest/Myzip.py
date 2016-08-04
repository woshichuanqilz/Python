x = [1, 2, 3]
y = [4, 5, 6, 7]
zipped = zip(x, y)
zipped

print 'zip'
print zipped
x2, y2 = zip(*zipped)
x == list(x2) and y == list(y2)

print 'unzip'
print x
print y
