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
    A simple PyQt5 application window that asks the user to enter their name 
    and displays it on the screen after submission.
    """
    def __init__(self):
        """
        Constructor to initialize the window and set up the UI components.
        """
        super().__init__()

        # Initialize the UI components
        self.init_ui()

    def init_ui(self):
        """
        Set up the user interface components and layout for the window.
        """
        # Set the window title
        self.setWindowTitle("Entries Input")

        # Create a label to instruct the user
        self.label = QLabel("Enter your two numbers:")
        # Create a text input field for nums entry
        self.number1_input = QLineEdit()
        self.number2_input = QLineEdit()

        # Create a submit button
        self.submit_button = QPushButton("Submit")
        # Create a label to display the result (i.e., the entered numbers)
        self.result_label_ADD = QLabel("")
        self.result_label_SUB = QLabel("")
        self.result_label_MUL = QLabel("")
        self.result_label_DIV = QLabel("")
        self.result_label_EDIV = QLabel("")
        self.result_label_POW = QLabel("")
        self.result_label = QLabel("")



        # Set up the layout with a vertical box layout (QVBoxLayout)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.number1_input)
        layout.addWidget(self.number2_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.result_label_ADD)
        layout.addWidget(self.result_label_SUB)
        layout.addWidget(self.result_label_MUL)
        layout.addWidget(self.result_label_DIV)
        layout.addWidget(self.result_label_EDIV)
        layout.addWidget(self.result_label_POW)
        layout.addWidget(self.result_label)



        # Apply the layout to the window
        self.setLayout(layout)

        # Connect the button click event to the display_calculation method
        self.submit_button.clicked.connect(self.display_calculation)

    def display_calculation(self):
        """
        Event handler method that retrieves the user's name from the input field 
        and displays it on the screen.
        """
        # Get the text entered by the user in the QLineEdit
        if self.number1_input.text() != '':
            num1 = float(self.number1_input.text())
        if self.number2_input.text() != '':
            num2 = float(self.number2_input.text())
        if not isinstance(num1, float) and not isinstance(num2, float):
            # If no name was entered, prompt the user to enter a name
            self.result_label.setText("Please enter your nums.")
        # Check if a name was entered
        self.result_label_ADD.setText(f"Addition : {num1} + {num2} = {num1 + num2}")
        self.result_label_SUB.setText(f"Substraction: {num1} - {num2} = {num1 - num2}")
        self.result_label_MUL.setText(f"Product: {num1} * {num2} = {num1 * num2}")
        self.result_label_DIV.setText(f"Division: {num1} / {num2} = {num1 / num2}")
        self.result_label_EDIV.setText(f"Entire Division: {num1} // {num2} = {num1 // num2}")
        self.result_label_POW.setText(f"Power: {num1} ^ {num2} = {num1 ** num2}")
        
        

def main():
    """
    The main function that creates and runs the PyQt6 application.
    """
    # Create the QApplication object, essential for any PyQt application
    app = QApplication(sys.argv)

    # Create an instance of the CalcInputWindow
    window = CalcInputWindow()

    # Show the window on the screen
    window.show()

    # Start the application's event loop and ensure clean exit
    sys.exit(app.exec())

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()
