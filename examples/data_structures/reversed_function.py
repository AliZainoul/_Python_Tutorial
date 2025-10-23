# Example with a string
my_string = "Hello"
my_string_reversed = reversed(my_string)
print(type(my_string_reversed))
# Output: <class 'reversed'>
for char in my_string_reversed:
    print(char)

# Example with a tuple
my_tuple = (1, 2, 3, 4, 5)
my_tuple_reversed = reversed(my_tuple)
print(type(my_tuple_reversed))
# Output: <class 'reversed'>
for value in my_tuple_reversed:
    print(value)
    
# Example with a list
my_list = [1, 2, 3, 4, 5]
my_list_reversed = reversed(my_list)
print(type(my_list_reversed))
# Output: <class 'list_reverseiterator'>
for element in my_list_reversed:
    print(element)

# WE CANNOT REVERSE A SET