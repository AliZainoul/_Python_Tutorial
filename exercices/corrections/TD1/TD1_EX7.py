def is_valid_integer(value: str) -> bool:
    """Check if the input string can be converted to an integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False

def convert_to_binary(values: list) -> list:
    """Convert a list of values to their binary representations (if valid)."""
    binary_values = []
    for value in values:
        if is_valid_integer(value):
            binary_values.append(bin(int(value)))
        else:
            binary_values.append(f"'{value}' cannot be converted to binary")
    return binary_values

def main():
    user_input = input("Enter a series of values separated by commas: ")
    
    # Split the input by commas and remove any extra spaces
    values = [value.strip() for value in user_input.split(",")]

    binary_values = convert_to_binary(values)
    
    print("\nBinary conversions:")
    for original, binary in zip(values, binary_values):
        print(f"{original}: {binary}")

if __name__ == "__main__":
    main()