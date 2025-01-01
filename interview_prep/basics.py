#runtime assignment

n=0

print("n =", n)

n= 'abc'

print(n)

#here you can see that variables have no type, and every variable is assigned at runtime

#multiple assignments


a, b, c = 1, True, 'abc'

#incrementation
n=0
n= n + 1
n+=1
#n++ this is bad and cant be done, related to the python interprete

n= None #prints none

# if n>2:
#     print(True)

# if n==1:
#     print(False)

n=0
while n<5:
    print(n)
    n+=1


for i in range(5):
    print(i)



for i in range(2,6):
    print(i)
    
#decrementing within the loop(start from 6 upto 2, increment by 1)
for i in range(6,2,-1):
    print(i)
    
#divison in python is different for example , divison in python is decimal, other language automatically round off to 0 ie integer division but python doesnt do that


print(5/2) # yields 2.5

#if integer division is needed 

print(int(5/2))


#also other languages when negative division round of to number closer to 0 but python rounds of towards negative infinty

print(-7/2) #yields 3.5 because decimal division

#now integer division

print(int(-7/2))

#if you want to round down

print(5//2) #this rounds to 2

#remainder is calculated by %

print(10%3)

#again the issue is remainder with negative values

print(-10%3) #maybe expecting -1 but we get 2, which is differnt from other C based languages

#to get actual value, we need to import math

import math

print("The actual correct mod value is ",math.fmod(10,3))


#to round down

print("Round down this number ", math.floor(10/3))

#to round up

print("Round up is done by ",math.ceil(10/3))

#to square

print("Square is taken by ", math.sqrt(5))

#to power

print("power is given by", math.pow(2,5))

#python numbers are infinite so they never overflow, which means

print(" A large number ", math.pow(2,300))

#to get the most minimum value

float("-inf")

#to get max

print((math.pow(2,300))< float("inf")) # should print true