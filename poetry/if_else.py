print('Put something in the machine:')

input_in_machine=input()


if input_in_machine == 'coke':
    print('Rotating the machine, choosing bottle opener')
    bottle_opener=True
    
    if bottle_opener:
        print('Scanning it right now')
        print('Turns out it is a bottle opener')
        
        print("Press 1 open teh can'o'coke, 0 to fuck off:")
        
        opener_command=int(input())
        
        if opener_command==0:
            print('fackin off mi amor')
        
        else:
            print('Opening the can')
    
    else:
        print('This aint no bottle opener')

else:
    print('This aint no coke')
    