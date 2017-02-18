#!/usr/bin/python

import sys
from itertools import *


    
def doit():
    n,m = map(int,raw_input().strip().split())

    l = [map(int, raw_input().strip().split()[1:]) for _ in range(n)]
    iter = product(*l)

    def foo(*t):
        return sum(x * x for x in t) % m
    
    print max(starmap(foo, iter))
    
if __name__ == "__main__":
    doit()
