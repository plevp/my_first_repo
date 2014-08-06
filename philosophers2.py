#!/usr/bin/python


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


THINKING_MIN = 3
THINKING_MAX = 13

EATING_MIN = 1 
EATING_MAX = 10


start_time  = time.gmtime();
start_m = start_time.tm_min
start_s = start_time.tm_sec

print "Starting time", start_m, start_s


def low_time():
    cur_time = time.gmtime();
    d = 0
    if (cur_time.tm_min < start_m) or ((cur_time.tm_min == start_m) and cur_time.tm_sec < start_s):
        d = 3600
    t  = d + (cur_time.tm_min - start_m) * 60 + ( cur_time.tm_sec -start_s)
    return (cur_time.tm_min, cur_time.tm_sec , t)
    
def mytime():

    cur_time = time.gmtime();
    d = 0
    if (cur_time.tm_min < start_m) or ((cur_time.tm_min == start_m) and cur_time.tm_sec < start_s):
        d = 3600
    t  = d + (cur_time.tm_min - start_m) * 60 + ( cur_time.tm_sec -start_s)
    
    (m,s,t) = low_time()
    #return '%2s:%2s[%3s] ' % (time.gmtime().tm_min,time.gmtime().tm_sec, t)
    return '%2s:%2s[%3s] ' % (m, s,  t)


class Philosopher(threading.Thread):

    running = True

    def __init__(self, xname, forkOnLeft, forkOnRight, thinking_time = None,  eating_time = None, delta = None):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
        self._thinking_time = thinking_time;
        self._eating_time = eating_time;
        self._delta = delta

    def mylog(self, s):
        sys.stdout.write("%s %s %s\n" % (mytime(), self.name, s))
        sys.stdout.flush()


    def run(self):
        if self._delta != None:
            time.sleep(self._delta)
            
        while(self.running):
            #  Philosopher is thinking (but really is sleeping).
            # sys.stdout.write( "%s %s leaves to think\n" % (self.name)
            # sys.stdout.flush()
            self.mylog('leaves to think.')
            if self._thinking_time == None:
                time.sleep( random.uniform(THINKING_MIN, THINKING_MAX))
            else:
                time.sleep(self._thinking_time)
            (_,_, t) = low_time()
            self._hungry_time = t
            self.mylog('is hungry.')
            #sys.stdout.flush()
            self.dine()
 #           sys.output.write"*****"
 #           sys.stdout.flush()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        k = 0;
        while True:
            # self.mylog('in dine')            
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break # go to eat
            fork1.release()
            k = k + 1
            self.mylog('swaps forks [' + str(k) + ',' + str(self._hungry_time) + ']')
            #sys.stdout.flush()
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        Philosopher.eating += 1;
        self.mylog ('starts eating.' + "[" + str(Philosopher.eating) + "]")
        
        #sys.stdout.flush()
        if self._eating_time == None:
            time.sleep(random.uniform(EATING_MIN, EATING_MAX))
        else:
            time.sleep(self._eating_time)
        Philosopher.eating -= 1;        
        self.mylog('finishes eating.')
        #sys.stdout.flush()

def DiningPhilosophers(the_time):
    Philosopher.eating = 0;
    forks = [threading.Lock() for _ in range(5)]
    philosopherNames = ('Aristotle','Kant','Buddha','Marx', 'Russel')

    philosophers= [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]
    
#     this is a problem of starvation of Kant
#     philosophers = [None] * 5
#     philosophers[0] = Philosopher(philosopherNames[0], forks[0], forks[1], 3,5,3)
#     philosophers[1] = Philosopher(philosopherNames[1], forks[1], forks[2], 7, 2, 0)
#     philosophers[2] = Philosopher(philosopherNames[2], forks[2], forks[3], 3,5,7)
#     philosophers[3] = Philosopher(philosopherNames[3], forks[3], forks[4], 200,2)
#     philosophers[4] = Philosopher(philosopherNames[4], forks[4], forks[0], 200,2)

#    random.seed(507129)
    seed = time.time()
    random.seed(seed)

    Philosopher.running = True

    print "We are staring with seed: ", seed

    for p in philosophers:
        p.daemon = True;     ## enable to work ctrl-C
        p.start()


    time.sleep(the_time)
    print "After sleeping:", the_time
    Philosopher.running = False
    for p in philosophers:
        p.join()

    print "Now we're finishing with seed: ", seed


def main():
    if len(sys.argv) == 1:
        the_time = 50
    else:
        the_time = int(sys.argv[1]);
    DiningPhilosophers(the_time)


if __name__  == '__main__':
    main()
