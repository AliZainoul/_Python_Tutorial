# Example of using a for loop with different container types

def main() -> None:
    # String
    text = "Python"
    print("\nIterating through a string:")
    for char in text:
        print(char)

    # Tuple
    numbers = (1, 2, 3, 4)
    print("\nIterating through a tuple:")
    for number in numbers:
        print(number)
    
    # List
    fruits = ["apple", "banana", "cherry"]
    print("Iterating through a list:")
    for fruit in fruits:
        print(fruit)

    # Dictionary
    person = {"name": "Alice", "age": 30, "city": "New York"}
    print("\nIterating through a dictionary (keys and values):")
    for key, value in person.items():
        print(f"{key}: {value}")

    # Set
    unique_numbers = {10, 20, 30, 40}
    print("\nIterating through a set:")
    for num in unique_numbers:
        print(num)

if __name__ == "__main__":
    main()
