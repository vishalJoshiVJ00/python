# Basic list operations in Python

# Define a list with numbers and strings
my_list = [1, 2, 3, "v", "j"]

# Print entire list
print(my_list)

# Accessing elements by index
print(my_list[0])  # First element
print(my_list[1])  # Second element
print(my_list[2])  # Third element

# Print last 3 elements using slicing
for item in my_list[-3:]:
    print(item)
    
# Check if an element exists in the list
if "v" in my_list:
    print("yes")
else:
    print("no")

# List comprehension example: square of even numbers from 1–10
squared_evens = [(i + 1) ** 2 for i in range(10) if i % 2 == 0]
print(squared_evens)
