import tkinter as tk
from ttkbootstrap.constants import * 
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
            text=f"Is the number prime? {prime_result}\n\nFactorial: {factorial_result}",
            fg="white", bg="#320A6B"
        )
    except ValueError:
        messagebox.showerror("Input error!", "Please enter a valid integer.")

root = tk.Tk()
root.title("Prime and Factorial Checker")
root.geometry("425x350")
root.configure(bg="#78B9B5")

tk.Label(root, text="Enter a number: ", font=("Helvetica", 14, "bold"), bg="#78B9B5", fg="black").pack(pady=15)

input_frame = tk.Frame(root, bg="#78B9B5")
input_frame.pack(pady=5)

entry = tk.Entry(input_frame, font=("Consolas", 14), width=20, justify="center")
entry.pack()

tk.Button(input_frame, text="Confirm", bg="#0F828C", fg="black", font=("Helvetica", 12, "bold"), activebackground="#065084", activeforeground="white", relief="flat", command=calculate, padx=15, pady=6, width=20).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 13), bg="#78B9B5", fg="white", justify="center")
result_label.pack(pady=10, padx=20, fill="x")

root.mainloop()