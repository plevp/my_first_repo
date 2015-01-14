
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


    
