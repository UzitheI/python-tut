diction={'name':"Sweigart",'age':'45'}


key=list(diction.keys())

#this will transfer all the key values into the list 

val=list(diction.values())

#now they can be used accordingly

print('the ' + key[0] +'is '+val[0])

#we can check if the values exist in the dictionary or nto 

def check_the_val():
    print('Enter the key that you want to check')
    k=input()
    if k in diction:
        return True
    else:
        return False

val=check_the_val()
if(val== True):
    print('It is done')