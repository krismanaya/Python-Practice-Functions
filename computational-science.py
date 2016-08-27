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