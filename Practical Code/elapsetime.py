import threading
import time
from time import strftime
arg1=0
arg2=1
etc=2

# your function that takes a while.
# Note: If your function returns something or if you want to pass variables in/out,
# you have to use Queues
def yourFunction(arg1,arg2,etc):
    while processthread.isAlive():
        time.sleep(1) #your code would replace this
        elapsetime = time.clock() - starttime
        print str(int(elapsetime))
        # print strftime('%S', elapsetime)
    

# Setup the thread
processthread=threading.Thread(target=yourFunction,args=(arg1,arg1,etc)) #set the target function and any arguments to pass
processthread.daemon=True
processthread.start() # start the thread

starttime = time.clock()
time.sleep(1000)
#loop to check thread and display elapsed time
# while processthread.isAlive():
    # elapsetime = time.clock() - starttime
    # # print time.clock()
    # print elapsetime
    # time.sleep(10) # you probably want to only print every so often (i.e. every second)

print 'Done'
