import tkinter as tk
from tkinter import messagebox
import re

def safe_eval(expression):
 
    if not re.match(r'^[0-9+\-*/(). ]+$', expression):
        raise ValueError("Invalid characters in input")
    return eval(expression)

def on_click(button_text):
    if button_text == "=":
        try:
            result = safe_eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")


root.configure(bg="black")

entry = tk.Entry(root, width=20, font=("Arial", 24), bd=5, insertwidth=4, justify='right', bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4)

entry.configure(bg="black", fg="white")

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        if button_text.isdigit():  # Numbers
            button = tk.Button(root, text=button_text, padx=15, pady=15, font=("Arial", 18), bg="black", fg="white", command=lambda text=button_text: on_click(text))
        else:  # Operators and special buttons
            button = tk.Button(root, text=button_text, padx=15, pady=15, font=("Arial", 18), bg="black", fg="red", command=lambda text=button_text: on_click(text))
        button.grid(row=i+1, column=j, padx=2, pady=2)

root.mainloop()