#!/usr/bin/python

import sys

def foo(s):
    d = {'A':0, 'C':0, 'T':0, 'G':0};
    for i in xrange(len(s)):
        d[s[i]] += 1
    return d;

def doit():
    n = int(raw_input().strip())
    s = raw_input().strip()
    n = len(s)
    print s
    m = n/4
    #l2i = {'A':0, 'C':1, 'T':2, 'G':3};
    #i2l = {0:'A', 1:'C', 2:'T', 3:'G'};
    d = foo(s);
    st = set();
    k = 0
    print n, d, m
    for i in ['A', 'C', 'T', 'G']:
        d[i] -= m
        if d[i] > 0:
            k += d[i]
            st.add(i)
    print d
    print st
    if k == 0:
        print 0;
        return;

    i = 0
    while s[i] not in st:
        i += 1
    start = i;
    
    p = 0;
    d1 = d.copy();
    while p < k and  i < len(s):
        if s[i]  in st:
            if d1[s[i]] > 0:
                p += 1
            d1[s[i]] -= 1
        i += 1

    print "k, p ", k, p
    print d1
    best_start = start
    best_end = i-1;
    best_len = best_end-best_start+1
    
    l = best_len
    print "best_len", best_len
    
    while (i < len(s)):
        j = start;
        print "0. p, j, i ", p, j,i
        print d1
        while j < len(s) and s[j] in st and p > 0:
            if d1[s[j]] >= 0:
                  p -= 1            
            d1[s[i]] +=1
            j += 1
        print "0.1  p, j, i ", p, j,i
        print d1
        while j < len(s) and s[j] not in st:
            j += 1
        print "1. p, j, i ", p, j,i
        if j == len(s):
            break;
        while p < k and i < len(s):
            if s[i]  in st:
                if d1[s[i]] > 0:
                    p += 1
                    d1[s[i]] -= 1                
            i += 1
        print "2. p, j, i", p, j, i
        if p < k:
            break;
        else:
            start = j
            print "best_len", best_len, i - j -1
            if i - j    < best_len:
                best_start = j
                best_end = i-1;
                best_len = best_end-best_start+1
                
    print best_start, best_end, best_len
    
if __name__ == "__main__":
    doit()
