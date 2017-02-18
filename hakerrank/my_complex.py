#!/usr/bin/python

class Complex(object):
    def __init__(self, real, imaginary):
        self.r = float(real)
        self.i = float(imaginary)
        
    def __add__(self, no):
        return Complex(self.r + no.r, self.i + no.i)
        
    def __sub__(self, no):
        return Complex(self.r - no.r, self.i - no.i)       
        
    def __mul__(self, no):
        return Complex(self.r * no.r - self.i * no.i, self.r * no.i + self.i * no.r)
        
    def __div__(self, no):
        t = no.r **2 + no.i**2
        r_ = self.r * no.r + self.i* no.i
        i_ = self.i* no.r - self.r * no.i
        return Complex(r_/t, i_/ t)
  
    def mod(self):
        return Complex(pow(self.r**2 + self.i**2, 0.5), 0)
    
        
    def __str__(self):
        
        if self.i == 0:
            result = "%.2f+0.00i" % (self.r)
        elif self.r == 0:
            if self.i >= 0:
                result = "0.00+%.2fi" % (self.i)
            else:
                result = "0.00-%.2fi" % (abs(self.i))
        elif self.i > 0:
            result = "%.2f+%.2fi" % (self.r, self.i)
        else:
            result = "%.2f-%.2fi" % (self.r, abs(self.i))
        return result


if __name__ == '__main__':
    #c = map(float, raw_input().split())
    #d = map(float, raw_input().split())
    #x = Complex(*c)
    #y = Complex(*d)
    x = Complex(2,1)x    
    y = Complex(5,6)
    
    print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))


