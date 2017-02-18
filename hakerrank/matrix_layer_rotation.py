#!/usr/bin/python

import sys

def foo(m, n, s):
    s = s % ( 2* (n+m) - 4)
    i = 0; j = 0;
    if s == 0:
        i = 0; j = 0;
    elif s < m:
        i = s;
    elif s < m +n -1:
        i = m-1;
        j = s -m +1
    elif s < m + n +m -2:
        j = n -1;
        i = 2*m + n - s - 3;
    else:
        i = 0;
        j = 2*(m+n) -s -4
    return (i,j);

def bar(m, n, i, j):
    if j == 0 or i == m-1:
        return i + j
    else:
        return 2 *(m+n) - 4 - i - j
"""
for k in xrange(2 *(m+n) -4):
    i, j =  foo(4,5, k)
    print i, j
    print bar(4, 5, i, j);
"""

def print_a(a):
    for i in range(len(a)):
        print ' '.join(map(str, a[i]));

def doit():
    m, n, r = map(int, raw_input().strip().split(' '))
    print m, n, r
    a = []
    for i in xrange(m):
        a.append(map(int, raw_input().strip().split()));    
    print_a(a);
    b = [];
    for i in xrange(m):
        b.append(n *[0])

    o = 0
    mm = m;
    nn = n;
    while (True):
        for j in xrange(n):
            p = bar(m, n, 0, j) + r  
            i_n, j_n = foo(m, n, p);
            b[i_n+o][j_n+o] = a[0+o][j+o];        
            p = bar(m, n, m-1, j) +r    
            i_n, j_n = foo(m, n, p);
            b[i_n+o][j_n+o] = a[m-1+o][j+o];
        for i in xrange(1, m-1):
            p = bar(m, n, i, 0) +r  
            i_n, j_n = foo(m, n, p);
            b[i_n+o][j_n+o] = a[i+o][0+o]
            p = bar(m, n, i, n-1) +r    
            i_n, j_n = foo(m, n, p);
            b[i_n+o][j_n+o] = a[i+o][n-1+o]
        m = m - 2;
        n = n - 2;
        o += 1;
        if m == 0 or n == 0:
            break;
    
    print_a(b);
    
doit();
