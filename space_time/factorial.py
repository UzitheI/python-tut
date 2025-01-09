import time

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print("Enter the number that you want the factorial of:")
number_for_factorial = int(input())

starting_time = time.time()

result = fact(number_for_factorial)

time_elapsed = time.time() - starting_time

print(f"The factorial is {result}")
print(f"The time elapsed in seconds is {time_elapsed}")
