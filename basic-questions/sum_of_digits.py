# Calculate sum of digits of a number

num = input("Enter a number: ")
sum_digits = 0

for digit in num:
    sum_digits += int(digit)

print(f"Sum of digits: {sum_digits}")
