# Find intersection of two lists

list1 = [12, 13, 11, 15, 14, 1, 6, 1, 5, 14, 12]
list2 = [11, 12, 13, 1, 2, 3, 1, 3, 6, 7, 9, 12]

intersection = []

for item in list1:
    if item in list2 and item not in intersection:
        intersection.append(item)

print(f"Intersection: {intersection}")
