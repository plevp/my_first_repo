
import sys

current = {}
next = {}

"""
del d[key]
d.clear()
del d
d.get(k, default)
"""


def get(d, k):
    return d.get(k, None);

def print_d(d):
    for (k,v) in d.items():
        print "key:", k, "value:", v

def display(d):

    ks = d.keys()
    y = ks.sort(key = lambda x: (x[1], x[0]))
    
    max_y = ks[-1][1]
    min_y = ks[0][1]
    max_x = reduce(lambda a, x: a if a >= x[0] else x[0], ks, -sys.maxint) 
    min_x = reduce(lambda a, x: a if a <= x[0] else x[0], ks, sys.maxint) 

    print "max x,y", max_x, max_y

    for k in range(max_y, min_y-1, -1):
        f = filter(lambda x: x[1] == k, ks)
        if len(f) == 0:
            s = print_line([], max_x);
        else:
            z = map(list, zip(*f))
            s = print_line(z[0], max_x);
        print s
        
    
foo_prev = -1
def foo(x):
    global foo_prev
    r = x - foo_prev -1
    foo_prev = x
    return r
    
def print_line(l, m):
    global foo_prev
    #print "print_line", l, m;
    foo_prev = -1
    l1 = map(foo, l +[m+1]);
    return reduce(lambda str, x: str + x * '.' + '*', l1, '')[:-1]


def read_data(fn):
    points = [];
    f = open(fn);
    y = 0
    for line in f.readlines():
        line = line.rstrip("\n")
        print "Line: ", len(line), line
        for x in range(len(line)):
            if line[x] == '*':
                points.append((x,y))
        y += 1

    f.close()
    y -= 1
    print points
    for ind in range(len(points)):
        current[(points[ind][0], y - points[ind][1])] = 1
    print current
    

    
#   l.sort(key = lambda x: (x[0], x[1]))
#   print ('.', end ='')
    #keys = sorted(current.keys(), key = lambda x : (x[1], x[0]))


def doit(fn):
    current.clear()
    read_data(fn)
    display(current)

