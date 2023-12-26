cats=[]
while True:
    print('Enter the name of your cat:')
    cat=input()
    if(cat==''):
        break
    cats=cats+[cat]

print('The name of the cats is:')
for cat in cats:
    print(''+cat)

