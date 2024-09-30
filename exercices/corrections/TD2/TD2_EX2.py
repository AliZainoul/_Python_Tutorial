def demonstrate_id():
    """
    Demonstrates the use of the id() function to display the unique memory address (identifier) of objects.
    """
    string_1 = "hello"
    string_2 = "world"
    tuple_1 = (1, 2, 3)
    tuple_2 = (4, 5, 6)

    # Displaying unique memory IDs using id()
    print(f"ID of string_1 ('hello'): {id(string_1)}")
    print(f"ID of string_2 ('world'): {id(string_2)}")
    print(f"ID of tuple_1 ((1, 2, 3)): {id(tuple_1)}")
    print(f"ID of tuple_2 ((4, 5, 6)): {id(tuple_2)}")

def demonstrate_hash():
    """
    Demonstrates the use of the hash() function to create a dictionary with immutable objects (strings, tuples) as keys.
    """
    # Creating a dictionary with strings and tuples as keys
    hash_dict = {
        "hello": "greeting",
        "world": "planet",
        (1, 2, 3): "tuple one",
        (4, 5, 6): "tuple two"
    }

    # Displaying the hash values of the keys
    print("\nHash values of the dictionary keys:")
    for key in hash_dict:
        print(f"Hash of {key}: {hash(key)}")

    # Accessing dictionary elements by their hashable keys
    print("\nAccessing elements in the dictionary using hashable keys:")
    print(f"Value for key 'hello': {hash_dict['hello']}")
    print(f"Value for key (1, 2, 3): {hash_dict[(1, 2, 3)]}")

def main():
    """
    Main function to run the id() and hash() demonstrations.
    """
    print("Demonstration of id() function:")
    demonstrate_id()

    print("\nDemonstration of hash() function:")
    demonstrate_hash()

if __name__ == "__main__":
    main()
