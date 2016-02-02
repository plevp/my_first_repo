#!/usr/bin/env python

import sys
import re

def main(file_name):
    d = {}
    try:
        fp = open(file_name);
        for l in fp.readlines():
            #ls = re.split('\W|\d+',l);
            ls = re.split('[^a-zA-Z]+', l);
            for i in ls:
                if len(i) == 0:
                    continue
                il = i.lower()
                if il not in d:
                    d[il] = 0
                d[il] = d[il] + 1
        print len(d)
        items = d.items()
        items.sort()
        for i in items:
            print i[0], i[1]

    except Exception as e:
        print e
        exit();




#--------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
            main(sys.argv[1])
	except:
            print "Error catched by try"
            
