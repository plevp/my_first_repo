#!/usr/bin/python

import sys

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass

def doit():

    x = [raw_input().strip() for _ in xrange(int(raw_input().strip()))]
         
    d = OrderedCounter(x)
    
    print d
    
    print(len(d))
    print ' '.join(map(str, d.values()))

if __name__ == "__main__":
    doit()

