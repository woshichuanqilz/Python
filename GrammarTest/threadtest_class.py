#!/usr/bin/python

import thread
import time

# Define a function for the thread
class mythread():
    totalCnt = 0
    def print_time(self, threadName):
       while count < 5:
          delay = 2
          time.sleep(delay)
          count += 1
          print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
    mt = mythread()
    thread.start_new_thread( mt.print_time, ("Thread-1") )
    thread.start_new_thread( mt.print_time, ("Thread-2") )
except:
   print "Error: unable to start thread"

while 1:
   pass
