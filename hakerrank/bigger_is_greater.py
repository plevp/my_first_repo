#!/usr/bin/python

import sys

k = int(raw_input().strip())

for i in xrange(k):
    s = raw_input().strip()
    l = len(s)
    ls = list(s);
    done = False;
    for j in xrange(l-1, 0, -1):
        l = ls[j]
        p = ls[j-1]
        if ls[j-1] < ls[j]:
            done = True;
            ls1 = ls[j:]
            print ls1
            for k in xrange(len(ls1)-1, -1, -1):
               if ls[j-1] < ls1[k]:
                   ls[j-1], ls1[k] = ls1[k], ls[j-1]                   
                   print ls, ls1, j, k
                   break
            ls1.sort()
            
            print ''.join(ls[:j] + ls1)
            break;
    if done == False:
        print "no answer"
