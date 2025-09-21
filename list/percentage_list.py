# Creating a list with user input and adding 10% to each number

numbers_with_bonus = []  # Empty list

# Input length of list
length = int(input("Enter the length of the list: "))

# Loop to take numbers as input
for i in range(length):
    num = int(input("Enter a number: "))
    ten_percent = num * 10 / 100
    numbers_with_bonus.append(num + ten_percent)

print(numbers_with_bonus)
