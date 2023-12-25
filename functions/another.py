import random
def getNumber(Number):
    if(Number==1):
        return 'uno'
    elif(Number==2):
        return 'dos'
    elif(Number==3):
        return 'tres'

newNumber=random.randint(1,3)
answer=getNumber(newNumber)
print(answer)
#with return you are not printing so using print is mandatory