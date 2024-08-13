# src/calculate/calculator.py

class Calculator:
    """Class to perform basic arithmetic operations using function pointers."""

    def __init__(self):
        self.operations = {
            "add": self.add,
            "subtract": self.subtract,
            "multiply": self.multiply,
            "divide": self.divide,
            "power": self.power
        }

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def perform_operation(self, operation_name, a, b):
        """Perform the operation specified by operation_name."""
        if operation_name not in self.operations:
            raise ValueError(f"Operation {operation_name} not supported")
        return self.operations[operation_name](a, b)
