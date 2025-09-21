# Count vowels in a given string

text = input("Enter your text: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = 0

for char in text.lower():
    if char in vowels:
        count_vowels += 1

print(f"Number of vowels: {count_vowels}")
