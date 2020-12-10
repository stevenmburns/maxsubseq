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
#        r, pr = x
#        pr = max(0,y+pr)
#        r = max(r,pr)
#        return r, pr
        return max(x[0],max(0,y+x[1])),max(0,y+x[1])
    r, pr =  functools.reduce( f, s, (0,0))
    return r

def cmp( s):
    f = fast(s)
    print( s, f)
    return ref(s) == f
    return quad(s) == f
    return quad2(s) == f
    return fastalt(s) == f

def test_A():
    assert 0 == ref([])
    assert 1 == ref([1])
    assert 0 == ref([-1])
    assert 1 == ref([1,-1])
    assert 3 == ref([2,-1,1,1])
    assert 2 == ref([1,0,1,-1,0,1])

def test_B():
    assert cmp([])
    assert cmp([1])
    assert cmp([-1])
    assert cmp([1,-1])
    assert cmp([-1,1])
    assert cmp([2,-1,1,1])
    assert cmp([1,1,-1,2])
    assert cmp([1,0,1,-1,0,1])

def test_C():
    for i in range(10):
        lst = []
        for j in range(10):
            lst.append( random.randint( -100, 100))
        assert cmp( lst)

