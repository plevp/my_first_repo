#!/usr/bin/python

from __future__ import print_function

import sys

def doit():
    def foo(x,y):
        if x.islower():
            if y.islower():
                return ord(x) - ord(y)
            else:
                return -1
        elif y.islower():
            return 1;
        elif x.isupper():
            if y.isupper():
                return ord(x) - ord(y)
            else:
                return -1
        elif y.isupper():
            return 1;
        elif x.isdigit() and int(x) % 2 == 1:
            if y.isdigit() and int(y) % 2 == 1:
                return ord(x) - ord(y)
            else:
                return -1
        elif y.isdigit() and int(y) % 2 == 1:
            return 1
        elif x.isdigit() and int(x) % 2 == 0:
            if y.isdigit() and int(y) % 2 == 0:
                return ord(x) - ord(y)
            else:
                return -1
        else:
            return 0
                    
    s = raw_input().strip()
    s1 = sorted(s, cmp = foo);

    print (*s1,sep='')
    #print  ''.join(sorted(s, cmp = foo))

if __name__ == "__main__":
    doit()
