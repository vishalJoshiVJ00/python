# Demonstrating add, discard, remove in sets

s1 = {1, 2, 8, 5, 67, 6, 9, 12}

# Add an element
s1.add(33)
print("After add:", s1)

# Discard removes element if present, no error if not
s1.discard(33)
print("After discard:", s1)

# Remove element (raises error if element not found)
try:
    s1.remove(333)  # 333 is not present
except KeyError:
    print("Element 333 not found, remove() raised KeyError")

print("Final set:", s1)
