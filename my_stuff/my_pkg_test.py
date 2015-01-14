#!/usr/bin/python

import my_pkg
import random


my_pkg.foo()

print my_pkg.gen_uniq_list(0,10)
print my_pkg.gen_uniq_list(0,10, 4)
print my_pkg.gen_uniq_list(0,10,4)

random.seed(2)

print my_pkg.random_point()
print my_pkg.random_point()


print my_pkg.random_point(100)
print my_pkg.random_point(100)
print my_pkg.random_point(100)
print my_pkg.random_point(100)


