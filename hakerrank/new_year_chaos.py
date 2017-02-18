#!/usr/bin/python


"""        
        if l[i] > i +1:
            r += (l[i] - i -1)
        for j in xrange(i+1, min(n, l[i] + 6)):
            if l[j]< l[i]:
                r +=1;
"""           
def invers(l):
    n =len(l);
    r = 0
    for i in xrange(n-1, -1, -1):
        if l[i] > i +3:
            return -1
        for j in xrange(max(0,l[i] -2), i):
            if l[j]> l[i]:
                r +=1;

    return r

def invers1(l):
    n =len(l);
    r = 0
    for i in xrange(n-1):
        if l[i] > i +3:
            return -1
        for j in xrange(i+1,n):
            if l[j]< l[i]:
                r +=1;
    return r




def doit():
    n = int(raw_input().strip())
    for __ in xrange(n):
        _ = int(raw_input().strip())
        l = map(int, raw_input().strip().split());

        ii = invers(l);
        if ii == -1:
            print "Too chaotic"
        else:
            print ii, invers1(l);
    
if __name__ == '__main__':
    doit()
