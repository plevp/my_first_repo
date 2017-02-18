#!/usr/bin/python

def doit():
    # s = raw_input();
    s = 'aaabbcccddd'
    s = ''
    s= 'baab'
    d = True;
    
    while (d):
        d = False;
        i = 0;
        r = ''
        while (True):
            if i == len(s):
                break;
            print " i =", i
            c = 1;
            p = s[i];
            l = True;
            for j in xrange(i+1, len(s)):
                if s[j] == p:
                    c +=1;
                else:
                    l = False;
                    break;
            i = j
            print i, p, c
            if c > 1:
                d = True
            if c % 2 == 1:
                r = r + p;
            if l and j == len(s) -1:
                break;
            
        if d == False or len(r) == 0:
            break;
        s = r;
        
    if r == '':
        print "Empty String"
    else:
        print r 

    
if __name__ == "__main__":
    doit()
