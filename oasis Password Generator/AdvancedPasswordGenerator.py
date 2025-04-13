import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected!"
    
    return ''.join(random.choice(characters) for _ in range(length))

# Function to handle button click
def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive number!")
            return

        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        if password == "Error: No character set selected!":
            messagebox.showerror("Error", password)
        else:
            result_label.config(text=f"Generated Password: {password}", fg="green")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length!")

# Create the main window
app = tk.Tk()
app.title("Password Generator")
app.geometry("500x500")
app.resizable(True, True)

# UI Elements
title_label = tk.Label(app, text="Password Generator", font=("Arial", 20))
title_label.pack(pady=10)

length_label = tk.Label(app, text="Enter desired password length:")
length_label.pack(pady=5)

length_entry = tk.Entry(app)
length_entry.pack(pady=5)

# Checkboxes for character types
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

letters_check = tk.Checkbutton(app, text="Include Letters", variable=letters_var)
letters_check.pack()

numbers_check = tk.Checkbutton(app, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

symbols_check = tk.Checkbutton(app, text="Include Symbols", variable=symbols_var)
symbols_check.pack()

# Generate button
generate_button = tk.Button(app, text="Generate Password", command=generate, bg="green", fg="white")
generate_button.pack(pady=10)

# Result label
result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the app
app.mainloop()
