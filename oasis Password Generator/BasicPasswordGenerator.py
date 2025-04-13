import random
import string

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

# Get user input for password length
try:
    length = int(input("Enter desired password length: "))
    if length <= 0:
        print("Password length must be a positive number!")
    else:
        # Ask user for character types
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Your random password: {password}")

except ValueError:
    print("Please enter a valid number for the password length!")
