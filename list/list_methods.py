# Demonstrating different list methods

numbers = [11, 5, 10, 48, 5, 6]

# Append new element at the end
numbers.append(9)
print(numbers)

# Sort the list in descending order
numbers.sort(reverse=True)
print(numbers)

# Find index of an element
print(numbers.index(10))

# Count frequency of a value
print(numbers.count(5))

# Copy list and modify copy (original remains same)
copy_numbers = numbers.copy()
copy_numbers[0] = 13
print("Original:", numbers)
print("Copy:", copy_numbers)

# Insert element at specific index
numbers.insert(5, 12)
print(numbers)

# Extend list with another list
extra_numbers = [123, 124, 125]
numbers.extend(extra_numbers)
print(numbers)
