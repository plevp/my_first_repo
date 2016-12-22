#!/usr/bin/python
# -*- coding: utf-8 -*-

def doit():
    n = int(raw_input().strip())
    arr=list(map(int,raw_input().strip().split()))
    print arr;
    arr.sort();

    k_max = 0;
    k = 1;
    v = 0;
    print arr
    
    for i in xrange(n - 1):
        if arr[i+1] == arr[i]:
            k += 1
        else:
            if k > k_max:
                k_max = k;
                v = arr[i];
                print "v = ", v, "k_max = ", k_max
            k = 1
    if k > k_max:
        k_max = k;
        v = arr[n-1];
        
    print k_max, v
    print n - k_max

if __name__ == '__main__':
    doit()
    
