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
    return prod(range(1, n + 1))

def calculate():
    try:
        number = int(entry.get())
        prime_result = "Yes" if check_prime(number) else "No"
        factorial_result = factorial(number)
        result_label.config(
            text=f"Is Prime? {prime_result}\nFactorial: {factorial_result}"
        )
    except ValueError:
        messagebox.showerror("Input error: Please enter a valid input.")

root = tk.Tk()
root.title("Prime and Factorial Checker")
root.geometry("400x400")

tk.Label(root, text="Enter a number: ").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Confirm", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()