def get_number(prompt: str) -> float:
    """Prompt the user to enter a number and return it as a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def perform_operation(num1: float, num2: float, operator: str) -> float:
    """Perform the basic math operation based on the operator."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return num1 / num2
    else:
        print("Invalid operator. Please use one of: +, -, *, /")
        return None

def calculator():
    """Main calculator function."""
    print("Simple Calculator")
    
    num1 = get_number("Enter the first number: ")
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = get_number("Enter the second number: ")

    result = perform_operation(num1, num2, operator)
    if result is not None:
        print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()