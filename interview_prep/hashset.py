#hashset


mySet=set()


a=4
b=4.5

c="hello"

sample_list=[1,2,3]

sample_tuple=(1,2,3)

sample_dictionary={'name':'john','age':30}

sample_set={1,2,3}

sample_set.add(4)

sample_set_2={1,2,3,4,5}

sample_set.intersection(sample_set_2)


a=101

b=111

#complement

print(~a)

#xor

print(a^b)

#and

print(a&b)


#two's complement


#strings to list

a="apple"


list(a)

print(list(a))




#ive been given a function that takes in a string and has a parameter reverse=True, how can i reverse the string using such function

def reverse_string(string,reverse=True):
    if reverse:
        return string[::-1]
    else:
        return string



    

