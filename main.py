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
            text=f"Is the number prime? {prime_result}\n\nFactorial: {factorial_result}"
        )
    except ValueError:
        messagebox.showerror("Input error!", "Please enter a valid integer.")

root = tk.Tk()
root.title("Prime and Factorial Checker")
root.geometry("425x350")
root.configure(bg="#78B9B5")

tk.Label(root, text="Enter a number: ", font=("Helvetica", 14, "bold"), 
         bg="#78B9B5", fg="black").pack(pady=15)

input_frame = tk.Frame(root, bg="#78B9B5")
input_frame.pack(pady=5)

entry = tk.Entry(input_frame, font=("Consolas", 14), width=22,
                  justify="center", bg="white", fg="black", relief="solid")
entry.pack(pady=5)

btn = tk.Button(input_frame, text="Confirm", bg="#0F828C", fg="black", 
          font=("Helvetica", 12, "bold"), activebackground="#0F828C", 
          activeforeground="white", relief="groove", borderwidth=2, command=calculate, 
          padx=15, pady=6, width=22, height=1)

btn.pack(pady=10)

result_frame = tk.Frame(root, bg="#320A6B", bd=5, relief="flat")
result_frame.pack(pady=20, padx=20, fill="both", expand=True)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side="right", fill="y")

result_label = tk.Label(root, text="", font=("Arial", 13), 
                        bg="#320A6B", fg="white", justify="center", wraplength=400)
result_label.pack(expand=True, pady=15, padx=15)

root.mainloop()