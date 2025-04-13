import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive numbers!")
            return

        bmi = weight / (height ** 2)
        category = get_bmi_category(bmi)

        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}", fg="blue")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for weight and height!")


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Create the main window
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("300x400")
app.resizable(False, False)

# Create UI elements
title_label = tk.Label(app, text="BMI Calculator", font=("Arial", 20))
title_label.pack(pady=10)

weight_label = tk.Label(app, text="Enter your weight (kg):")
weight_label.pack(pady=5)

weight_entry = tk.Entry(app)
weight_entry.pack(pady=5)

height_label = tk.Label(app, text="Enter your height (m):")
height_label.pack(pady=5)

height_entry = tk.Entry(app)
height_entry.pack(pady=5)

calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi, bg="green", fg="white")
calculate_button.pack(pady=20)

result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the app
app.mainloop()
