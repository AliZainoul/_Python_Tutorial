def get_number(prompt: str):
    """Prompt the user to enter a number and return it as int, float, or complex."""
    while True:
        user_input = input(prompt)
        try:
            # Try to parse as an integer
            number = int(user_input)
            return number
        except ValueError:
            try:
                # Try to parse as a float
                number = float(user_input)
                return number
            except ValueError:
                try:
                    # Try to parse as a complex number
                    number = complex(user_input)
                    return number
                except ValueError:
                    print("Invalid input. Please enter an integer, float, or complex number.")

def add_numbers(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2

def subtract_numbers(num1, num2):
    """Return the difference of two numbers."""
    return num1 - num2

def multiply_numbers(num1, num2):
    """Return the product of two numbers."""
    return num1 * num2

def divide_numbers(num1, num2):
    """Return the division of two numbers."""
    if num2 == 0:
        return "Division by zero is undefined"
    return num1 / num2

def exponentiate_numbers(base, exponent):
    """Return the exponentiation of base to the power of exponent."""
    return base ** exponent

def floor_division(num1, num2):
    """Return the floor division of two numbers, if applicable."""
    if isinstance(num1, complex) or isinstance(num2, complex):
        return "Floor division is not supported for complex numbers"
    if num2 == 0:
        return "Floor division by zero is undefined"
    return num1 // num2

def modulo_numbers(num1, num2):
    """Return the modulo of two numbers, if applicable."""
    if isinstance(num1, complex) or isinstance(num2, complex):
        return "Modulo is not supported for complex numbers"
    if num2 == 0:
        return "Modulo by zero is undefined"
    return num1 % num2

def display_results(num1, num2):
    """Display the results of various operations on the two numbers."""
    print(f"Addition: {add_numbers(num1, num2)}")
    print(f"Subtraction: {subtract_numbers(num1, num2)}")
    print(f"Multiplication: {multiply_numbers(num1, num2)}")
    print(f"Division: {divide_numbers(num1, num2)}")
    print(f"Exponentiation: {exponentiate_numbers(num1, num2)}")
    print(f"Floor Division: {floor_division(num1, num2)}")
    print(f"Modulo: {modulo_numbers(num1, num2)}")

def main():
    print("Mathematical Operations Program")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    
    display_results(num1, num2)

if __name__ == "__main__":
    main()