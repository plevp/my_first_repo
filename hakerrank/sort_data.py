#!/usr/bin/python

import sys

def doit():

    n, m = [int(x) for x in raw_input().split()]
    l = []
    for _ in xrange(n):
        t = [int(x) for x in raw_input().split()]
        l.append(t)
    k = int(raw_input().strip())
    
    # print n,m,k

    # print l

    
    r = sorted(l, key = lambda x: (x[k]))
    for y in r:
        print ' '.join([str(x) for x in y])
                        
         
if __name__ == "__main__":
    doit()
