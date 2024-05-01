# Create a list
my_list = [1, 2, 3, 4, 5]


# append(): Adds an element to the end of the list
my_list.append(6)
print("List after append:", my_list)

# extend(): Extends the list by appending elements from the iterable
my_list.extend([7, 8])
print("List after extend:", my_list)

# insert(): Inserts an element at the specified index
my_list.insert(0, -1)
print("List after insert:", my_list)

# remove(): Removes the first occurrence of a value from the list
my_list.remove(-1)
print("List after remove:", my_list)

# pop(): Removes and returns the element at the specified index
popped_item = my_list.pop(1)
print("Popped item:", popped_item)
print("List after pop:", my_list)

# clear(): Removes all elements from the list
my_list.clear()
print("List after clear:", my_list)

# copy(): Returns a shallow copy of the list
new_list = [1, 2, 3, 4, 5]
copied_list = new_list.copy()
print("Copied list:", copied_list)

# reverse(): Reverses the elements of the list in place
new_list.reverse()
print("Reversed list:", new_list)

# sort(): Sorts the elements of the list in place
new_list.sort()
print("Sorted list:", new_list)

# __len__(): Returns the length of the list
print("__len__ method:", new_list.__len__())

# index(): Returns the index of the first occurrence of a value
print("Index of '3' in the list:", new_list.index(3))

# count(): Returns the number of occurrences of a value
print("Count of '2' in the list:", new_list.count(2))

# __add__(): Returns a new list by concatenating the original list and the added list
print("__add__ method:", new_list.__add__([6, 7]))

# __class__(): Returns the class of the list
print("Class of the list:", new_list.__class__)

# __getitem__(): Returns the element at index i
print("__getitem__ method:", new_list.__getitem__(2))

# __repr__(): Returns a string representation of the list
print("String representation of the list:", new_list.__repr__())

# __hash__(): Returns the hash value of the list
try:
    print("Hash value of the list:", new_list.__hash__())
except TypeError as e:
    print(f"__hash__ method:", e)

# __str__(): Returns a string representation of the list
print("String representation of the list:", new_list.__str__())

# __eq__(): Compares the list with another list for equality
print("Equality comparison with another list:", new_list.__eq__([1, 2, 3, 4, 5]))

# __ne__(): Compares the list with another list for not equality
print("Not equality comparison with another list:", new_list.__ne__([1, 2, 3, 4]))

# __lt__(): Compares the list with another list for less than
print("Less than comparison with another list:", new_list.__lt__([2, 3, 4, 5, 6]))

# __le__(): Compares the list with another list for less than or equal to
print("Less than or equal to comparison with another list:", new_list.__le__([1, 2, 3, 4, 5]))

# __gt__(): Compares the list with another list for greater than
print("Greater than comparison with another list:", new_list.__gt__([0, 1, 2, 3, 4]))

# __ge__(): Compares the list with another list for greater than or equal to
print("Greater than or equal to comparison with another list:", new_list.__ge__([1, 2, 3, 4, 5]))

# __iter__(): Returns an iterator over the elements of the list
iterator = new_list.__iter__()
print("Elements of the list using iterator:")
for item in iterator:
    print(item)

# __getitem__(): Returns the value at the specified index
print("Value at index 2:", new_list.__getitem__(2))

# __mul__(): Returns a new list with elements repeated a specified number of times
print("List multiplied by 2:", new_list.__mul__(2))

# __rmul__(): Returns a new list with elements repeated a specified number of times (reversed order)
print("2 multiplied by list:", new_list.__rmul__(2))

# __contains__(): Checks if a value is present in the list
print("Is 3 present in the list?", new_list.__contains__(3))


# Your additional methods here...
