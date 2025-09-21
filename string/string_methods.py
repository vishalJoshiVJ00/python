# Demonstrating multiple string methods

email = "vishaljoshi0@gmail.com"

print(email.capitalize())  # Capitalize first letter
print(len(email.center(50)))  # Center the string with padding
print(len(email))  # Length of the string
print(email.count("l"))  # Count occurrences of 'l'

# Checking start and end
print(email.endswith("@gmail.com"))
print(email.startswith("vishaljoshi"))

# Find index of a character
print(email.find("o"))

# Check string properties
print(email.isalnum())  # False (because it contains '@' and '.')
print(email.islower())  # True if all characters are lowercase
