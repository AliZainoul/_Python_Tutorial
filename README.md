# Python Tutorial Repository

Welcome to the `_Python_Tutorial` repository! This repository is organized to help you explore Python in various domains, from numerical computing to GUI programming and code quality practices.

## Directory Overview

- **Numpy**:  
  Examples, exercises, and explanations for working with NumPy arrays, matrices, and numerical operations.

- **documents**:  
  Notes, tutorials, and references in PDF, Markdown, or other formats to support your Python learning journey.

- **exercices**:  
  Python exercises of varying difficulty, ideal for hands-on practice and reinforcing concepts.

- **pygame**:  
  Projects and exercises using the Pygame library for creating games and graphical simulations.

- **code_quality**:  
  Tools, tips, and examples for writing clean, maintainable Python code. Includes PEP8 guidelines, linting, and testing best practices.

- **examples**:  
  Standalone Python scripts demonstrating specific concepts, functions, or libraries in action.

- **explanations**:  
  Detailed explanations and guides for understanding Python syntax, data structures, OOP, and advanced topics.

- **pyqt**:  
  Projects, tutorials, and exercises using PyQt for building GUI applications in Python.

## Cleaning Up Python Cache

During development, Python generates `__pycache__` directories containing bytecode. You can safely remove all `__pycache__` directories using:

```bash
find . -name "__pycache__" -type d -exec rm -rf {} +
```

Note: Run this command from the root of the repository (_Python_Tutorial) to clean caches across all subdirectories.

## Usage Tips

Navigate into each folder to explore examples and exercises.

Use virtual environments to manage dependencies (venv or conda).

Regularly clean up __pycache__ if you want to reduce clutter or force re-compilation of scripts.

## License & Credits

This repository is created for educational purposes to learn and practice Python across multiple domains. Adapt, reuse, and share responsibly.
