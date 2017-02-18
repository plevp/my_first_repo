#!/usr/bin/python

import sys

def doit():
    l1 = ['1','2','3']
    l2 = ['0','$','1']

    for i in xrange(len(l1)):
        try:
            print  int(l1[i])/int(l2[i])
        except Exception as e:
            print "Error code:", e
                        
if __name__ == "__main__":
    doit()
