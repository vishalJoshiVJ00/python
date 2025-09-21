# Sort a list without using built-in sort()

numbers = [1, 1, 5, 3, 0, 2, 9, 7]
sorted_list = []

while numbers:
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    sorted_list.append(min_value)
    numbers.remove(min_value)

print(f"Sorted list: {sorted_list}")
