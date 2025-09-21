# Reverse a string without using slicing

text = input("Enter a string to reverse: ")
reversed_text = ""

for i in range(len(text)-1, -1, -1):
    reversed_text += text[i]

print(f"Reversed string: {reversed_text}")
