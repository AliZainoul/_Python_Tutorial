# Example of modifying the original list during iteration
original_list = [1, 2, 3, 4, 5]
for element in reversed(original_list):
    original_list.append(element * 2)
print(original_list)  # Output: [1, 2, 3, 4, 5, 10, 8, 6, 4, 2]

# Example of accessing elements by index during iteration
for index, element in enumerate(reversed(original_list)):
    print(f"Index: {index}, Element: {element}")

# Example of using list-specific methods during iteration
for element in reversed(original_list):
    if element % 2 == 0:
        original_list.remove(element)
print(original_list)  # Output: [1, 3, 5]

# Example of converting the iterator back to a list
list_reverseiterator_object = reversed(original_list)
reversed_list = list(list_reverseiterator_object)
print(reversed_list)  # Output: [5, 3, 1]