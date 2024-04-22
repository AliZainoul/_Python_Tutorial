import copy

l1 = [1, 2, 3]
l2 = l1
l3 = l1[:]
l4 = l1.copy()
l5 = copy.deepcopy(l1)
# Before modification of l1
print("# Before modification of l1")
for el in [l1, l2, l3, l4, l5]:
    print(el)

l1[0] = 10
# After modification of l1
print("# After modification of l1")
for el in [l1, l2, l3, l4, l5]:
    print(el)


'''
# Displaying all lists
print("Original list:", l1)  # Output: Original list: [10, 2, 3]
print("Assigning copy (l2):", l2)  # Output: Assigning copy (l2): [10, 2, 3]
print("Operator copy (l3):", l3)  # Output: Operator copy (l3): [1, 2, 3]
print("Shallow copy (l4):", l4)  # Output: Shallow copy (l4): [1, 2, 3]
print("Deep copy (l5):", l5)  # Output: Deep copy (l5): [1, 2, 3]
'''