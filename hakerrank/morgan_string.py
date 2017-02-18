#!/usr/bin/python

import sys

def bar(l):
    i = len(l) - 1;
    k = 0;
    while (i >= 0 and l[i] == 'Z'):
        i -= 1
        l.pop()
        k += 1;
    return k
    
def foo(s1, s2):
    l = []
    res = ''
    if len(s1) == 0:
        res = s1;
    elif len(s2) == 0:
        res = s2;
    else:
        l1 = list(s1)
        l2 = list(s2)
        # print l1
        # print l2
        k = bar(l1) + bar(l2);
        l1 = l1[::-1]
        l2 = l2[::-1]
        # print l1
        #  print l2
        while (len(l1) > 0 or len(l2) > 0):

            i1 = len(l1) - 1;
            i2 = len(l2) - 1;
            if len(l1) == 0 and len(l2) == 0:
                break;
            b = ''
            while(i1 >=0 and i2>=0 and l1[i1] == l2[i2]):
                i1 -= 1;
                i2 -= 1;
                b = l1[i1]
            if i1 >= 0 and i2 >= 0:
                c1 = l1[i1];
                c2 = l2[i2]
                if c1 < c2:
                    l.append(l1.pop());
                    while len(l1) and l1[-1] == b:
                        l.append(l1.pop());
                        # i1 -=1
                else:
                    l.append(l2.pop());
                    while len(l2) > 0 and l2[-1] == b:
                        l.append(l2.pop());
                        # i2 -=1                    
            elif i1 < 0 and i2 < 0:
                l.append(l2.pop())
            elif i1 < 0:
                l.append(l2.pop())
            else: # i2 == 0
                l.append(l1.pop())
                # print l;
        for j in xrange(k):
            l.append('Z');
    res = ''.join(l)        
    return res    
        
def doit():
    n = int(raw_input().strip())

    for _ in range(n):
        s1 = raw_input().strip()
        s2 = raw_input().strip()
        print foo(s1,s2);


if __name__ == "__main__":
    doit()
