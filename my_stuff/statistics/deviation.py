
from math import *

def arith_mean(l):
    return (0.0 +sum(l))/ len(l)
    
    
def diviation(l):
    m = arith_mean(l)
    v = reduce(lambda a, x : a + (x -m)**2, l, 0.0)
    v = v / (len(l) -1)
    return (v, sqrt(v))

def moment(l, k):
    m = arith_mean(l)
    v = reduce(lambda a, x : a + (x -m)**k, l, 0.0)
    return v/len(l)

def skewness(l):
    print arith_mean(l)
    m3 = moment(l,3)
    m2 = moment(l,2)
    print m2, m3
    
    return m3 / (m2 * sqrt(m2))

def kurtosis(l):
    m4 = moment(l, 4)
    m2 = moment(l, 2)
    return m4 / (m2 **2)



#print diviation([1,2,3,4,5])
#print diviation([4.9, 4.8, 6.8])


#print skewness([ 1006.84, 15732.31, 41824.32, 415.42, 84748.37, 53041.98])

# Statistics quize week 3
print diviation([1.46, 4.16, 0.27, 9.95, 0.67, -0.14])
print skewness([1.46, 4.16, 0.27, 9.95, 0.67, -0.14])
print kurtosis([1.46, 4.16, 0.27, 9.95, 0.67, -0.14]) -3


