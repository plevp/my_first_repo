
import socket

MAXLINE = 4096
HOSTNAME = 'xn01'

class Socket_Read:
    
    Normal = 0
    EOF   = 1
    Fatal = 2
    
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

    def read_non_empty_line(self):
        line = self.read_line()
        while (line == ''):
            line = self.read_line();
        return line;

    def read_event(self):
        vals = []
        line = self.read_non_empty_line();

        if line == None:
            return (self.EOF, " ", [])

        #print "line:", line
        if not line.startswith("#ros_event ") :
            return (self.Fatal, "*** Fatal: cannot find keyword #ros_event \n\tline: " + line)

        ls = line.split();
        if len(ls) != 4:
            return (self.Fatal, "*** Fatal: cannot parse #ros_event line \n\tline: " + line)

        topic = ls[2]
        line = self.read_non_empty_line();
        while line.strip() != "}":
            ls = line.split(": ",1)
            if len(ls) != 2:
                return (self.Fatal, "*** Fatal: cannot parse data line \n\tline:" + line)
            vals.append(ls[1])
            line = self.read_non_empty_line();
        
        return (self.Normal, topic, vals)
