#!/usr/bin/python

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
k = k % n


for a0 in xrange(q):    
    m = int(raw_input().strip())
    if m >= k:
        print a[m-k]
    else:
        print a[n-(k-m)]
