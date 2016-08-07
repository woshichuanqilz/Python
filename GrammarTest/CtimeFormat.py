import datetime
import time

print time.ctime()
ftime = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
print datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
print ftime.day 
print ftime.year 
