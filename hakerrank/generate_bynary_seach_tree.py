#!/usr/bin/python

import sys
#from collections import namedtuple
from random import randint, seed

#Node = namedtuple("Node", "value, parent, left, right")

def strval(n):    
    return "None" if n == None else str(n.value)

class Node:
    def __init__(self, v, p = None, l = None, r = None):
        self.value = v;
        self.left = l
        self.right = r
        self.parent = p

    def __str__(self):
        return "N("+ str(self.value)+ ","+ strval(self.parent) + ","+ strval(self.left) +  ","+ strval(self.right) + ")"

def print_tree2(n):
    if n == None: return "None"
    if n.left != None:
        print_tree2(n.left)
    print n
    if n.right != None:
        print_tree2(n.right)        

def print_tree(n, ind = 0):
    if n == None: return "None"
    print "." * ind + str(n)
    if n.left != None:
        print_tree(n.left, ind+1)
    if n.right != None:
        print_tree(n.right, ind+1)        
        
def gentree(min_v, max_v, nodes, parent=None):
    if nodes == 0:
        return None;
    elif nodes == 1:
        return Node(randint(min_v, max_v), parent, None, None)
    else:
        pass
        m = (max_v - min_v +1) / nodes
        n = nodes -1;
        l_nodes = randint(0, nodes-1);
        r_nodes = n - l_nodes;
        l = None; r = None
        if l_nodes > 0:
            l = gentree(min_v, min_v + m * l_nodes -1, l_nodes)
        if r_nodes> 0:
            r = gentree(min_v + m *(l_nodes +1), max_v, r_nodes)
        res = Node(randint(min_v + m * l_nodes, min_v + m * l_nodes + m -1), None, l,r);
        if l_nodes > 0: l.parent = res;
        if r_nodes > 0: r.parent = res;
        return res;

def doit(nodes, mult):
    seed(5)
    print "nodes =", nodes
    r = gentree(0, (nodes -1) *mult, nodes, None)
    print_tree(r)
    
if __name__ == "__main__":
    n  = int(sys.argv[1])
    k  = int(sys.argv[2])
    doit(n, k)

