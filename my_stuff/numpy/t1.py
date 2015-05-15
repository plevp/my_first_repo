
import time
import numpy


def trad_version():
    t1 = time.time()
    X = xrange(1000000)
    Y = xrange(1000000)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    X = numpy.arange(10000000)
    Y = numpy.arange(10000000)
    Z = X + Y
    return time.time() - t1


print trad_version()

print numpy_version()



