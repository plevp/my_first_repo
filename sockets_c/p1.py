#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import socket
import sys


def doit(port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('xn01', port)

    print 'connecting to %s port %s' % server_address
    sock.connect(server_address)

    while True:
        # Send data
        message = raw_input("message:\n")
        if message.strip() == "":
            break
        print  'sending "%s"' % message
        sock.sendall(message)
        
    sock.close()

if __name__  == '__main__':
    doit(int(sys.argv[1]))

