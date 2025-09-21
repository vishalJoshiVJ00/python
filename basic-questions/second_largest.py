# Find the second largest element in a list

numbers = [14, 12, 12, 13, 150, 90, 203, 67, 96]

first_max = max(numbers)
second_max = None

for num in numbers:
    if num != first_max:
        if second_max is None or num > second_max:
            second_max = num

print(f"First largest: {first_max}")
print(f"Second largest: {second_max}")
