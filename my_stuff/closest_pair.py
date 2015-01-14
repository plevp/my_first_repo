#!/usr/bin/python

import sys
import random
import my_pkg
import math

import time

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) **2 + (y1 - y2) **2)
    
def brute_force(points):
    mdist = float("inf")
    p1 = -1
    p2 = -1
    k = 0
    for i in range(1, len(points)):
        for j in range(0,i):
            k = k +1 
            d = dist(points[i], points[j])
            if d < mdist:
                p1, p2 = i,j
                mdist = d
    return mdist, p1,p2

def closest_pair(points):
    
    points_x = sorted(points, key= lambda tup : tup[0])
    points_y = sorted(points, key= lambda tup : tup[1])
    #print points_x
    #print points_y
    
    return closest_pair_r(points_x, points_y)

def closest_pair_r(points_x, points_y):
    if len(points_x) == 1:
        return (float("inf"), points_x[0],points_x[0])
    elif len(points_x) == 2:
        return (dist(points_x[0], points_x[1]), points_x[0],points_x[1])

    # # # # #

    ln = len(points_x)
    lnl = ln/2
    lnr = ln - lnl
    l_x = points_x[0:lnl]
    r_x = points_x[lnl:]
    l_y = sorted(l_x, key = lambda t: t[1])
    r_y = sorted(r_x, key = lambda t: t[1])
    
    d_l = closest_pair_r(l_x, l_y)
    d_r = closest_pair_r(r_x, r_y)

    #res =  d_l if d_l[0] < d_r[0] else d_r[0], d_r[1] + lnl, d_r[2] + lnl
    res = d_l if  d_l[0] < d_r[0] else d_r

    x_bar = l_x[-1][0];
    delta = res[0]

    s_y =[]
    for p in points_y:
        if abs(p[0] - x_bar) <= x_bar:
            s_y.append(p)

    mdelta = delta;
    p1 = -1; p2 = -1;
    
    if len(s_y) > 1:
        #print "s_y", s_y
        for j in range(len(s_y)-1):
            for i in range(j+1, min(j+8,len(s_y))):
                d = dist(s_y[i], s_y[j])                
                if d < mdelta:
                    # print "Xxx"
                    mdelta = d
                    p1 = j; p2 = i
        if mdelta < delta:
            res = (mdelta, s_y[p1], s_y[p2])
    #print  "closest_pair_r:", res
    return res
    
def doit():

    points = 10
    edge = 10
    #random.seed(1);

    if len(sys.argv) > 1:
        edge = int(sys.argv[1])
        if len(sys.argv) > 2:
            points = int(sys.argv[2])
    print "Hello", edge, points
    

    l = [ my_pkg.random_point(edge) for _ in range(points)]

    """
    l = 4* [0]
    l[0] = (10.0, 10.0)
    l[1] = (20.0, 20.0)
    l[2] = (21.0, 21.0)
    l[3] = (30.0, 30.0)
    """
    
    #print l[0], l[1], dist(l[0], l[1])

    #print l;    
    print "***********"

    print
    t0 = time.time()
    r = brute_force(l);
    print "Brute Force result", r, l[r[1]], l[r[2]]
    t1 = time.time()
    print "***********"

    r1 = closest_pair(l)
    print r1
    t2 = time.time()

    print "Times: ", t1 - t0, t2 - t1 

    if r[0] != r1[0]:
        print Error
    
if __name__ == '__main__':
    doit()
        
"""


"""
