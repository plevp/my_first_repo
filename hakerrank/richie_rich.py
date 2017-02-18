#!/usr/bin/python

import sys

def foo(s,k):
    j = len(s) -1;
    res = 0
    p = 0;
    for i in xrange(len(s)/2):
        if s[i] == s[j]:
          pass  
        else:
            p = p+1
        if p > k:
            res = -1;
            break;
        j = j-1
    if res == 0:
        j = len(s) -1;
        for i in xrange(len(s)/2):
            if s[i] == s[j]:
                if s[i] == '9':
                    pass
                elif k > p+1:
                    s[i] = '9'
                    s[j] = '9'
                    k = k-2                    
                else:
                    pass;
            else:   ### !=
                p = p-1
                k = k-1
                if s[i] == '9':
                    s[j] = '9'
                elif s[j] =='9':
                    s[i] = '9'
                else:
                    if k > p:
                        s[i] = '9'
                        s[j] = '9'
                        k = k-1
                    elif s[i] > s[j]:
                        s[j] = s[i]
                    else:
                        s[i] = s[j]
            j = j-1
    if k > 0 and (len(s) % 2) == 1:
        s[len(s)/2] = '9'
    if res == 0:
        return ''.join(s)
    return -1


def doit():
    n,k = map(int, raw_input().strip().split())
    s = raw_input().strip()
    print foo(list(s), k);
    

if __name__ == "__main__":
    doit()
