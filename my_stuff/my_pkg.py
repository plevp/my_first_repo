
import random

def foo():
    print "Hello"

def gen_uniq_list(first, last, number= -1):

    if number == -1 or  number > (last-first +1):
        number = last -first +1

    r = list(range(first, last +1))

    random.shuffle(r)

    if r == last -first +1:
        return r
    else:
        return r[0:number]

def random_point(c=1):
    x = random.random() * c
    y = random.random() * c
    return (x,y)

def read_ints(fn):
    f = open(fn);
    inp = []
    for item in f.readlines():
        item = item.strip()
        if item != "":            
            inp.append(int(item))
    f.close()
    return inp;

def read_ints2(fn):
    f = open(fn);
    inp = []
    item = f.readline()
    while item:
        item = item.strip();
        if item != "":
            inp.append(int(item))
        item = f.readline()
        
    f.close()
    return inp
