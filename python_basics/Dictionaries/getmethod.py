#there is a getmethod by which we can get the values of the dictionary

mycat={'name':'andy','color':'green'}

#the getmethod at first takes the key and also takes the return type if the element is not found 

val = mycat.get('name',0)

print(val)