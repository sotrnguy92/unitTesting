def add(x,y):
    """add function"""
    return (x +y);

def subtract(x,y):
    """subtract function"""

    return (x-y);

def multiply(x,y):
    """mutiply function"""

    return x*y;

def divide(x,y):
    """divide function"""

    if y == 0:
        raise ValueError("can not divide by zero!")
    return (x/y);

