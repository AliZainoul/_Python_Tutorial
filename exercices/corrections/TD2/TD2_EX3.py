def compare_objects():
    """
    Compares different objects using the 'is' operator and explains the difference between 'is' and '=='.
    """
    # Integer comparison
    a = 100
    b = 100
    print(f"a is b: {a is b}")  # True, small integers are cached by Python
    print(f"a == b: {a == b}")  # True, values are equal

    # String comparison
    string1 = "hello"
    string2 = "hello"
    print(f"\nstring1 is string2: {string1 is string2}")  # True, identical string literals are interned
    print(f"string1 == string2: {string1 == string2}")    # True, values are equal

    # Tuple comparison
    tuple1 = (1, 2, 3)
    tuple2 = (1, 2, 3)
    print(f"\ntuple1 is tuple2: {tuple1 is tuple2}")  # True, tuples are immutable and may share memory
    print(f"tuple1 == tuple2: {tuple1 == tuple2}")    # True, values are equal
    
    # List comparison
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(f"\nlist1 is list2: {list1 is list2}")  # False, different objects in memory
    print(f"list1 == list2: {list1 == list2}")    # True, values are equal



def main():
    print("Object Comparison Using 'is' and '==':\n")
    compare_objects()

if __name__ == "__main__":
    main()
