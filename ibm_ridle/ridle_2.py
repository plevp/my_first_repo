#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
import random
import sys

def check1():
    for s in all:
        if len(s) != 6:
            print s;
            print "Error 1 ";
            exit_

N = 25
whole = set(range(32));
err_list = [0]* N

def calc_err(s1, s2):
    return abs(len(s1.intersection(s2)) -1);

def max_index(old):
    
    m = 0;
    i = 0;
    for j in err_list:
        if j > m and  i != old:
            m = j
            mi = i;
        i += 1

    return [j for j in range(N) if err_list[j] == m]
    
def all_errs():
    for i in range(N):
        #print i;
        err_list[i] = 0;
        for j in range(N):
            if (i != j):
                e = calc_err(all[i], all[j]);
                #print i, j, e;
                err_list[i] += e

#all = [set()] * N
all  = [];

def try_one(ind):
    r = [];
    s =  all[ind]
    p = whole - s;
    #print p
    for v in all[ind]:
        s1 = s - set([v])
        for u in p: 
            s2 = set(s1);
            s2.add(u);
            e = 0;
            all[ind] = s2;

            all_errs();
            '''            
            for j in range(N):
                if  j != ind:
                    e += calc_err(s2, all[j]);
            '''
            all[ind] = s;
            r.append((v, u, sum(err_list)));
    return r;
            
def doit():
    global all;
    all.append(set(range(0,6)))
    all.append(set([ 0,  7,  8,  9, 10, 11]));
    all.append(set([ 0, 12, 13, 14, 15, 16]));
    all.append(set([ 0, 17, 18, 19, 20, 21]));    

    all.append(set([ 2,  7, 12, 17, 22, 23]));
    all.append(set([ 2,  8, 13, 18, 24, 25]));
    all.append(set([ 2,  9, 14, 19, 26, 27]));
    all.append(set([ 2, 10, 15, 20, 28, 29]));

    all.append(set([ 3, 16, 21,  7, 13, 17]));
    all.append(set([ 3, 12, 17, 22, 27, 28]));
    all.append(set([ 3, 13, 22, 1, 29, 11]));
    all.append(set([ 3, 18, 29,  8, 30, 12]));

    all.append(set([ 1,  6, 11, 16, 19, 26]));
    all.append(set([ 1,  7, 17, 21, 27, 28]));
    all.append(set([ 1,  0,  8, 18, 29, 30]));
    all.append(set([ 1,  9,  2, 10, 12, 13]));

    all.append(set([ 4,  7, 11, 17, 21, 22]));
    all.append(set([ 4, 10, 11, 12, 13, 14]));
    all.append(set([ 4, 15, 16, 17, 18, 19]));
    all.append(set([ 4, 20, 21, 22, 23, 24]));

    all.append(set([ 5,  7,  9, 11, 13, 15]));
    all.append(set([ 5,  8, 11, 14, 17, 20]));
    all.append(set([ 5,  9, 13, 17, 21, 25]));
    all.append(set([ 5, 10, 16, 21, 17, 26]));


    all.append(set([ 7, 12, 17, 22, 27, 25]));
    '''

    all =[set([0, 1, 2, 3, 4, 5]), set([0, 7, 9, 10, 11, 29]), set([0, 14, 15, 16, 22, 25]), set([0, 18, 19, 20, 21, 23]),
           set([2, 7, 12, 17, 22, 23]), set([5, 7, 13, 18, 24, 25]), set([2, 9, 14, 19, 26, 27]), set([2, 6, 15, 20, 28, 29]),
           set([3, 7, 13, 16, 20, 26]), set([3, 10, 17, 24, 27, 28]), set([3, 11, 13, 19, 22, 31]), set([3, 12, 14, 18, 29, 30]),
           set([1, 6, 11, 16, 19, 24]), set([1, 7, 14, 21, 28, 31]), set([1, 13, 15, 17, 29, 30]), set([1, 10, 12, 19, 20, 25]),
           set([4, 21, 22, 24, 26, 29]), set([4, 6, 10, 12, 13, 14]), set([4, 16, 17, 18, 19, 28]), set([4, 9, 20, 22, 24, 30]),
           set([2, 8, 13, 18, 24, 25]), set([5, 8, 11, 14, 17, 20]), set([3, 6, 9, 17, 21, 25]), set([2, 10, 16, 21, 30, 31]), set([0, 12, 17, 24, 26, 31])]
    all = [set([0, 1, 2, 3, 4, 5]), set([0, 7, 9, 10, 11, 29]), set([0, 14, 15, 16, 22, 25]), set([0, 18, 19, 20, 21, 23]),
           set([2, 7, 12, 17, 22, 23]), set([5, 10, 15, 18, 22, 26]), set([2, 9, 14, 19, 26, 27]), set([2, 6, 15, 20, 28, 29]),
           set([3, 7, 13, 16, 20, 26]), set([3, 10, 23, 24, 27, 28]), set([3, 11, 13, 19, 22, 31]), set([3, 12, 14, 18, 29, 30]),
           set([1, 6, 11, 16, 23, 24]), set([1, 7, 14, 18, 28, 31]), set([1, 13, 15, 17, 27, 30]), set([1, 10, 12, 19, 20, 25]),
           set([4, 23, 25, 26, 29, 31]), set([4, 6, 10, 12, 13, 14]), set([4, 16, 17, 18, 19, 28]), set([4, 9, 20, 22, 24, 30]),
           set([2, 8, 13, 18, 24, 25]), set([5, 8, 11, 14, 17, 20]), set([3, 6, 9, 17, 21, 25]), set([2, 10, 16, 21, 30, 31]), set([0, 12, 17, 24, 26, 31])]


    all = [set([0, 1, 2, 3, 4, 5]), set([0, 7, 9, 10, 11, 29]), set([0, 14, 15, 16, 22, 25]), set([0, 18, 20, 21, 27, 31]), set([2, 7, 12, 21, 22, 23]), set([5, 6, 10, 18, 22, 26]), set([2, 9, 14, 19, 26, 27]), set([2, 6, 15, 20, 28, 29]), set([3, 7, 13, 16, 20, 26]), set([3, 10, 15, 23, 24, 27]), set([3, 11, 19, 22, 28, 31]), set([3, 12, 14, 18, 29, 30]), set([4, 6, 11, 12, 16, 27]), set([1, 6, 7, 14, 24, 31]), set([1, 13, 17, 22, 27, 29]), set([1, 10, 12, 19, 20, 25]), set([4, 23, 25, 26, 29, 31]), set([4, 10, 13, 14, 21, 28]), set([4, 7, 15, 17, 18, 19]), set([4, 9, 20, 22, 24, 30]), set([2, 11, 13, 18, 24, 25]), set([5, 11, 14, 17, 20, 23]), set([3, 6, 9, 17, 21, 25]), set([2, 10, 16, 17, 30, 31]), set([0, 12, 17, 24, 26, 28])]
    '''

    check1();

    all_errs();


    print sum(err_list), err_list;

    iter = 0;
    old_ind = -1;
    status = set();
    status.add(sum(err_list));

    random.seed(1);
    while sum(err_list) > 0 and iter < 8000:
        iter += 1;
        mis = max_index(old_ind)
        #print "mis:", mis
        mii = random.randint(0,len(mis)-1);
        mi = mis[mii]
        #f mi == old_ind:
        #    print "Error 2"
        sum_err = sum(err_list);
        #print "Start iter: ", iter, all[mi], mi, err_list[mi], sum_err;
        #print err_list
        r = try_one(mi);
        
        #print "try_one", r;
        elem = reduce(lambda (v,p,er), (x,y, z): (v, p, er) if er < z  else (x, y, z) , r,   (0,0, 100000))

        (v, p, er) = elem
        if er >= sum_err:
            print "Error 3";
            print "Iter: ", iter, all[mi], mi, err_list[mi], sum_err;
            elem = r[random.randint(0, len(r) -1)]
            (v, p, er) = elem
        
        #print "elem: ",  elem;
        t = (all[mi] - set([v]))
        t.add(p);
        all[mi] = t;
            
        #print "new elem:", all[mi]
        all_errs();
        old_ind = mi;
            
        
    print all

    check1()
    all_errs();    
    print sum(err_list);
    
if __name__ == '__main__':
    doit()


'''
[set([0, 1, 2, 3, 4, 5]), set([0, 7, 9, 10, 11, 29]), set([0, 14, 15, 16, 22, 25]), set([0, 18, 20, 21, 27, 31]), set([2, 7, 12, 21, 22, 23]), set([5, 6, 10, 18, 22, 26]), set([2, 9, 14, 19, 26, 27]), set([2, 6, 15, 20, 28, 29]), set([3, 7, 13, 16, 20, 26]), set([3, 10, 15, 23, 24, 27]), set([3, 11, 19, 22, 28, 31]), set([3, 12, 14, 18, 29, 30]), set([4, 6, 11, 12, 16, 27]), set([1, 6, 7, 14, 24, 31]), set([1, 13, 17, 22, 27, 29]), set([1, 10, 12, 19, 20, 25]), set([4, 23, 25, 26, 29, 31]), set([4, 10, 13, 14, 21, 28]), set([4, 7, 15, 17, 18, 19]), set([4, 9, 20, 22, 24, 30]), set([2, 11, 13, 18, 24, 25]), set([5, 11, 14, 17, 20, 23]), set([3, 6, 9, 17, 21, 25]), set([2, 10, 16, 17, 30, 31]), set([0, 12, 17, 24, 26, 28])]
''' 
