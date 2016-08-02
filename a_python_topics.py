##More practice## 


my_dict = { "Name" : "Kris", 
            "Age"  : 21, 
            "BDFL" : True 
}
print my_dict.items()
##[('BDFL', True), ('Age', 21), ('Name', 'Kris')]##
print my_dict.keys()
##['Name','Age','BDFL']##
print my_dict.values() 
##['Kris', 21, True]##

##Prints the keys of the dictionary and the associated value of the keys##
for key in my_dict: 
    print key,my_dict[key]

#list comprehension prints even numbers in range 51#
evens_to_50 = [i for i in range(51) if i % 2 == 0]

#Prints even squares# 
even_squares = [x**2 for x in range(1,11) if (x**2) % 2 == 0]

#Prints cubes only if the cube is evenly divisable by four#
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0] 

#Binary operation#
print 0b1,     #1 2^0
print 0b10,    #2 2^1
print 0b11,    #3 2^0 + 2^1
print 0b100,   #4 2^2 
print 0b101,   #5 2^0 + 2^2
print 0b110,   #6 2^1 + 2^2
print 0b111,   #7 2^0 + 2^1 + 2^2
print 0b1000,  #8 2^3 
print 0b1001,  #9 2^3 + 2^0 
print 0b1010,  #10 2^3 + 2^1
print 0b1011,  #11 2^3 + 2^1 + 2^0
print 0b1100,  #12 2^3 + 2^2 
print 0b1101,  #13 2^3 + 2^2 + 2^0
print 0b1110,  #14 2^3 + 2^2 + 2^1 
print 0b1111,  #15 2^3 + 2^2 + 2^1 + 2^0 
print 0b10000, #16 2^4
print 0b10001, #17 2^4 + 2^0
print 0b10010, #18 2^4 + 2^1
print 0b10011, #19 2^4 + 2^1 + 2^0 
print 0b10100  #20 2^4 + 2^2

print "******"
print 0b1 + 0b11
print 0b11 * 0b11