#python2
import sys
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
def leap_year(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False

## returns power of integer with map and lambda properties. ##
def pow_integer(n):
    return map(lambda n: n*n ,range(0,n))

## L^P norm ## 
def p_norm(vector,p): 
    return pow(sum([pow(abs(number),p) for number in vector]), p)

## L^2 norm ## 
def norm(vector): 
    return pow(sum([pow(abs(number),2) for number in vector]), .5)
    
def solveMeFirst(a,b):
    return a+b
 """This is a sample for hacker rank to have standard output for their terminal."""


num1 = input()
num2 = input()
res = solveMeFirst(num1,num2)
print res


"""Alice and Bob problem"""
a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

alice = 0
bob = 0 
if a0 < b0: 
    bob +=1 
if a0 > b0: 
    alice += 1
if a1 < b1: 
    bob += 1
if a1 > b1: 
    alice += 1
if a2 < b2: 
    bob += 1 
if a2 > b2: 
    alice +=1 
print alice,bob
  

#!/bin/python
"""Very Big Sum problem"""

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print sum(arr)


"""Given a square matrix of size n x n , 
calculate the absolute difference between the sums of its diagonals."""
n = int(raw_input().strip())
a = []
primary_diagonal = 0 
secondary_diagonal = 0 
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
for i in range(n): 
    primary_diagonal += a[i][i]
    secondary_diagonal += a[i][(n-1)-i]
print abs(primary_diagonal - secondary_diagonal)


"""Given an array of integers, calculate which fraction of its elements are positive, 
which fraction of its elements are negative, and which fraction of its elements are zeroes, 
respectively. Print the decimal value of each fraction on a new line."""
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos = 0
neg = 0
zeros = 0
for i in arr: 
    if i > 0:
        pos += 1
    if i < 0:
        neg += 1
    if i == 0:
        zeros += 1
pos_n = pos/float(n)
neg_n = neg/float(n)
zeros_n = zeros/float(n)
print pos_n
print neg_n
print zeros_n


"""Print a stair case of hashes of size n with height n in the opposite direction."""
n = int(raw_input().strip()) 
for i in range(1,n+1): 
    print ' ' * (n - i) + '#'*i
    


"""Circular Array Rotation"""
n, k, q = map(int, raw_input().strip().split(' '))
arr = map(int,raw_input().strip().split(' '))
queries = []
for _ in xrange(q): 
    queries.append(int(raw_input().strip()))
for _ in range(k): 
    arr = [arr[-1]] + arr[:-1]
for query in queries: 
    print arr[query]


"""Divisible Sum Pairs: You are given an array of n integers a_0, ...., a_n-1
and a positive integer k. Find and pring the (i,j) pairs where i<j and a_i + a_j
is evenly divisible by k."""

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
count = 0
for i in range(n-1): 
    for j in range(i+1,n): 
        if (a[i] + a[j]) % k == 0:
            count +=1 
            print(a[i],a[j])
print count

"""a concatenation of one or more words consisting of English letters 
input: str(saveChangesInTheEditor)
output: 5 """
s = raw_input().strip()
count = 1
for letter in s: 
    if letter == letter.upper(): 
        count += 1
print count 

"""takes a sentence of words and checks if its a pangram or not."""
s_1 = raw_input().strip()
alphabet = "abcdefghijklmnopqrstuvwxyz"
low_s1 = s_1.lower()
sent_1 = ''.join(low_s1.split())
u_1 = []
for c in sent_1: 
    if c not in u_1: 
        u_1.append(c)
order_1 = [ord(letter) for letter in u_1]
alphabet_order = [ord(letter) for letter in alphabet]
if sum(order_1) == sum(alphabet_order): 
    print "pangram"
else: 
    print "not pangram"

        




 


