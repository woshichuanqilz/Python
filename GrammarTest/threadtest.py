#!/usr/bin/python

import thread
import time

totalCnt = 0
# Define a function for the thread
def print_time( threadName, delay):
    global totalCnt
    count = 0
    while count < 5:
        totalCnt += 1
        time.sleep(delay)
        count += 1
        print "%s: %s : total Cnt %d" % ( threadName, time.ctime(time.time()), totalCnt )

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
  

ping 127.0.0.1 -n 6 > nul  print "Error: unable to start thread"

while 1:
   pass
