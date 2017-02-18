#!/usr/bin/python

import sys

n = int(raw_input().strip())

s = []
all = set()
count = 0
for _ in xrange(n):
    str = raw_input().strip()
    t = set(str)
    s.append(t)
    all.update(t)


print all
print s

for c in all:
    d = True
    for i in xrange(n):
        if c not in s[i]:
            d = False;
            break;
    count += d
print count

