#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import socket
import sys
import time;

def doit(port, file_name):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('xn01', port)

    print 'connecting to %s port %s' % server_address
    sock.connect(server_address)

    try:
        fp = open(file_name);
    except:
        print "cannot open file %s" % file_name
        return;
    
    buf = fp.read();
    # time.sleep(20);
    print  'sending data: "%s"' % buf
    try :    #Set the whole string
        sock.sendall(buf)
    except socket.error:
        #Send failed
        print 'Send failed'
        sys.exit()
    
    
    sock.close()

if __name__  == '__main__':
    doit(int(sys.argv[1]), sys.argv[2])
    

