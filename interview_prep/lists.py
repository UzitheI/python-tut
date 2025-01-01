#arrays


arr=[1,2,3]


#arrays are dynamic by default in python, so lists can be used as stacks in python

arr.append(4)

print(arr) # should print [1,2,3,4]

arr.pop() # should pop 4


print(arr) # should be original


#as this is technically not a stack, we can still put values in random indexes

arr.insert(1,3) #should insert 3 in index 1, so list should be [1,3,2,3]

#another fun fact, using insert is an O(n) event because it goes through all the array and then puts the value where it needs to be, subsequently also has to fix the indexes for others
print(arr)

#directly indexing is O(1) because we're replacing the value

arr[1]=7

print(arr)



#initialize arr of size n with default value of 1


n=5

marr=[1]*n

print(marr)

print(len(marr))

# targeting the last value using -1, as index -1 is not out of bounds in python


print(arr[-1]) # should print the last item


# we can also slice the array


print(arr[1:3]) #starts from index 1 and takes up everything upto 3 except 3

# we have another feature called unpacking when the items of the list can be assigned to different variables


a,b,c=[1,2,3]
#for unpacking the number of variables must be equal to the number of items in the list


#a,b=[1] # gets error: not enough values to unpack
print(a,b,c)



#looping through the array

for i in range(len(arr)):
    print(arr[i])
    
#withou index

for n in arr:
    print(n)
    
#if we need suppose both the value and the index, one approach is to use the first for loop or use enumerate


for i,n in enumerate(arr):
    print(i,n)
    
#loop through multiple arrays simultaneously with unpacking


num1=[1,3,2,5,6]

num2=[1,3,2,5,1]


# we need to use something called zip

for n1,n2 in zip(num1, num2):
    print(n1,n2) # 1 3 2 5 6 at one and 1 3 2 5 1 
    
# reverse


trial=[1,2,3,4]


trial.reverse()

print(trial)


#sort

trial.sort()

print(trial)

trial.sort(reverse=True)

print(trial)

# sorting of strings can be done similarly but how can you do custom sorting, maybe sort through with in terms of length

#the answer is lambda functions


lamb_array=["apple","ball","elephant","micah"]

#lambda is a function without a name

lamb_array.sort(key=lambda x:len(x))

''' 
    the custom sort is set by using the parameter key where upon the key has to be the lenght of the strings, the length of the strings has to be returned by a function, for that we use lambda, we take in all the values of the array lamb_array using x and then pass it through the len function
    
'''

print(lamb_array)



#list comprehension




