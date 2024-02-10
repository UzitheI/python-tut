birthday={'ujjwal':'feb 27','janet':'30th feb'}

print('Find the birthday for a person')
name= input()

if name in birthday:
    print('the birtday of '+name+'is on '+birthday[name])
else:
    print('I dont have the birthday input for that person')
    print('What is the name of the person')
    new_name=input()
    print('What is their birthday')
    new_date= input()
    # birthday[new_name]=new_date
    birthday.update({new_name:new_date})
    #these are the 2 methods used to update a dictionary 
    
    print(birthday)


