#!/usr/bin/python

from __future__ import print_function

import sys

#from = int(raw_input(),strip())
#to = int(raw_input(),strip())

frm = 1
to =  1


def foo(n):
    n2 = n**2
    s = '0' + str(n2)
    for j in xrange(1, len(s)):
        s1 = s[:j]
        s2 = s[j:]
        ns2 = int(s2);
        if ns2 > 0 and int(s1) + ns2 == n:
            print(n, n2, s1, s2, "\n")
            return True;
    return False

"""
for n in xrange(frm, to+1):
    if foo(n):
        print(n, end= " ")
"""
foo(5292)
foo(4879)
foo(7272)
foo(38962)
foo(17344)

print ("")

    

