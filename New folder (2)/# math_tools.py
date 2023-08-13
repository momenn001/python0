# math_tools.py

def maximum_num(x, y, z):
    """
    Returns the maximum of three numbers.
    """
    return max(x, y, z)

def even_num(x):
    """
    Returns True if the given number is even, False otherwise.
    """
    return x % 2 == 0

def prime_num(x):
    """
    Returns True if the given number is prime, False otherwise.
    """
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
