#creating an array of options
import random
family=['ramhari','durga','ramgopal','kalpana','pralad','sujita','pujan','ujjwal','ujjwalika','suwarna','swarnika']

def choice():
    id=random.randint(0, len(family)-1)
    print(family[id])

choice()