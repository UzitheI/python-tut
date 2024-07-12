import random
def getNumber(Number):
    if(Number==1):
        return 'uno'
    elif(Number==2):
        return 'dos'
    elif(Number==3):
        return 'tres'

print(getNumber(random.randint(1,3)))
#with return you are not printing so using print is mandatory