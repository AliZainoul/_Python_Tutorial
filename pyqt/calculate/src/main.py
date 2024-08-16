# src/main.py

import sys
from PyQt6.QtWidgets import QApplication
from ui.calculator_ui import CalculatorUI

def main():
    """Main function to run the PyQt application."""
    app = QApplication(sys.argv)
    window = CalculatorUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()