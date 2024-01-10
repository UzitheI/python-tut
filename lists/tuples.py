#tuples is similar to lists but the values inside tuples cannot be changed

def main():
    max=('anish','ramesh','chinese')

    min=('anish',)
    print(max[0])

    stax=max+min
    print(stax)

    min[0]='amrt'

    # print(min)
    #here we cannot modify the value of min because it is a tupule, unlike other languages it doesnt matter if you leave , at the end of the list because it is a tuple and it is immutable

    

main()

    