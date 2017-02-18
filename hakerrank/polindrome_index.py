#!/usr/bin/python

import sys

def if_polindrom(s):
    j = len(s) -1;
    for i in xrange(len(s)/2):
        if s[i] != s[j]:
            return False;
        j = j-1
    return True;



print if_polindrom("aa")

"""    
n = int(raw_input().strip())
for _ in xrange(n):
    res = -1
    s = raw_input().strip()
    l = len(s)
    j = l-1
    for i in xrange(l/2):
        if s[i] != s[j]:
            if s[i+1] == s[j] and if_polindrom(s[i+1:j +1]):
                res = i
            else:
                res = j
            break;
        j = j -1

    print res
"""
