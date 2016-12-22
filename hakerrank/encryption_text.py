#!/usr/bin/python
from __future__ import print_function

import sys
import math

#s = raw_input().strip()
s = "chillout"

l = len(s)
r = int(math.sqrt(l))
c = r
if r * r < l:
    c = r+1 
    if c *r < l:
        r = r +1
    
print (c, r)

for ci in xrange(c):
    for ri in xrange(r):
        if (ri*c + ci) < l:
            print (s[ri*c+ci], end ="")
    print (" ", end = "")
print ("")

