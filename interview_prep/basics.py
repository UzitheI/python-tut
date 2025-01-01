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