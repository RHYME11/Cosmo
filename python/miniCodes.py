import os


# Separate the numeric part (mass number) and the alphabetic part (isotope symbol)
def get_isotope_details(isotope_str):
    isotope_A = ''.join(filter(str.isdigit, isotope_str))
    isotope_symbol = ''.join(filter(str.isalpha, isotope_str))
    
    return isotope_symbol, int(isotope_A)


# Function to validate float input
def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Warning: Please enter a valid number!")

# Turn number to #th
def ordinal(n):
    # Handle the special cases for 11th, 12th, and 13th
    if 11 <= n % 100 <= 13:
        suffix = 'th'
    else:
        # Assign suffix based on the last digit
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

