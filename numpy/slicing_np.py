import numpy as np

#slicing numpy arrays

np1= np.array([1,2,3,4,5,6,7,8])

#return 2,3,4,5

print(np1[1:5])

#from 3 till the end
print(np1[3:])

#return negative slices 
#-5 is 4 and -1 is 7
print(np1[-5:-1])

#steps (slice the array and print in the steps of 2)

print(np1[1:5:2])

#steps on the entire array

print(np1[::2])


#slice a 2-d array 

np2= np.array([[1,2,3,4,5],[2,3,4,55,4]])
#pull out a single item
print(np2[1,3]) #should return 55

#from 0 until the 1th which is basically the 0th array and then 
print(np2[0:1,0:3])