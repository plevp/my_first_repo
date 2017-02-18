#!/usr/bin/python

import sys

def dset_find(arr, id):
    r = arr[id];
    while r[0] != r[1]: 
        r = arr[r[1]];
    return r[0];
    
def dset_union(arr, id1, id2):
    r1 = dset_find(arr, id1)
    r2 = dset_find(arr, id2)
    if r1 == r2:
        print "already done", id1, id2
        return;
    i1 = arr[r1]
    i2 = arr[r2]

    if i1[2] < i2[2]:
        arr[r1] = (i1[0], r2, i1[2], i1[3])
        arr[r2] = (i2[0], i2[1], i2[2], i2[3] + i1[3])
    elif i1[2] > i2[2]:
        arr[r2] = (i2[0], r1, i2[2], i2[3])
        arr[r1] = (i1[0], i1[1], i1[2], i1[3] + i2[3])
    else:
        arr[r2] = (i2[0], r1, i2[2], i2[3])
        arr[r1] = (i1[0], i1[1], i1[2] +1, i1[3]+i2[3])

def doit():
    
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    N,l = map(int,raw_input().split())
 
    arr = []
    for i in xrange(N):
        arr.append((i, i, 0,1))
    
    for i in xrange(l):
        a,b = map(int,raw_input().split())
        # Store a and b in an appropriate data structure
        if i == 57:
            #print a,b
            #print arr[a], arr[b]            
            print arr;
        r1 =dset_find(arr, a)
        r2 =dset_find(arr, b)
        print a,r1,b, r2
        print arr[r1], arr[r2];
        dset_union(arr,a,b);
        print arr[r1], arr[r2];
        print arr[2], arr[3], arr[9], arr[35], arr[50], arr[55]
        
    n = []
    for i in arr:
        if i[0] == i[1]:
            n.append(i[3]);

    s = 0; p = 0
    if len(n) < 2:
        pass
    else:    
        for i in xrange(len(n)-1):
            s = s+n[i]
            p = p + s * n[i+1]
                
    print p

if __name__ == "__main__":
    doit()



######### testcase 3:  499175
###################4   3984
