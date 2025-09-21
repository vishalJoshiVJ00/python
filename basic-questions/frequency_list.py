# Find the frequency of each element in a list

numbers = []
for _ in range(6):
    n = int(input("Enter a number: "))
    numbers.append(n)

for num in set(numbers):
    print(f"{num}: {numbers.count(num)}")
