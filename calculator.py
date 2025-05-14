import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set the background color of the main window to black
root.configure(bg="black")

# Create an entry widget for the display
entry = tk.Entry(root, width=20, font=("Arial", 24), bd=5, insertwidth=4, justify='right', bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4)

# Update the entry widget's background and foreground colors to match the new theme
entry.configure(bg="black", fg="white")

# Define the button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Update the button styles to have black background and white text for numbers, with buttons closer together
for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        if button_text.isdigit():  # Numbers
            button = tk.Button(root, text=button_text, padx=15, pady=15, font=("Arial", 18), bg="black", fg="white", command=lambda text=button_text: on_click(text))
        else:  # Operators and special buttons
            button = tk.Button(root, text=button_text, padx=15, pady=15, font=("Arial", 18), bg="black", fg="red", command=lambda text=button_text: on_click(text))
        button.grid(row=i+1, column=j, padx=2, pady=2)

# Run the application
root.mainloop()