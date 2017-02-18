#!/usr/bin/python

import sys

def doit():
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    l1 = len(s1)
    l2 = len(s2)
    a = [[0]*(5001) for i in range(5001)]
    for i in xrange(0,l1):
        for j in xrange(0,l2):
            if(s1[i]==s2[j]):
                a[i+1][j+1] = a[i][j]+1
            else:
                a[i+1][j+1] = max(a[i+1][j],a[i][j+1])
    print(a[l1][l2])
 
    pass

if __name__ == "__main__":
    doit()
