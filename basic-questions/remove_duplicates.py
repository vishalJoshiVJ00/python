# Remove duplicates from a list without using set()

numbers = [1, 1, 2, 4, 5, 6, 2, 3, 4, 6, 8, 6, 4, 3, 3, 5, 57, 8]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f"List without duplicates: {unique_numbers}")
