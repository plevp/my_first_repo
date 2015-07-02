import time
from threading import Thread
import random

'''
def myfunc(i):
    print "sleeping 5 sec from thread %d" % i
    time.sleep(5)
    print "finished sleeping from thread %d" % i
'''

l = [1,2,3,4,5,6,7,8,9,10]

def myfunc(i):
    for j in l:
        print str(i) + " " +str(j) + '\n';
        time.sleep(random.randint(0,3))

for i in range(3):
    t = Thread(target=myfunc, args=(i,))
    t.start()
