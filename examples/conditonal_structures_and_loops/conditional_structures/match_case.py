"""
This script demonstrates the use of the `match-case` statement in Python.
The `match-case` statement is a powerful control structure introduced in Python 3.10
for pattern matching. This script includes examples of how to use `match-case`
effectively.
"""

def main():
    """
    Main function to demonstrate match-case examples.
    """
    # Example 1: Simple match-case
    value = 2
    match value:
        case 1:
            print("Value is 1")
        case 2:
            print("Value is 2")
        case 3:
            print("Value is 3")
        case _:
            print("Value is something else")

    # Example 2: Matching with a tuple
    point = (0, 1)
    match point:
        case (0, 0):
            print("Point is at the origin")
        case (0, y):
            print(f"Point is on the Y-axis at y={y}")
        case (x, 0):
            print(f"Point is on the X-axis at x={x}")
        case (x, y):
            print(f"Point is at x={x}, y={y}")
        case _:
            print("Unknown point")

    # Example 3: Matching with a dictionary
    person = {"name": "Alice", "age": 30}
    match person:
        case {"name": name, "age": age} if age > 18:
            print(f"{name} is an adult, age {age}")
        case {"name": name, "age": age}:
            print(f"{name} is a minor, age {age}")
        case _:
            print("Unknown person")

if __name__ == "__main__":
    main()
