"""
This script demonstrates the usage of the range() object in Python with several examples.
"""

def main():
    # Example 1: Simple range from 0 to 4
    print("Example 1: range(5)")
    for i in range(5):
        print(i, end=" ")
    print("\n")

    # Example 2: Range with a start and stop
    print("Example 2: range(2, 8)")
    for i in range(2, 8):
        print(i, end=" ")
    print("\n")

    # Example 3: Range with a step
    print("Example 3: range(1, 10, 2)")
    for i in range(1, 10, 2):
        print(i, end=" ")
    print("\n")

    # Example 4: Range with a negative step
    print("Example 4: range(10, 0, -2)")
    for i in range(10, 0, -2):
        print(i, end=" ")
    print("\n")

    # Example 5: Using range to create a list
    print("Example 5: list(range(5))")
    print(list(range(5)))
    print("\n")

    # Example 6: Using range in reverse
    print("Example 6: range(5, 0, -1)")
    for i in range(5, 0, -1):
        print(i, end=" ")
    print("\n")

    # Example 7: Using range with len() in a for loop
    print("Example 7: Using range with len()")
    sample_list = ['a', 'b', 'c', 'd']
    for i in range(len(sample_list)):
        print(f"Index {i}: {sample_list[i]}")

if __name__ == "__main__":
    main()
