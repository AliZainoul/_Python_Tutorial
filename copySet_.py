import copy

# Creating an original set
s1 = {1, 2, 3}

# Copies of the original set
s2 = s1
# s3 = s1[:] # Set objects are not subscriptable
s4 = s1.copy()
s5 = copy.deepcopy(s1)
sets = [s1, s2, s4, s5]

def print_sets():
    for set in sets:
        print(set)

# Before modification of s1
print("# Before modification of s1")
print_sets()

# Modifying s1
s1.add(4)

# After modification of s1
print("# After modification of s1")
print_sets()

'''
# Displaying all sets after modification
print("Original set     (s1) : ", s1)       # Output: Original set     (s1) : {1, 2, 3, 4}
print("Assigning copy   (s2) : ", s2)       # Output: Assigning copy   (s2) : {1, 2, 3, 4}
print("Shallow copy     (s4) : ", s4)       # Output: Shallow copy     (s4) : {1, 2, 3}
print("Deep copy        (s5) : ", s5)       # Output: Deep copy        (s5) : {1, 2, 3}
'''