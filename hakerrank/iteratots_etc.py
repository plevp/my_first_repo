#!/usr/bin/python

import sys
from itertools import *

def doit():
    n = int(raw_input().strip())
    l = raw_input().strip().split()
    k = int(raw_input().strip())

    #print n,k
    #print l        

    cs = combinations(range(len(l)), k);
    good = 0
    count = 0
    for i in cs:
        count += 1
        for j in i:
            if l[j] == 'a':
                good += 1
                break;

    print("%.3f" % (float(good)/count))
    
    
if __name__ == "__main__":
    doit()
