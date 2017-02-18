#!/usr/bin/python

import sys


def foo(n, k, b):
    print "SSSSSS", n, k, b
    av = float(n)/b;
    av_1 = av+1

    if b * (b+1) / 2 > n:
        return -1
    if n > (k * b - (b * (b-1)/2)):
        return -1;

    l = list(range(1, b+1));
    print l
    s = b *(b+1)/2;
    d = (n -s) / b
    d2 = (n-s) % b
    print d, d2, s
    l = [  i + d for i in l]
    print l
    for j in xrange(len(l)-1, len(l)-1 -d2, -1):
        l[j] += 1
    return l
    
def doit():
    n = int(raw_input().strip())
    for _ in xrange(n):
        n, k, b = map(int, raw_input().strip().split());
        print foo(n, k, b);

    
if __name__ == '__main__':
    doit()
