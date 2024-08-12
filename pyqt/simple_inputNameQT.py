import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

def main():
    def display_name():
        """
        Event handler method that retrieves the user's name from the input field 
        and displays it on the screen.
        """
        # Get the text entered by the user in the QLineEdit
        name = name_input.text()

        # Check if a name was entered
        if name:
            # If a name was entered, display a greeting message
            result_label.setText(f"Hello, {name}!")
        else:
            # If no name was entered, prompt the user to enter a name
            result_label.setText("Please enter your name.")

    """
    The main function that creates and runs the PyQt6 application.
    """
    # Create the QApplication object, essential for any PyQt application
    app = QApplication(sys.argv)

    # Create an instance of the NameInputWindow
    window = QWidget()
    """
    Set up the user interface components and layout for the window.
    """
    # Set the window title
    window.setWindowTitle("Name Input")

    # Create a label to instruct the user
    label = QLabel("Enter your name:")
    # Create a text input field for name entry
    name_input = QLineEdit()
    # Create a submit button
    submit_button = QPushButton("Submit")
    # Create a label to display the result (i.e., the entered name)
    result_label = QLabel("")

    # Set up the layout with a vertical box layout (QVBoxLayout)
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(name_input)
    layout.addWidget(submit_button)
    layout.addWidget(result_label)

    # Apply the layout to the window
    window.setLayout(layout)

    # Connect the button click event to the display_name method
    submit_button.clicked.connect(display_name)

    # Show the window on the screen
    window.show()

    # Start the application's event loop and ensure clean exit
    sys.exit(app.exec())

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    main()