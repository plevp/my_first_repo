#!/usr/bin/python

s = raw_input().strip()
#s = "aabbcd"

d = 26 * [0]
 
for i in xrange(len(s)):
    d[ord(s[i]) - ord('a')] += 1

print d;
s = set(d)
if 0 in s:
    s.remove(0)

l = list(s)
if len(l) == 1:
    print "YES"
elif  len(l) == 2 and l[1] == l[0] +1 and d.count(l[1]) == 1:
    print "YES"
else:
    print "NO"

