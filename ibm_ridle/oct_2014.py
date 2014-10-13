

x0 = 2 ** 31;

def foo(order):
    global x0;
    x = x0;
    ord = 10 ** order;   
    ord1 = 10 * ord;
    part = x0 % ord
    #print "foo", x0, order, ord, part 
    for i in range(8000000):
        x = x * 2
        if x > ord1:
            x = x % ord1
        #print "foo", x
        if x % ord == part:
            return i
    return -1;

def bar():
    for i in range(1,11):
        r = foo(i)
        print i, " ---- ", r

bar()

        
