def get_integer(prompt: str) -> int:
    """Prompt the user to enter an integer and return it."""
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def bitwise_and(num1: int, num2: int) -> int:
    """Return the result of bitwise AND between two integers."""
    return num1 & num2

def bitwise_or(num1: int, num2: int) -> int:
    """Return the result of bitwise OR between two integers."""
    return num1 | num2

def bitwise_xor(num1: int, num2: int) -> int:
    """Return the result of bitwise XOR between two integers."""
    return num1 ^ num2

def bitwise_right_shift(num1: int, shift: int) -> int:
    """Return the result of right shifting num1 by 'shift' positions."""
    return num1 >> shift

def bitwise_left_shift(num1: int, shift: int) -> int:
    """Return the result of left shifting num1 by 'shift' positions."""
    return num1 << shift

def display_bitwise_results(num1: int, num2: int):
    """Display the results of bitwise operations on the two numbers."""
    print(f"{num1} & {num2} (AND) = {bitwise_and(num1, num2)}")
    print(f"{num1} | {num2} (OR) = {bitwise_or(num1, num2)}")
    print(f"{num1} ^ {num2} (XOR) = {bitwise_xor(num1, num2)}")
    print(f"{num1} >> 2 (Right shift by 2) = {bitwise_right_shift(num1, 2)}")
    print(f"{num1} << 2 (Left shift by 2) = {bitwise_left_shift(num1, 2)}")

def main():
    print("Bitwise Operations Program")
    num1 = get_integer("Enter the first integer: ")
    num2 = get_integer("Enter the second integer: ")

    display_bitwise_results(num1, num2)

if __name__ == "__main__":
    main()
