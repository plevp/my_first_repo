
import socket

MAXLINE = 4096
ROS_EOF = "#ros_eof"
ROS_EVENT = "#ros_event"

class Socket_Read:
    
    Normal = 0
    EOF   = 1
    Fatal = 2
    
    def __init__(self, hostname, port):
        # Create a TCP/IP socket
        self.rest_line = ""
        self.lines = [];
        self.line_ind = -1
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
        while self.line_ind == -1:
            # read buffer            
            all_data = self.recv()
            #print "all_data:";   print all_data;
            #print "end all_data"
            if not all_data: return None; # Error
            
            self.lines = all_data.split('\n');
            #print "lines:", self.lines
            
            if all_data[-1] != '\n' and len(self.lines) == 1:
                self.rest_line += self.lines[0]
            else:
                last = self.lines.pop();  # pop the last line
                self.line_ind = 0;
                self.lines[0] = self.rest_line + self.lines[0];
                self.rest_line = last;
                break

        result = self.lines[self.line_ind]
        self.line_ind +=1
        if self.line_ind == len(self.lines):
            self.lines = []
            self.line_ind = -1

        return result

    def read_non_empty_line(self):
        
        line = self.read_line()
        #print "line:", line
        
        while (line == ''):
            line = self.read_line();
        return line;

    def read_event(self):
        vals = []
        line = self.read_non_empty_line();

        #print "line:", line
        if line.startswith(ROS_EOF):
            return (self.EOF, " ", [])
        
        if not line.startswith(ROS_EVENT) :
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
