#!/usr/bin/python

import sys

def wrapper(f):
    def fun(l):
        f(['+91' + ' ' + i[-10:-5] + ' ' + i[-5:] for i in l])
    return fun


@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

def doit():
    l = [raw_input() for _ in range(int(raw_input().strip()))]
    sort_phone(l)

if __name__ == "__main__":
    doit()
