import tkinter as tk
import customtkinter as ctk
import sys
from tkinter import messagebox
from math import isqrt, prod

# Can be configured to test other cases
sys.set_int_max_str_digits(0)

# This function is to check if the number is a prime number or not
def check_prime(n):
    if n <= 1: # 1 is not a prime number
        return False
    if n <= 3: # 3 is a prime number
        return True
    if n % 2 == 0 or n % 3 == 0: # Check if they are divisible by either 3 or 2
        return False
    for i in range(5, isqrt(n) + 1, 6): #
        if n % i == 0 or n % (i + 2) == 0:
                return False
    return True

# This function checks if the number is a factorial
def factorial(n):
    if n < 0: # Negative values are not factorial
        return "Not a factorial"
    return prod(range(1, n + 1)) # This will iterate the values of n! = e.g. (3 = 1 x 2 x 3)

# Outputs the result of isPrime and the input's factorial (n!)
def calculate():
    input_value = entry.get()

    if not input_value.isdigit() or "." in input_value:
        messagebox.showerror("Input error!", "Please enter a valid positive integer (non-decimal).")
        return

    number = int(input_value)
    prime_result = "Yes" if check_prime(number) else "No"
    factorial_result = factorial(number)
    
    result_text.configure(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Is the number prime? {prime_result}\n\nFactorial: {factorial_result}")
    result_text.configure(state="disabled")


# Non-resizable window
root = ctk.CTk()
root.title("Prime and Factorial Checker")
root.geometry("500x500")
root.configure(fg_color="#4173CF")
root.resizable(False, False)

# Label
tk.Label(root, text="Enter a number: ", font=("Arial", 14, "bold"), 
         bg="#4173CF", fg="white").pack(pady=15)

# Textbox for input
entry = ctk.CTkEntry(root, width=200, height=40, corner_radius=20, font=("Arial", 14),
                  justify="center", fg_color="white", text_color="black")
entry.pack(pady=5)

# Confirm button
btn = ctk.CTkButton(root, font=("Arial", 14, "bold"), width=200, height=40,
                    corner_radius=20, text="Confirm", command=calculate,
                    fg_color="#4C11BB", hover_color="#1A218A", text_color="white")
btn.pack(pady=5)

# Container for results box
result_frame = ctk.CTkFrame(root, fg_color="#320A6B", corner_radius=10)
result_frame.pack(pady=20, padx=20, fill="both", expand=True)

result_text = ctk.CTkTextbox(master=result_frame, wrap="word", font=("Arial", 15), 
                         fg_color="#D4CDDF", text_color="black", corner_radius=10,
                         scrollbar_button_color="#888888", state="disabled")
result_text.pack(expand=True, side="left", fill="both")


root.mainloop()