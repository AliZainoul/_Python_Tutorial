import copy

# Creating an original dictionary
d1 = {'a': 1, 'b': 2, 'c': 3}

# Copies of the original dictionary
d2 = d1
d3 = d1.copy()
d4 = copy.deepcopy(d1)

# Before modifying d1
print("# Before modifying d1")
for el in [d1, d2, d3, d4]:
    print(el)

# Modifying d1
d1['a'] = 10

# After modifying d1
print("# After modifying d1")
for el in [d1, d2, d3, d4]:
    print(el)

'''
# Displaying all dictionaries
print("Original dictionary:", d1)  # Output: Original dictionary: {'a': 10, 'b': 2, 'c': 3}
print("Assigning copy (d2):", d2)  # Output: Assigning copy (d2): {'a': 10, 'b': 2, 'c': 3}
print("Shallow copy (d3):", d3)  # Output: Shallow copy (d3): {'a': 1, 'b': 2, 'c': 3}
print("Deep copy (d4):", d4)  # Output: Deep copy (d4): {'a': 1, 'b': 2, 'c': 3}
'''
