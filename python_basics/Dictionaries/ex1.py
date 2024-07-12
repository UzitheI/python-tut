#dictionaries help accessing data much easier

mycat={'name':'samantha','color':'grey'}

print(mycat['name'])

#one of the primary differences in lists and dictionaries is that the elements inside dictionaries are not ordered 

#when you compare a list with another list then the output will be false if done inside an interpreter shell 

#when you do that with a dictionary the value is returned to be true because there are seemingly no order

#while from python 3.7 dictionaries can remember the sequence by which elements were put in the dictionary, it is still not the best to use this because older versions of python dont use them, moreover there is no surefire way to access them as they dont have indexes like lists

#every dictionary has a key and a value and we can even use them in the lists