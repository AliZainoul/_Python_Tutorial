import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Calculator Input")

label = QLabel("Enter your two numbers:")

number1_input = QLineEdit()
number2_input = QLineEdit()

submit_button = QPushButton("Submit")

result_labels = {
    'ADD': QLabel(""),
    'SUB': QLabel(""),
    'MUL': QLabel(""),
    'DIV': QLabel(""),
    'EDIV': QLabel(""),
    'POW': QLabel(""),
    'ERROR': QLabel("")
}

layout = QVBoxLayout()

layout.addWidget(label)
layout.addWidget(number1_input)
layout.addWidget(number2_input)
layout.addWidget(submit_button)

for label in result_labels.values():
    layout.addWidget(label)

window.setLayout(layout)

def _get_validated_inputs():
    """
    Validates the inputs from the user. Ensures that both inputs are present
    and can be converted to floats. Raises a ValueError if the inputs are invalid.

    Returns:
        tuple: A tuple containing two floats representing the user's input.
    
    Raises:
        ValueError: If the input fields are empty or contain non-numeric values.
    """
    number1_text = number1_input.text()
    number2_text = number2_input.text()

    if not number1_text or not number2_text:
        raise ValueError("Please enter both numbers.")
    
    try:
        num1 = float(number1_text)
        num2 = float(number2_text)
    except TypeError:
        raise TypeError("Please enter valid numbers.")
    
    return num1, num2
def _display_results(num1, num2):
    global result_labels
    """
    Displays the results of various arithmetic calculations on the screen.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
    """
    operations = {
        'ADD': (num1 + num2, "Addition"),
        'SUB': (num1 - num2, "Subtraction"),
        'MUL': (num1 * num2, "Product"),
        'DIV': (num1 / num2 if num2 != 0 else None, "Division"),
        'EDIV': (num1 // num2 if num2 != 0 else None, "Entire Division"),
        'POW': (num1 ** num2, "Power")
    }

    for key, (result, operation) in operations.items():
        if result is None:
            result_labels[key].setText(f"{operation}: N/A (division by zero)")
        else:
            result_labels[key].setText(f"{operation}: {num1} and {num2} = {result}")

def _clear_result_labels():
    global result_labels
    """
    Clears the text of all result labels except the error label.
    """
    for key in result_labels:
        if key != 'ERROR':
            result_labels[key].setText("")
def display_calculation():
    global result_labels
    """
    Event handler that retrieves the user's inputs from the input fields,
    performs various arithmetic calculations, and displays the results.
    """
    # Clear previous error messages
    result_labels['ERROR'].clear()

    try:
        num1, num2 = _get_validated_inputs()
        _display_results(num1, num2)
    except ValueError as e:
        result_labels['ERROR'].setText(str(e))
        _clear_result_labels()


submit_button.clicked.connect(display_calculation)

window.show()

sys.exit(app.exec())