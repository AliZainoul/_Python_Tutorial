# Ask the user to input the number of tuples they want to provide.
N: int = int(input("Please enter a number N: \n"))

# Collect N tuples from the user's input, where each input is split into components and stored as a tuple of strings.
# The list comprehension generates a list of string tuples.
list_of_strs: list[tuple[str]] = \
    [input(f"Please enter tuple number {i+1} : \n").split() for i in range(N)]

def to_float_tuple(col: tuple[str]) -> tuple[float]:
    """
    Converts a tuple of strings into a tuple of floats.
    
    Args:
        col (tuple[str]): A tuple of strings representing numeric values.
        
    Returns:
        tuple[float]: A tuple where each string element is converted into a float.
        
    Example:
        Input: ('3', '4', '5')
        Output: (3.0, 4.0, 5.0)
    """
    # Convert each string element in the tuple to a float and return a new tuple of floats.
    tuple_of_floats: tuple[float] = tuple([float(el) for el in col])
    return tuple_of_floats

def inputs_to_list_of_tuple_of_floats(col: list[tuple[str]]) -> list[tuple[float]]:
    """
    Converts a list of string tuples into a list of float tuples.
    
    Args:
        col (list[tuple[str]]): A list where each element is a tuple of strings representing numeric values.
    
    Returns:
        list[tuple[float]]: A list where each tuple of strings is converted into a tuple of floats.
        
    Example:
        Input: [('1', '2'), ('3', '4')]
        Output: [(1.0, 2.0), (3.0, 4.0)]
    """
    # Apply `to_float_tuple` to each tuple in the input list and return the result.
    list_of_float_tuples: list[tuple[float]] = [to_float_tuple(tup) for tup in col]
    return list_of_float_tuples

# Convert the list of string tuples into a list of float tuples using the `inputs_to_list_of_tuple_of_floats` function.
list_of_tuples = inputs_to_list_of_tuple_of_floats(list_of_strs)

# sorting the list of float tuples by the second element (index 1) in each tuple.
sorted_list = sorted(list_of_tuples, key=lambda tup: tup[1])

# Print the results of the three sorting attempts.
print(sorted_list)
