#!/usr/bin/python

import sys
import re

def foo(m):
    return 'or if m.groups(0) == '|| else 'and'

def doit():
    n = int(raw_input().strip())
    l = [raw_input().strip() for _ in xrange(n)]
    print l

    for x in l:
        re.sub(r'\|\'
    


if __name__ == "__main__":
    doit()
