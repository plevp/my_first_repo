#!/usr/bin/python

import sys

def print_a(a):
    for i in range(len(a)):
        print ' '.join(map(str, a[i]));
        
def doit():
    q = int(raw_input().strip())
    for q_ in xrange(q):
        n = int(raw_input().strip())
        a = []
        m = n*2
        for i in xrange(m):
            a.append(map(int, raw_input().strip().split()));

        res = 0;
        for i in xrange(n):
            for j in xrange(n):
                res += max(a[i][j], a[i][m - j -1] , a[m-i-1][ j], a[m-i-1][ m-j-1])
        print res
        

if __name__ == "__main__":
    doit()

            
