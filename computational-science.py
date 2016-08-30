### Trying to write some computational science problems### 

def f(x): 
    return x**3 + x + 1

### Bisection Method ### 
"""find a solution to f(x) = 0 given the continous function f on the interval [a,b],
f(a) and f(ab) have opposite signs:"""


def Bisection(a,b,TOL,N): 
    i = 1 
    FA = f(a)
    while i <= N:
        p = a+(b-a)/2.0
        FP = f(p)
        if FP == 0 or (b-a)/2.0 < TOL: 
            return p
        if FA * FP > 0: 
            a = p 
            FA = FP
        else:
            b = p
        i += 1
    return "Method Failed after %d iteration" %(i)


class Vector: 
    """Represent a vector in a multidimensional space."""
    def __init__(self,d):
    """Create d-dimensional vector of zerios.""" 
        self.d = [0]*d 

    def __len__(self)
    """Return the dimenson of the vector"""
        return len(self.d)

    def __getitem__(self,j): 
    """Return jth coordinate of vector."""
        return self.d[j]

    def __setitem__(self,j,val): 
        """Set jth coordinage of vector to given value."""
        self.d[j] = val 

    def __add__(self,other): 
    """Return sum of two vectors"""
        if len(self) != len(other): 
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)): 
            result[j] = self[j] + other[j]
        return result 

    def __eg__(self,other): 
        """Return True if vector has same coordinages as other."""
        return self.d == other.d

    def __ne__(self,other): 
        """Return True if vector differs from other"""
        return not self == other 

    def __str__(self): 
        """PRoduce string representation of vector."""
        return "<" + str(self.d)[1:-1] + ">"

