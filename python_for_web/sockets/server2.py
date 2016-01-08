#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port


def doit(port):
    server_address = ('localhost', port)
    print 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    
    # Listen for incoming connections
    sock.listen(1)
    print 'waiting for a connection'
    connection, client_address = sock.accept()
    print "connection: ", connection, "client_address: ", client_address            
    print 'connection from', client_address
            
    
    while True:
        # Wait for a connection
        #print 'waiting for a connection'
        # connection, client_address = sock.accept()
        #print "connection: ", connection, "client_address: ", client_address                
        #print 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print  'received "%s"' % data
            if data:
                print 'sending data back to the client'
                connection.sendall(data)
            else:
                print 'no more data from', client_address
                break

    connection.close()

if __name__ == '__main__':
    doit(int(sys.argv[1]))
