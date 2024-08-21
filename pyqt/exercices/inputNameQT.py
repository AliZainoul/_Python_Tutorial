import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

class NameInputWindow(QWidget):
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
        self.setWindowTitle("Name Input")

        # Create a label to instruct the user
        self.label = QLabel("Enter your name:")
        # Create a text input field for name entry
        self.name_input = QLineEdit()
        # Create a submit button
        self.submit_button = QPushButton("Submit")
        # Create a label to display the result (i.e., the entered name)
        self.result_label = QLabel("")

        # Set up the layout with a vertical box layout (QVBoxLayout)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.result_label)

        # Apply the layout to the window
        self.setLayout(layout)

        # Connect the button click event to the display_name method
        self.submit_button.clicked.connect(self.display_name)

    def display_name(self):
        """
        Event handler method that retrieves the user's name from the input field 
        and displays it on the screen.
        """
        # Get the text entered by the user in the QLineEdit
        name = self.name_input.text()

        # Check if a name was entered
        if name:
            # If a name was entered, display a greeting message
            self.result_label.setText(f"Hello, {name}!")
        else:
            # If no name was entered, prompt the user to enter a name
            self.result_label.setText("Please enter your name.")

def main():
    """
    The main function that creates and runs the PyQt6 application.
    """
    # Create the QApplication object, essential for any PyQt application
    app = QApplication(sys.argv)

    # Create an instance of the NameInputWindow
    window = NameInputWindow()

    # Show the window on the screen
    window.show()

    # Start the application's event loop and ensure clean exit
    sys.exit(app.exec())

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()
