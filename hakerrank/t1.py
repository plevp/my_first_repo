#!/usr/bin/python

import sys

def doit():
    n,m = map(int, raw_input().split())

    l=[]
    #for _ in range(n):
    #    l.append([int(i) for i in raw_input().split()])
    l =  [[int(i) for i in raw_input().split()] for _ in range(n)]
    print l;
    
if __name__ == "__main__":
    doit()
