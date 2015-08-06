
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



    


## ********************** ## 

def state_size(state):
    ks = state.keys()
    ks.sort(key = lambda x: x[0])
    
    max_x = ks[-1][0]
    min_x = ks[0][0]
    ks.sort(key = lambda x: x[1])
    
    max_y = ks[-1][1]
    min_y = ks[0][1]

    return (min_x, max_x, min_y, max_y)

state = {}

## initial
state[(1,0)] = 1
state[(0,0)] = 1
state[(-1,0)] = 1

state[(10,10)] = 1
state[(10,11)] = 1
state[(11,10)] = 1
state[(11,11)] = 1

state[(20,20)] = 1
state[(20,21)] = 1
state[(21,20)] = 1
state[(21,21)] = 1
state[(22,22)] = 1
state[(23,23)] = 1
state[(22,23)] = 1
state[(23,22)] = 1


state[(-43,-43)] = 1
state[(-43,-44)] = 1
state[(-43,-45)] = 1
state[(-44,-43)] = 1
state[(-45,-44)] = 1

print "State init", state_size(state)

# get all neigbours
def neib(i,j):
    n=[]
    for k1 in range(-1,2):
        for k2 in range(-1,2):
            n.append((i+k1, j + k2))
    return n
    
# generator next state of life    
def gen_life():
    global state

    yield state
    while True:
        #print "State", state
        d1 = {};
        for (i,j), _ in state.items():
            
            ns = neib(i,j);
            
            for n in ns:
                if not n in d1:
                    nss = neib(n[0], n[1])
                    c = 0
                    for nn in nss:
                        if nn in state and nn != n:
                            c += 1
                    d1[n] = 2                    
                    if n in state:
                        if ( c == 2 or c ==3):
                            d1[n] = 1
                    else:
                        if c==3:
                            d1[n] = 1
        state.clear()
        for k, v in d1.items():
            if v == 1:
                state[k] =1

        yield state;
            


g = gen_life()

print g

for k in range(4):
    g1 = g.next()
