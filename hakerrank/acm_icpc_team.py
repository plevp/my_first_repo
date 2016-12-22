#!/usr/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)

c_max = 0;
k_max = 0;
for i in xrange(n-1):
    ti = topic[i]
    for j in xrange(i+1, n):
        tj = topic[j]
        c = 0;
        for k in xrange(m):
            if ti[k] == '1' or tj[k] == '1':
                c += 1
        if c > c_max:
            c_max = c
            k_max = 1
        elif c == c_max:
            k_max += 1
        else: 
            pass
print c_max
print k_max

"""
4 5
10101
11100
11010
00101
"""

