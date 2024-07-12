
import random 
marks=['car','peope','pope']

print(random.choice(marks))

random.shuffle(marks)
#if you directly try to print the above , it returns none because the norm is not to return the mutable object but the mutation has happened
print(marks)