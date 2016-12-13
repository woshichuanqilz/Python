x = [1, 2, 3]
y = [4, 5, 6, 7]
z = ['lizhe', 'mazi']
zipped = zip(x, y)
print zipped


x2, y2 = zip(*zipped)
x == list(x2) and y == list(y2)

print 'unzip'
print x
print y

print 'Smile'
zipped2 = zip(x, z)
print zipped2
print [list(row) for row in zip(*zipped2)]
print [row for row in zip(*zipped2)]
