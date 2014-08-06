#!/usr/bin/python


gdata = 0
class My_class():

    data = 10;

    def doit(self):
        global gdata
        print "Self:", self.data;
        self.data = gdata;
        gdata +=1;

        print "Self:", self.data;
        print "Global", gdata

def doit():
    print "Class:", My_class.data

    m1 = My_class();
    m1. doit()
    m2 = My_class();
    m2. doit()
    print "Class:", My_class.data
    
    
if __name__  == '__main__':
    doit()
