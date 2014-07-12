import threading
import random
import time
import datetime
import sys


# Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.
#
# Deadlock is avoided by never waiting for a fork while holding a fork (locked)
# Procedure is to do block while waiting to get first fork, and a nonblocking
# acquire of second fork.  If failed to get second fork, release first fork,
# swap which fork is first and which is second and retry until getting both.
#
# See discussion page note about 'live lock'.

def mytime():
    return '%s:%s ' % (time.gmtime().tm_min,time.gmtime().tm_sec)

class Philosopher(threading.Thread):



    running = True

    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def mylog(self, s):
        sys.stdout.write("%s %s %s\n" % (mytime(), self.name, s))
        sys.stdout.flush()


    def run(self):
        while(self.running):
            #  Philosopher is thinking (but really is sleeping).
            # sys.stdout.write( "%s %s leaves to think\n" % (self.name)
            # sys.stdout.flush()
            self.mylog('leaves to think.')
            time.sleep( random.uniform(3,13))
            self.mylog('is hungry.')
            #sys.stdout.flush()
            self.dine()
 #           sys.output.write"*****"
 #           sys.stdout.flush()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while True:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            self.mylog('swaps forks.')
            #sys.stdout.flush()
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        self.mylog ('starts eating.')
        #sys.stdout.flush()
        time.sleep(random.uniform(1,10))
        self.mylog('finishes eating.')
        #sys.stdout.flush()

def DiningPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('Aristotle','Kant','Buddha','Marx', 'Russel')

    philosophers= [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) \
            for i in range(5)]

#    random.seed(507129)
    seed =time.time()
    random.seed(seed)

    Philosopher.running = True

    print "We are staring with seed: ", seed

    for p in philosophers: p.start()
    time.sleep(100)
    print "After sleep(100)"
    Philosopher.running = False
    for p in philosophers: p.join()
    print "Now we're finishing with seed: ", seed

DiningPhilosophers()
