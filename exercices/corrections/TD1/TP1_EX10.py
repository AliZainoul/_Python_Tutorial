def get_number(prompt: str) -> int:
    """Prompt the user to enter a number in binary, octal, hexadecimal, or decimal and return it as an integer."""
    while True:
        user_input = input(prompt).lower().strip()
        try:
            # Handle binary without '0b' prefix
            if user_input.startswith("b"):
                return int(user_input[1:], 2)
            # Handle octal without '0o' prefix
            elif user_input.startswith("o"):
                return int(user_input[1:], 8)
            # Handle hexadecimal without '0x' prefix
            elif user_input.startswith("x"):
                return int(user_input[1:], 16)
            # Handle numbers with explicit '0b', '0o', '0x' prefixes
            elif user_input.startswith(("0b", "0o", "0x")):
                return int(user_input, 0)
            # Handle decimal input
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid binary (b...), octal (o...), hexadecimal (x...), or decimal number.")

def to_exponential(num: int) -> str:
    """Return the exponential notation of the number."""
    return f"{num:e}"

def to_binary(num: int) -> str:
    """Return the binary representation of the number."""
    return bin(num)

def to_octal(num: int) -> str:
    """Return the octal representation of the number."""
    return oct(num)

def to_hexadecimal(num: int) -> str:
    """Return the hexadecimal representation of the number."""
    return hex(num)

def display_conversions(num: int):
    """Display the number in different notations."""
    print(f"Exponential notation: {to_exponential(num)}")
    print(f"Binary notation: {to_binary(num)}")
    print(f"Octal notation: {to_octal(num)}")
    print(f"Hexadecimal notation: {to_hexadecimal(num)}")

def main():
    print("Numeric Notation Conversion Program")
    num = get_number("Enter a number (binary, octal, hexadecimal, or decimal): ")

    display_conversions(num)

if __name__ == "__main__":
    main()
