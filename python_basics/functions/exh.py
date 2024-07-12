def spam(value):
    try:
        return 42/value
    except ZeroDivisionError:
        return '404 eror'
    
print(spam(0))
