import time

counter=0

def fibonacci(n):
    global counter
    counter += 1
    print(f'Counter: {counter}')
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print('Enter the number for which you want the fibo:')

number=int(input())

starting_time=time.time()

print(f"The {number}th fibonacci number is", fibonacci(number))

elapsed_time=time.time()-starting_time

print(f"The time take is {elapsed_time}")


