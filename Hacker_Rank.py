## Problems on Hacker Rank ##

## Yields the following mathematical properties ##
def two_integers(x,y): 
    yield x + y
    yield x - y
    yield x*y

## Prints division and float division for two integers. ##

def divide_two_integers(x,y): 
    print x // y
    print x / float(y)

## yields the power of k^2 for integers less than n. ##
def less_integer(n): 
    k = 0
    while k < n: 
        yield k*k
        k += 1

## returns true if the year is a leap year and false otherwise. ##
def leap_year(x): 
    if x % 4 == 0 and x % 100 == 0 and x % 400 == 0: 
        return True
    return False 

## returns power of integer with map and lambda properties. ##
def pow_integer(n):
    return map(lambda n: n*n ,range(0,n))

## P norm ## 
def p_norm(vector,p): 
    return sum([pow(pow(number,p),p) for number in vector])

## norm ## 
def norm(vector): 
    retrun sum([pow(pow(number,2),.5) for number in vector])
    