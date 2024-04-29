# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# len(): Returns the length of the tuple
print("Length of the tuple:", len(my_tuple))

# index(): Returns the index of the first occurrence of a value
print("Index of '3' in the tuple:", my_tuple.index(3))

# count(): Returns the number of occurrences of a value
print("Count of '2' in the tuple:", my_tuple.count(2))

# __class__(): Returns the class of the tuple
print("Class of the tuple:", my_tuple.__class__())

# __repr__(): Returns a string representation of the tuple
print("String representation of the tuple:", my_tuple.__repr__())

# __hash__(): Returns the hash value of the tuple
print("Hash value of the tuple:", my_tuple.__hash__())

# __str__(): Returns a string representation of the tuple
print("String representation of the tuple:", my_tuple.__str__())

# __eq__(): Compares the tuple with another tuple for equality
print("Equality comparison with another tuple:", my_tuple.__eq__((1, 2, 3, 4, 5)))

# __lt__(): Compares the tuple with another tuple for less than
print("Less than comparison with another tuple:", my_tuple.__lt__((2, 3, 4, 5, 6)))

# __le__(): Compares the tuple with another tuple for less than or equal to
print("Less than or equal to comparison with another tuple:", my_tuple.__le__((1, 2, 3, 4, 5)))

# __gt__(): Compares the tuple with another tuple for greater than
print("Greater than comparison with another tuple:", my_tuple.__gt__((0, 1, 2, 3, 4)))

# __ge__(): Compares the tuple with another tuple for greater than or equal to
print("Greater than or equal to comparison with another tuple:", my_tuple.__ge__((1, 2, 3, 4, 5)))

# __iter__(): Returns an iterator over the elements of the tuple
iterator = my_tuple.__iter__()
print("Elements of the tuple using iterator:")
for item in iterator:
    print(item)

# __getitem__(): Returns the value at the specified index
print("Value at index 2:", my_tuple.__getitem__(2))

# __mul__(): Returns a new tuple with elements repeated a specified number of times
print("Tuple multiplied by 2:", my_tuple.__mul__(2))

# __rmul__(): Returns a new tuple with elements repeated a specified number of times (reversed order)
print("2 multiplied by tuple:", my_tuple.__rmul__(2))

# __contains__(): Checks if a value is present in the tuple
print("Is 3 present in the tuple?", my_tuple.__contains__(3))

