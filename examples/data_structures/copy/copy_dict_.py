import copy

# Creating an original dictionary
d1 = {'a': 1, 'b': 2, 'c': 3}

# Copies of the original dictionary
d2 = d1
# d3 = d1[:] # TypeError: unhashable type: 'slice'
d4 = d1.copy()
d5 = copy.deepcopy(d1)
dicts = [d1, d2, d4, d5]

def print_dicts():
    for dict in dicts:
        print(dict)

# Before modifying d1
print("# Before modifying d1")
print_dicts()

# Modifying d1
d1['d'] = 4

# After modifying d1
print("# After modifying d1")
print_dicts()

'''
# Displaying all dictionaries after modification
print("Original dict    (d1) : ", d1)       # Output: Original dict     (d1) : {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Assigning copy   (d2) : ", d2)       # Output: Assigning copy    (d2) : {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Shallow copy     (d4) : ", d4)       # Output: Shallow copy      (d4) : {'a': 1, 'b': 2, 'c': 3}
print("Deep copy        (d5) : ", d5)       # Output: Deep copy         (d5) : {'a': 1, 'b': 2, 'c': 3}
'''