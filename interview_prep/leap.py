print('Enter the year that you want to check:')

year=int(input())


if year%100 != 0:
    if year%4 ==0:
        print(f"the year is a leap year")
        
    else:
        print('the year isnt a leap yar')


    


