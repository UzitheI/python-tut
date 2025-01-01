import numpy as np

#copy vs view


np1= np.array([1,2,3,4,5])

#create a view

np2= np1.view()

print(f'Origin ')