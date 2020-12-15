import itertools
import functools
import random

def ref( s):
    result = 0
    for l in range(len(s)):
       for u in range(l+1,1+len(s)):
           ss = sum( s[l:u])
           result = max(result,ss)
    return result

def quad( s):
    result = 0
    for l in range(len(s)):
       ss = 0 
       for u in range(l+1,1+len(s)):
            ss += s[u-1]
            result = max(result,ss)
    return result

def quad2( s):
    result = 0
    cached = [0] + list(itertools.accumulate(s))

    for l in range(len(s)):
       for u in range(l+1,1+len(s)):
            ss = cached[u] - cached[l]
            result = max(result,ss)
    return result

def fast( s):
    r = 0
    pr = 0
    for x in s:
        pr = max(0,x+pr)
        r = max(r,pr)
    return r

def fastalt( s):
    def f( x, y):
        # Walrus operator, requires Python 3.8
        return max(x[0],(pr:=max(0,y+x[1]))),pr
    r, pr =  functools.reduce( f, s, (0,0))
    return r

class Associative:
    def __init__(self, x=0):
        self.ss = max(0,x)
        self.ls = max(0,x)
        self.sr = max(0,x)
        self.lr = x

    def __repr__(self):
        return f"({self.ss} {self.ls} {self.sr} {self.lr})"

    def __add__(self, other):
        result = Associative()
        result.lr = self.lr + other.lr
        result.ls = max(self.ls,self.lr + other.ls)
        result.sr = max(self.sr + other.lr, other.sr)
        result.ss = max(self.ss,other.ss,self.sr+other.ls)
#        print( f"{self} + {other} => {result}")
        return result

def linear_associative( s):
    def tree( s):
        l = len(s)
        if l == 1:
            return s[0]
        elif l == 0:
            return Associative(0)
        else:
            # walrus operator requires 3.8
            return tree(s[:(m := l//2)]) + tree(s[m:])

    return tree([ Associative( x) for x in s]).ss

def cmp( s):
    f = fast(s)
#    print( s, f)
#    assert ref(s) == f
#    assert quad(s) == f
#    assert quad2(s) == f
    assert fastalt(s) == f
    assert linear_associative(s) == f

def test_A():
    assert 0 == ref([])
    assert 1 == ref([1])
    assert 0 == ref([-1])
    assert 1 == ref([1,-1])
    assert 3 == ref([2,-1,1,1])
    assert 2 == ref([1,0,1,-1,0,1])

def test_B():
    cmp([])
    cmp([1])
    cmp([-1])
    cmp([1,-1])
    cmp([-1,1])
    cmp([2,-1,1,1])
    cmp([1,1,-1,2])
    cmp([1,0,1,-1,0,1])
    cmp([80, -62, 66, -80, -85, 33, -96, 12, -80, -1])

def test_C():
    number_of_trials = 10000
    size_of_list = 100
    b = 100
    for _ in range(number_of_trials):
        lst = [random.randint( -b, b) for _ in range(size_of_list)]
        cmp( lst)


