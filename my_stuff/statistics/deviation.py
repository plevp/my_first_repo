
from math import *

def arith_mean(l):
    return (0.0 +sum(l))/ len(l)
    
    
def diviation(l):
    m = arith_mean(l)
    print m
    v = reduce(lambda a, x : a + (x -m)**2, l, 0.0)
    v = v / (len(l) -1)
    return (v, sqrt(v))

#print diviation([1,2,3,4,5])
print diviation([4.9, 4.8, 6.8])
print diviation([1.46, 4.16, 0.27, 9.95, 0.67, -0.14])

