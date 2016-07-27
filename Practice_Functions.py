#### A bunch of functions I made for python practice 

#Returns True if even. 
def is_even(x): 
    if x % 2 == 0: 
        return True  
    else: 
        return False 

#Returns True if integer. 
def is_int(x): 
    if (x - int(x)) == 0: 
        return True
    else: 
        return False 

#Sums the digits for any integer i. 
def digit_sum(n): 
    x = str(n)
    y = [int(i) for i in x]
    return sum(y) 

#Facotorial recursively.
 def factorial(x):
    if x == 1 or x== 0: 
        return 1
    else: 
        return x*factorial(x-1)

#Returns a prime number.
def is_prime(x): 
    if x < 2: 
        return False 
    elif x == 3 or x == 2: 
        return True 
    else: 
        for n in range(2,x-1): 
            if x % n == 0: 
                return False 
        else:
            return True

#Reverses a text. 
def reverse(text): 
    m = []
    j = len(text) - 1
    for i in range(len(text)):
        m.append(text[-i + j])
    return ''.join(m)
 
 #Get rid of vowels. 
 def anti_vowel(text):
    m =[]
    vowel = 'aeiouAEIOU'
    for j in vowel[:len(vowel)]:
        for i in text[:len(text)]: 
            if i == j: 
                text = text.replace(i,'')
                m.append(text)
    return m[len(m) -1]
    
#Sum a scrabble score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    s = [ ]
    for i in score: 
        for j in word.lower():
            if i is j: 
                s.append(score[i])
    return sum(s) 

#******* bleeps a word 

def censor(text,word):
    text = text.split()
    for i in range(len(text)):
        if text[i] == word:
            for k in range(len(word)): 
                text[i] = word[k].replace(word[k], '*'*(k+1))
                
    return ' '.join(text)
   
    
#Returns the lenght of a sequence 
def count(sequence, item): 
    m = []
    for i in range(len(sequence)): 
        if sequence[i] == item: 
            m.append(sequence[i])
    return len(m)

### Takes a list and checks all integers mod 2. 
### If integer is even appends new list.
def purify(list): 
    l = []
    for i in range(len(list)): 
        if list[i] % 2 == 0: 
            l.append(list[i])
    return l

#Takes a list and returns the product of each argument in the list. 
def product(list):
    total = 1
    for num in list: 
        total *= num
        print total
    return total

#Removes duplicate integers in a list. 
def remove_duplicates(list):
    list.sort()
    new_list = []
    for i in list: 
        if list.count(i) >= 2: 
            list.remove(i)
            new_list.append(i)
            new_list
        else: 
            return list 
    return new_list
        