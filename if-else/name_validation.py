# Program to validate a full name (first and last name)

name = input("Enter your full name (e.g., John Doe): ")

# Check if first character is uppercase
first_upper = name[0].isupper()

# Check if there is exactly one space
space_count = name.count(" ")

# Flag to check if first letter after space is uppercase
after_upper = False

# Flag to check if name contains digits
has_no_digits = True

# Iterate over characters
for i, char in enumerate(name):
    if char.isdigit():
        has_no_digits = False
    elif char == " " and i + 1 < len(name):
        if name[i + 1].isupper():
            after_upper = True

# Validation conditions
if first_upper and after_upper and has_no_digits and space_count == 1:
    print("Valid name")
else:
    print("Invalid name")
