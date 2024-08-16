# Calculator Project

## Project Description

This project is a simple Calculator application built using Python. It is structured into different modules for better organization and maintainability. The application includes core functionalities for performing basic operations, a graphical user interface (GUI) for interacting with different operations, and a set of unit tests to ensure the reliability of the code.

## Project Structure

The project is organized into various directories:

- **src/calculate/**: Contains the core logic of the Calculator application.
- **src/ui/**: Handles the graphical user interface for the application.
- **src/tests/**: Contains unit tests for testing the functionality of the application.
- **src/main.py**: The entry point for the application, which initializes and runs the UI.

## Import Guidelines

### Tests Directory

- **`__init__.py`**: Should be present but empty.
- **`test_calculator.py`**: Import the `Calculator` class as follows:

```python
  from calculate.calculator import Calculator
```

### TodoList Directory (Under src)
- **`__init__.py`**: Should be present but empty.
- **`calculator.py`**: No imports required

### UI Directory
- **`__init__.py`**: Should be present but empty.
- **`calculator_ui.py`**: Import the Calculator class as follows:

```python
  from calculate.calculator import Calculator
```

### Main file (main.py)
- **`main.py`**: Import the CalculatorUI class as follows:

```python
from ui.calculator_ui import CalculatorUI
```

## In order to clean your project: 

```
rm -rf src/*/__pycache__
```