#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import sys


avr = [0.0] *151
tmp = [0.0] * 151
point = [0] * 151

def calc(k,n):
    return ((10.0 + avr[n-1]) * (n-1) + (1+avr[k-n+1] ) * (k - n + 1)) / k 

def calc2(k):
    for n in range(2,k+1):
	t = calc(k,n)
	tmp[n] = t

    # print tmp[1:k+1]
    avr[k] = min(tmp[2:k+1])
    point[k] = tmp[2:k+1].index(avr[k]) +2

def doit():

  avr[0] = 0
  avr[1] = 0

  for i in range(2,101):
      calc2(i)

  #print avr
#  print point

  print "The result is", avr[100]
if __name__ == '__main__':
    doit()
