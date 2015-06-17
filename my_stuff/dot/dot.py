# dot.py 

"Require Python 2.3 (or 2.2. with from __future__ import generators)"

def dotcode(cls):
    setup='node [color=Green,fontcolor=Blue,fontname=Courier]\n'
    name='hierarchy_of_%s' % cls.__name__
    code='\n'.join(codegenerator(cls))
    return "digraph %s{\n\n%s\n%s\n}" % (name, setup, code)

def codegenerator(cls):
    "Returns a line of dot code at each iteration."
    # works for new style classes; see my Cookbook
    # recipe for a more general solution
    for c in cls.__mro__:
        bases=c.__bases__
        if bases: # generate edges parent -> child
            yield ''.join([' %s -> %s\n' % ( b.__name__,c.__name__)
                           for b in bases])
        if len(bases) > 1: # put all parents on the same level
            yield " {rank=same; %s}\n" % ''.join(
                ['%s ' % b.__name__ for b in bases])

if __name__=="__main__": 
    # returns the dot code generating a simple diamond hierarchy
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    print dotcode(D)

