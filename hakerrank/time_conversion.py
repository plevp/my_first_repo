#!/usr/bin/python

import sys

time = raw_input().strip()
t = time[:-2]
p = time[-2:]
if p == "AM" and t[:2] == "12":
    print "00" + t[2:];
elif p == "PM" and t[:2] == "12":
    print t;
elif p == "PM":
    print (str((int(t[:2]) + 12)))  + t[2:]
else:
    print t

