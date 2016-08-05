import os.path, time, inspect
# Get Current file directory
CurrentFilePath = os.path.abspath(inspect.stack()[0][1])

# Get the Create time here

print type(os.path.getmtime(CurrentFilePath))
print os.path.getmtime(CurrentFilePath)
print "last modified: %s" % time.ctime(os.path.getmtime(CurrentFilePath))
print "created: %s" % time.ctime(os.path.getctime(CurrentFilePath))
