#factorial of n

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


a=factorial(5)

print(a)