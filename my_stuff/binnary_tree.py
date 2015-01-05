#! /usr/bin/env python


Nodes = 10


class Node:

    def __init__(self, val, l = None, r = None):
        self.left = l
        self.right = r
        self.value = val
        
    def __str__(self):
        return "[%d] {%s, %s}" %\
               (self.value,  "Null" if self.left == None else str(self.left.value),
                "Null" if self.right == None else str(self.right.value))

    def Disp(self, indent="", role="R"):
        print "%s%s%s" % (indent, role,self)
        indent += "  "
        if self.left != None:
            self.left.Disp(indent,"L");
        if self.right != None:
            self.right.Disp(indent, "R");

    def Min(self):
        return self.value if self.left == None else self.left.Min()

def CreateRandomTree(Nodes):
    pass

def SmallTree():
    
    t = Node(100, Node(50), Node(150))
    return t


def TestTree():
    return Node(4, Node(2, Node(1), Node(3)), Node(11, Node(10, Node(5, None, Node(6, None, Node(8, Node(7), Node(9)))))))
    
    
def Doit():
    t = SmallTree()
    print "Small Tree:" 
    print "Root:" 
    print t
    print "Tree:"
    t.Disp()

    print "Min:", t.Min()

    print "\n\nTestTree"
    t = TestTree()
    print "Root:" 
    print t
    print "Tree:"
    t.Disp()
    print "Min:", t.Min()
    

if __name__ == '__main__':
    Doit()
