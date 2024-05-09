# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# keys(): Returns a view of all the keys in the dictionary
print("Keys of the dictionary:", my_dict.keys())

# values(): Returns a view of all the values in the dictionary
print("Values of the dictionary:", my_dict.values())

# items(): Returns a view of all key-value pairs in the dictionary
print("Items of the dictionary:", my_dict.items())

# get(): Returns the value associated with the specified key
print("Value of key 'b':", my_dict.get('b'))

# pop(): Removes the item with the specified key and returns its value
popped_value = my_dict.pop('b')
print("Popped value:", popped_value)
print("Dictionary after pop:", my_dict)

# popitem(): Removes and returns an arbitrary key-value pair from the dictionary
popped_item = my_dict.popitem()
print("Popped item:", popped_item)
print("Dictionary after popitem:", my_dict)

# clear(): Removes all items from the dictionary
my_dict.clear()
print("Dictionary after clear:", my_dict)

# copy(): Returns a shallow copy of the dictionary
new_dict = {'x': 10, 'y': 20}
copied_dict = new_dict.copy()
print("Copied dictionary:", copied_dict)

# update(): Updates the dictionary with key-value pairs from another dictionary or iterable
new_dict.update({'z': 30})
print("Updated dictionary:", new_dict)

# fromkeys(): Returns a new dictionary with keys from a sequence and values set to a default value
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print("Dictionary from keys:", new_dict)

# __len__(): Returns the number of items in the dictionary
print("__len__ method:", new_dict.__len__())

# __getitem__(): Returns the value associated with the specified key
print("__getitem__ method:", new_dict.__getitem__('a'))

# __contains__(): Checks if a key is present in the dictionary
print("Is 'b' present in the dictionary?", new_dict.__contains__('b'))

# __eq__(): Compares the dictionary with another dictionary for equality
print("Equality comparison with another dictionary:", new_dict.__eq__({'a': 0, 'b': 0, 'c': 0}))

# __ne__(): Compares the dictionary with another dictionary for not equality
print("Not equality comparison with another dictionary:", new_dict.__ne__({'a': 0, 'b': 1, 'c': 0}))

# __repr__(): Returns a string representation of the dictionary
print("String representation of the dictionary:", new_dict.__repr__())

# __str__(): Returns a string representation of the dictionary
print("String representation of the dictionary:", new_dict.__str__())

# __hash__(): Returns the hash value of the dictionary
try:
    print("Hash value of the dictionary:", new_dict.__hash__())
except TypeError as e:
    print(f"__hash__ method:", e)