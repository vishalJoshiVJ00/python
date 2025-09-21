# Common set operations

s1 = {1, 2, 8, 5, 67, 6, 9, 12}
s2 = {1, 2, 5, 8, 6, 12, 89}

# Union of sets
print("Union:", s1.union(s2))

# Intersection of sets
print("Intersection:", s1.intersection(s2))

# Difference of sets
print("Difference (s1 - s2):", s1.difference(s2))

# Symmetric difference (elements not common in both)
print("Symmetric Difference:", s1.symmetric_difference(s2))

# Update operations (change the original set)
s1_copy = s1.copy()
s1_copy.intersection_update(s2)
print("Intersection Update:", s1_copy)

s1_copy = s1.copy()
s1_copy.difference_update(s2)
print("Difference Update:", s1_copy)

# Checking relationships
print("Is disjoint?:", s1.isdisjoint(s2))
print("Is s1 a superset of s2?:", s1.issuperset(s2))
print("Is s1 a subset of s2?:", s1.issubset(s2))
