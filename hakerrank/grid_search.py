#!/usr/bin/python

import sys


t = int(raw_input().strip())
print t
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    print R, C
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
       print G_t
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    print r,c 
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
       print P_t

    found = False
    print (R-r)
    for i in xrange(R-r+1):
        ind = 0
        while (True):
            #print "ind =", ind
            #print G[i]
            ind_ = G[i][ind:].find(P[0]);
            found = False
            if ind_ >= 0:
                ind = ind + ind_
                #print "ind =", ind
                found = True
                for j in xrange(1, r):
                    if G[i+j][ind: ind+c] != P[j]:
                        found = False
                        ind += 1
                        break;
                if found:
                    break;
            else:
                break;
            if found:
                break;
        if found:
            break;
            
            
    if found:
        print "YES"
    else:
        print "NO"


