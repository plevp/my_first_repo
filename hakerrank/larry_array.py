#!/usr/bin/python


def invers(l):
    n =len(l);
    r = 0
    for i in xrange(n-1):
        for j in xrange(i+1,n):
            if l[j]< l[i]:
                r +=1;
    return r
            
def doit():
    n = int(raw_input().strip())
    for __ in xrange(n):
        _ = int(raw_input().strip())
        l = map(int, raw_input().strip().split());
    
        if invers(l) % 2 == 1:
            print "NO"
        else:
            print "YES"
    
if __name__ == '__main__':
    doit()

    
