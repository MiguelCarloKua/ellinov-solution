import tkinter as tk
from tkinter import messagebox
from math import isqrt, prod

# This function is to check if the number is a prime number or not
def check_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
                return False
    return True

# This function checks if the number is a factorial
def factorial(n):
     if n < 0:
        return "Not a factorial"
     result = 1
     for i in range(2, n + 1):
          result *= i
    return result