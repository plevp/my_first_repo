#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import time 

from socket_read import *


def doit(port):

    sock = Socket_Read(HOSTNAME, port);
    fp = open("tmp.txt", "w");
    while True:
        # Look for the response
        data = sock.read_line()
        if data == None:
            break
        print 'received "%s(%d)"' % (data, len(data))
        
        fp.write(data+"\n");
        
        if data == "It is the last line":
            break;

    fp.close();
    sock.close()

if __name__  == '__main__':
    doit(int(sys.argv[1]))

