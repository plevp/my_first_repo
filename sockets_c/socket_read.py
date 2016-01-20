
import socket

MAXLINE = 4096
HOSTNAME = 'xn01'

class Socket_Read:
    sock = None
    rest_line = ""
    lines = [];
    line_ind = -1
    
    def __init__(self, hostname, port):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address  = (hostname, port)
        self.sock.connect(server_address)

        print 'connecting to %s port %s' % server_address

    def recv(self):
        data = self.sock.recv(MAXLINE)
        return data

    def close(self):
        self.sock.close();

    def read_line(self):
        if self.line_ind == -1:
            # read buffer
            all_data = self.recv()
            #print "all_data:";   print all_data;
            if len(all_data) == 0:
                return None;
            self.lines = all_data.split('\n');
            
            last = self.lines.pop();  # pop the last line
            if len(self.lines) == 0:
                return None
            self.line_ind = 0;
            if self.rest_line != "":
                self.lines[0] = self.rest_line + self.lines[0];
            self.rest_line = last;
        result = self.lines[self.line_ind]
        self.line_ind +=1
        if self.line_ind == len(self.lines):
            self.lines = []
            self.line_ind = -1

        return result
            

    def read_event(self):
        pass
    
