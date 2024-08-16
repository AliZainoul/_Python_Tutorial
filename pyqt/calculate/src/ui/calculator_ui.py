# src/ui/calculator_ui.py

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)
# from calculate import Calculator
# calculate is the folder containing calculator.py
from calculate.calculator import Calculator


class CalculatorUI(QWidget):
    """
    PyQt UI class that connects with the Calculator class 
    to perform operations based on user input.
    """

    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components."""
        self.setWindowTitle("Calculator")

        # Input fields and buttons
        self.number1_input = QLineEdit()
        self.number2_input = QLineEdit()
        self.result_label = QLabel("Result: ")

        self.operation_buttons = {
            "Add": "add",
            "Subtract": "subtract",
            "Multiply": "multiply",
            "Divide": "divide",
            "Power": "power"
        }

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.number1_input)
        layout.addWidget(self.number2_input)

        # Dynamically create buttons for each operation
        for button_text, operation_name in self.operation_buttons.items():
            button = QPushButton(button_text)
            button.clicked.connect(lambda checked, op=operation_name: self.handle_operation(op))
            layout.addWidget(button)

        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def handle_operation(self, operation_name):
        """Handle the selected operation."""
        try:
            num1, num2 = self.get_inputs()
            result = self.calculator.perform_operation(operation_name, num1, num2)
            self.result_label.setText(f"Result: {result}")
            #self.clear_error_message()  # Clear any previous error messages

        except ValueError as e:
            self.show_error_message(str(e))

    def get_inputs(self):
        """Get and validate inputs from the user."""
        try:
            num1 = float(self.number1_input.text())
            num2 = float(self.number2_input.text())
            return num1, num2
        except ValueError:
            raise ValueError("Please enter valid numbers")

    def show_error_message(self, message):
        """Display an error message in a dialog box."""
        QMessageBox.critical(self, "Error", message)

    def clear_error_message(self):
        """Clear any previous error messages."""
        self.result_label.setText("")
