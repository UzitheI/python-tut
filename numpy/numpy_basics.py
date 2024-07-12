import numpy as np

list1= [1,2,4]
print(list1)

list2 = ['Ram', 3, True, 'Final']

print(list2)

#list can contain a large number of datatypes but it gets fairly hard to manage once the data gets large thats why we need a library like numpy


#numpy is numeric python

#anything in a numpy array should be of the same datatype 

#datatype of numpy is nd array which stands for n-dimensional array


np1= np.array([0,1,2,3,4,5,6,67,8,9])
print(np1)

#shape of array,length of array

print(np1.shape)

np2= np.arange(10)

print(np2)

#step from range 0 to 10 print with interval of 2 

np3= np.arange(0,10,2)
print(np3)

#prints 10 zeros
np4= np.zeros(10)
print(np4)

#multidimensional array

np5= np.zeros((3,10))
print(np5)

#full , prints 2 dimensions of 6s

np6= np.full((2,10),6)
print(np6)

#convert python lists to np

my_list= [1,2,3,4,5]
np8= np.array(my_list)
print(np8)

print(np8[3])