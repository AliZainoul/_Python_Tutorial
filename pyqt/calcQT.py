import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

class CalcInputWindow(QWidget):
    """
    A PyQt6 application window that allows the user to enter two numbers
    and displays the results of various arithmetic operations.
    """
    def __init__(self):
        """
        Constructor to initialize the window and set up the UI components.
        """
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Set up the user interface components and layout for the window.
        """
        self.setWindowTitle("Calculator Input")

        # Initialize UI components
        self.label = QLabel("Enter your two numbers:")
        self.number1_input = QLineEdit()
        self.number2_input = QLineEdit()

        self.submit_button = QPushButton("Submit")
        
        # Initialize result labels
        self.result_labels = {
            'ADD': QLabel(""),
            'SUB': QLabel(""),
            'MUL': QLabel(""),
            'DIV': QLabel(""),
            'EDIV': QLabel(""),
            'POW': QLabel(""),
            'ERROR': QLabel("")
        }

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.number1_input)
        layout.addWidget(self.number2_input)
        layout.addWidget(self.submit_button)
        for label in self.result_labels.values():
            layout.addWidget(label)

        self.setLayout(layout)

        # Connect the button click event to the display_calculation method
        self.submit_button.clicked.connect(self.display_calculation)

    def display_calculation(self):
        """
        Event handler that retrieves the user's inputs from the input fields,
        performs various arithmetic calculations, and displays the results.
        """
        # Clear previous error messages
        self.result_labels['ERROR'].clear()

        try:
            num1, num2 = self._get_validated_inputs()
            self._display_results(num1, num2)
        except ValueError as e:
            self.result_labels['ERROR'].setText(str(e))
            self._clear_result_labels()

    def _get_validated_inputs(self):
        """
        Validates the inputs from the user. Ensures that both inputs are present
        and can be converted to floats. Raises a ValueError if the inputs are invalid.

        Returns:
            tuple: A tuple containing two floats representing the user's input.
        
        Raises:
            ValueError: If the input fields are empty or contain non-numeric values.
        """
        number1_text = self.number1_input.text()
        number2_text = self.number2_input.text()

        if not number1_text or not number2_text:
            raise ValueError("Please enter both numbers.")
        
        try:
            num1 = float(number1_text)
            num2 = float(number2_text)
        except ValueError:
            raise ValueError("Please enter valid numbers.")
        
        return num1, num2

    def _display_results(self, num1, num2):
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
                self.result_labels[key].setText(f"{operation}: N/A (division by zero)")
            else:
                self.result_labels[key].setText(f"{operation}: {num1} and {num2} = {result}")

    def _clear_result_labels(self):
        """
        Clears the text of all result labels except the error label.
        """
        for key in self.result_labels:
            if key != 'ERROR':
                self.result_labels[key].setText("")

def main():
    """
    The main function that creates and runs the PyQt6 application.
    """
    app = QApplication(sys.argv)
    window = CalcInputWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
