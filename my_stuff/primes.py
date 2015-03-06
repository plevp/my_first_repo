#!/usr/bin/python

import math
import sys

def primes(n):
    print "Hello", n
    l = list(range(2, n+1))
    
    p = 1;
    while ( p <= math.sqrt(n)):
        p = next (x for x in l if x > p)        
        l = [x for x in l if x % p != 0 or x == p]
    return l
        
if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
    except:
        print "Not a number"
        sys.exit();
    print len(primes(n))





