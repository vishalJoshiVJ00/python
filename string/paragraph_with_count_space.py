paragraph = input("enter the paragraph")
paragraph_to_list = paragraph.split(" ")
for i in range(len(paragraph)):
    if paragraph[i]==".":
        paragraph[i+2].upper()
space_of_paragraph = len(paragraph_to_list) - 1
print(paragraph)
print(space_of_paragraph)