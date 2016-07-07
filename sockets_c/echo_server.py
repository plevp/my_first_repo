#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import socket
import sys

MAXLINE = 4096

def doit(port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #server_address = ('localhost', port)
    print socket.gethostname();
    server_address = ( socket.gethostname(), port)
    
    print 'starting up on %s port %s' % server_address
    # Bind the socket to the port
    try:
        sock.bind(server_address)
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    # Listen for incoming connections
    sock.listen(1)

    while True:
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
            data = connection.recv(MAXLINE)
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
