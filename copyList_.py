import copy

# Creating an original list
l1 = [1, 2, 3]

# Copies of the original list
l2 = l1
l3 = l1[:]
l4 = l1.copy()
l5 = copy.deepcopy(l1)
lists = [l1, l2, l3, l4, l5]

def print_lists():
    for list in lists:
        print(list)

# Before modification of l1
print("# Before modification of l1")
print_lists()

# Modifying l1
l1.append(4)

# After modification of l1
print("# After modification of l1")
print_lists()

'''
# Displaying all lists after modification
print("Original list    (l1) : ", l1)       # Output: Original list    (l1) : [1, 2, 3, 4]
print("Assigning copy   (l2) : ", l2)       # Output: Assigning copy   (l2) : [1, 2, 3, 4]
print("Operator copy    (l3) : ", l3)       # Output: Operator copy    (l3) : [1, 2, 3]
print("Shallow copy     (l4) : ", l4)       # Output: Shallow copy     (l4) : [1, 2, 3]
print("Deep copy        (l5) : ", l5)       # Output: Deep copy        (l5) : [1, 2, 3]
'''