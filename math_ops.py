import math

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    return math.sqrt(a)

def factorial(a):
    return math.factorial(a)

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True
