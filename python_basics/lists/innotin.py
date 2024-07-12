names=['jeremy','joue','samber']

print('Enter your names:')
name=input()

if name not in names:
    print('The person is not in our list')
else:
    print('The person is in our list')


for index, item in enumerate(names):
    print('index'+ str(index)+ ' has the name  '+item)
    
