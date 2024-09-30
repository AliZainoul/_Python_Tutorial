import sys

def memory_usage(obj):
    """
    Returns the memory usage of an object in bytes.
    
    Args:
        obj: The object whose memory size needs to be measured.
    
    Returns:
        int: The size of the object in bytes.
    """
    return sys.getsizeof(obj)

def create_large_list_of_strings(size: int):
    """
    Create a large list of strings with the format 'string_i'.
    
    Args:
        size (int): The number of strings to create.
    
    Returns:
        list: A list of strings with 'string_i' format.
    """
    return [f"string_{i}" for i in range(size)]

def create_large_list_of_tuples(size: int):
    """
    Create a large list of tuples with the format (i, f'string_{i}').
    
    Args:
        size (int): The number of tuples to create.
    
    Returns:
        list: A list of tuples with the format (i, 'string_i').
    """
    return [(f"string_{i}") for i in range(size)]

def main():
    SIZE = 1_000_000  # SIZE of the lists

    # Create the large lists
    list_of_strings = create_large_list_of_strings(SIZE)
    list_of_tuples = create_large_list_of_tuples(SIZE)

    # Measure the memory usage of both lists
    strings_memory = memory_usage(list_of_strings)
    tuples_memory = memory_usage(list_of_tuples)

    print(f"Memory usage for list of {SIZE} strings: {strings_memory / 1024 / 1024:.2f} MB")
    print(f"Memory usage for list of {SIZE} tuples: {tuples_memory / 1024 / 1024:.2f} MB")

    # Individual SIZE of elements in both lists
    print(f"SIZE of an individual string: {memory_usage(list_of_strings[0])} bytes")
    print(f"SIZE of an individual tuple: {memory_usage(list_of_tuples[0])} bytes")

if __name__ == "__main__":
    main()
