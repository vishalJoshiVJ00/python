# Print Fibonacci sequence up to n terms

n = int(input("Enter number of terms: "))
a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
