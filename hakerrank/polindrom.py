#!/usr/bin/python

import sys

n = int(raw_input().strip())
for _ in xrange(n):
    c = 0
    s = raw_input().strip()
    l = len(s)
    j = l-1
    for i in xrange(l/2):
        oi = ord(s[i]);
        oj= ord(s[j])
        c  += abs(ord(s[i]) - ord(s[j]))
        j = j -1

    print c

