# Example of enumerate constructor usage

# Creating a list of fruits
fruits : list[str] = ['apple', 'banana', 'cherry']

# Printing the enumerate object and its type
print(f"Enumerating fruits: {enumerate(fruits)}") # Outputs the enumerate object <enumerate object at 0x10fcd2160>
print(f"Type of enumerate object: {type(enumerate(fruits))}") # Outputs <class 'enumerate'>

# Converting enumerate object to a list of tuples
print(f"Enumerating fruits: {list(enumerate(fruits))}") # Outputs [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# Printing the type of the first element in the list of tuples
print(f"Type of first element of list(enumerate(fruits)) : {type(list(enumerate(fruits))[0])}") # Outputs <class 'tuple'>

# Using enumerate in a for loop
for index, fruit in enumerate(fruits):
    print(index, fruit)
