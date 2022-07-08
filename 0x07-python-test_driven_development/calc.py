def add(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("x and y must be a number")
    return x + y

def subtract(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("x and y must be a number")
    return x - y

def multiply(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("x and y must be a number")
    return x * y

def divide(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("x and y must be a number")
    if y == 0:
        raise ZeroDivisionError("Can not be divided by 0")
    return x / y
