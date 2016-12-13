import os.path, time, inspect
# Get Current file directory
CurrentFilePath = os.path.abspath(inspect.stack()[0][1])

# Get the Create time here
print type(os.path.getmtime(CurrentFilePath))
print os.path.getmtime(CurrentFilePath)
print "last modified: %s" % time.ctime(os.path.getmtime(CurrentFilePath))
print "created: %s" % time.ctime(os.path.getctime(CurrentFilePath))

## dd/mm/yyyy format
print (time.strftime("%Y%m%d"))

print time.strftime('%Y%m%d', time.gmtime(os.path.getmtime(CurrentFilePath)))

# Reference url https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
