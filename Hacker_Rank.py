## Problems on Hacker Rank ##

## Yields the following mathematical properties ##
def two_integers(x,y): 
    yield x + y
    yield x - y
    yield x*y

## Prints division and float division for two integers 
def divide_two_integers(x,y): 
    print x // y
    print x / float(y)

## yields the power of k^2 for integers less than n. 
def less_integer(n): 
    k = 0
    while k < n: 
        yield k*k
        k += 1

## returns true if the year is a leap year and false otherwise. 
def leap_year(x): 
    if x % 4 == 0 and x % 100 == 0 and x % 400 == 0: 
        return True
    return False 