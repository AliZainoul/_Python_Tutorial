# Create a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])

# __len__(): Returns the number of elements in the frozenset
print("__len__ method:", my_frozenset.__len__())

# __iter__(): Returns an iterator over the elements of the frozenset
iterator = my_frozenset.__iter__()
print("Elements of the frozenset using iterator:")
for item in iterator:
    print(item)

# __contains__(): Checks if a value is present in the frozenset
print("Is 3 present in the frozenset?", my_frozenset.__contains__(3))

# isdisjoint(): Checks if two sets have no elements in common
other_set = {6, 7, 8}
print("Is the frozenset disjoint from another set?", my_frozenset.isdisjoint(other_set))

# issubset(): Checks if all elements of the frozenset are present in another set
print("Is the frozenset a subset of another set?", my_frozenset.issubset({1, 2, 3, 4, 5, 6}))

# __eq__(): Compares the frozenset with another frozenset for equality
print("Equality comparison with another frozenset:", my_frozenset.__eq__(frozenset([1, 2, 3, 4, 5])))

# __ne__(): Compares the frozenset with another frozenset for not equality
print("Not equality comparison with another frozenset:", my_frozenset.__ne__(frozenset([1, 2, 3, 4])))

# __lt__(): Compares the frozenset with another frozenset for less than
print("Less than comparison with another frozenset:", my_frozenset.__lt__(frozenset([1, 2, 3, 4, 5, 6])))

# __le__(): Compares the frozenset with another frozenset for less than or equal to
print("Less than or equal to comparison with another frozenset:", my_frozenset.__le__(frozenset([1, 2, 3, 4, 5])))

# __gt__(): Compares the frozenset with another frozenset for greater than
print("Greater than comparison with another frozenset:", my_frozenset.__gt__(frozenset([1, 2, 3, 4])))

# __ge__(): Compares the frozenset with another frozenset for greater than or equal to
print("Greater than or equal to comparison with another frozenset:", my_frozenset.__ge__(frozenset([1, 2, 3, 4, 5])))

# __repr__(): Returns a string representation of the frozenset
print("String representation of the frozenset:", my_frozenset.__repr__())

# __hash__(): Returns the hash value of the frozenset
print("Hash value of the frozenset:", my_frozenset.__hash__())