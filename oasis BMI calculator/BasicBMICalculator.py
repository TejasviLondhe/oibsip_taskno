def calculate_bmi(weight, height):
    return weight / (height ** 2)

# BMI categories
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Get user input with validation
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers!")
    else:
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        # Display result
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

except ValueError:
    print("Please enter valid numeric values for weight and height!")
