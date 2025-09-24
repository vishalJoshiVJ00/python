# Program: Capitalize first letter after '.' and count spaces in a paragraph

# Take paragraph input from user
paragraph = input("Enter the paragraph: ")

# Variable to count spaces
space_count = 0

# Convert string to list of characters (strings are immutable in Python)
char_list = list(paragraph)

# Loop through characters
for i in range(len(char_list) - 2):   # -2 to avoid index error
    # If character is a full stop
    if char_list[i] == '.':
        # Case 1: dot followed by a space
        if char_list[i+1] == ' ':
            char_list[i+2] = char_list[i+2].upper()
        # Case 2: dot directly followed by a letter
        else:
            char_list[i+1] = char_list[i+1].upper()
    
    # Count spaces
    if char_list[i] == ' ':
        space_count += 1

# Check last character for space
if char_list[-1] == ' ':
    space_count += 1

# Convert list back to string
modified_paragraph = "".join(char_list)

# Print results
print("Modified paragraph:", modified_paragraph)
print("Number of spaces:", space_count)
