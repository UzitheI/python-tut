import random,sys,os,math

for i in range(5):
    print(random.randint(1,10))

while True:
    print("Type exit:")
    res=input()
    if res=='exit':
        sys.exit()
    print('you typed'+ res +'.')