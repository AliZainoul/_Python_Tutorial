# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# __len__(): Returns the length of the tuple
print("__len__ method:", my_tuple.__len__())
# equivalent to: print("__len__ method:", len(my_tuple))

# index(): Returns the index of the first occurrence of a value
print("Index of '3' in the tuple:", my_tuple.index(3))

# count(): Returns the number of occurrences of a value
print("Count of '2' in the tuple:", my_tuple.count(2))

# print("__dir__ method:", dir(my_tuple))
# print("__doc__ attribute:", my_tuple.__doc__)

# __add__(): Returns a new tuple by concatenating the original tuple and the added tuple
print("__add__ method:", my_tuple.__add__((6, 7)))  # return a new tuple
# equivalent to: print("__add__ method:", my_tuple+(6, 7))  # return a new tuple

# __class__(): Returns the class of the tuple
print("Class of the tuple:", my_tuple.__class__)
# equivalent to: print("Class of the tuple:", type(my_tuple))

# __getitem__(): Returns the element at index i 
print("__getitem__ method:", my_tuple.__getitem__(2))
# equivalent to: print("__getitem__ method:", my_tuple[2])

# __repr__(): Returns a string representation of the tuple
print("String representation of the tuple:", my_tuple.__repr__())
# equivalent to: print("String representation of the tuple:", repr(my_tuple))

# __hash__(): Returns the hash value of the tuple
print("Hash value of the tuple:", my_tuple.__hash__())
# equivalent to: print("Hash value of the tuple:", hash(my_tuple))

# __str__(): Returns a string representation of the tuple
print("String representation of the tuple:", my_tuple.__str__())
# equivalent to: print("String representation of the tuple:", str(my_tuple))

# __eq__(): Compares the tuple with another tuple for equality
print("Equality comparison with another tuple:", my_tuple.__eq__((1, 2, 3, 4, 5)))
# equivalent to: print("Equality comparison with another tuple:", (my_tuple == (1, 2, 3, 4, 5)))

# __ne__(): Compares the tuple with another tuple for not equality
print("Not equality comparison with another tuple:", my_tuple.__ne__((1, 2, 3, 4)))
# equivalent to: print("__ne__ method:", my_tuple != (1, 2, 3, 4))

# __lt__(): Compares the tuple with another tuple for less than
print("Less than comparison with another tuple:", my_tuple.__lt__((2, 3, 4, 5, 6)))
# equivalent to: print("Less than comparison with another tuple:", (my_tuple <(2, 3, 4, 5, 6)))

# __le__(): Compares the tuple with another tuple for less than or equal to
print("Less than or equal to comparison with another tuple:", my_tuple.__le__((1, 2, 3, 4, 5)))
# equivalent to: print("Less than or equal to comparison with another tuple:", (my_tuple <= (1, 2, 3, 4, 5)))

# __gt__(): Compares the tuple with another tuple for greater than
print("Greater than comparison with another tuple:", my_tuple.__gt__((0, 1, 2, 3, 4)))
# equivalent to: print("Greater than comparison with another tuple:", (my_tuple > (0, 1, 2, 3, 4)))

# __ge__(): Compares the tuple with another tuple for greater than or equal to
print("Greater than or equal to comparison with another tuple:", my_tuple.__ge__((1, 2, 3, 4, 5)))
# equivalent to: print("Greater than or equal to comparison with another tuple:", (my_tuple >= (1, 2, 3, 4, 5)))

# __iter__(): Returns an iterator over the elements of the tuple
iterator = my_tuple.__iter__()
print("Elements of the tuple using iterator:")
for item in iterator:
    print(item)

# __getitem__(): Returns the value at the specified index
print("Value at index 2:", my_tuple.__getitem__(2))

# __mul__(): Returns a new tuple with elements repeated a specified number of times
print("Tuple multiplied by 2:", my_tuple.__mul__(2))
# equivalent to: print("Tuple multiplied by 2:", my_tuple*2)

# __rmul__(): Returns a new tuple with elements repeated a specified number of times (reversed order)
print("2 multiplied by tuple:", my_tuple.__rmul__(2))
# equivalent to: print("2 multiplied by tuple:", 2*my_tuple)

# __contains__(): Checks if a value is present in the tuple
print("Is 3 present in the tuple?", my_tuple.__contains__(3))
# equivalent to: print("Is 3 present in the tuple?", (3 in my_tuple))


"""
import sys

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# __getattribute__(): Retrieves an attribute value by name
print("__getattribute__ method:", my_tuple.__getattribute__('__class__'))

# __getnewargs__(): Returns the tuple's content as a new tuple
print("__getnewargs__ method:", my_tuple.__getnewargs__())

# __iter__(): Returns an iterator over the elements of the tuple
print("__iter__ method:")
for item in my_tuple:
    print(item)

# __sizeof__(): Returns the size of the tuple in bytes
print("__sizeof__ method:", my_tuple.__sizeof__())  # Returns size in bytes, memory occupied by the tuple
# Note: The size reported by __sizeof__() may include some additional memory overhead beyond just the elements.

# __delattr__(): Deletes an attribute
try:
    my_tuple.__delattr__("1")  # Attempting to delete an attribute
except AttributeError as e:
    print(f"__delattr__ method:", e)  # Output: AttributeError: 'tuple' object has no attribute '1'

# __format__(): Returns a formatted representation of the tuple
print("__format__ method:", my_tuple.__format__('^10'))  # Output: ('^1', '^2', '^3', '^4', '^5')

# __init__(): Initializes the tuple with the provided values
print("__init__ method:", my_tuple.__init__((1, 2, 3)))  # Output: None (initializes successfully)

# __init_subclass__(): Invoked when a subclass is instantiated
print("__init_subclass__ method:", my_tuple.__init_subclass__)  # Output: <built-in method __init_subclass__ of type object at 0x7f7f13a4d140>

# __reduce__(): Returns a stateful representation of the tuple for pickling
print("__reduce__ method:", my_tuple.__reduce__())

# __reduce_ex__(): Returns a stateful representation of the tuple for pickling with additional protocol
print("__reduce_ex__ method:", my_tuple.__reduce_ex__(2))

# __setattr__(): Sets the value of an attribute
try:
    my_tuple.__setattr__('attr', 10)  # Attempting to set an attribute
except AttributeError as e:
    print(f"    AttributeError:", e)  # Output: AttributeError: 'tuple' object has no attribute '__setattr__'

"""