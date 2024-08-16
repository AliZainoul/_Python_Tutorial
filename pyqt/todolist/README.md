# TodoList Project

## Project Description

This project is a simple Todo List application built using Python. It is structured into different modules for better organization and maintainability. The application includes core functionalities for managing tasks, a graphical user interface (GUI) for interacting with the tasks, and a set of unit tests to ensure the reliability of the code.

## Project Structure

The project is organized into various directories:

- **src/todolist/**: Contains the core logic of the Todo List application.
- **src/ui/**: Handles the graphical user interface for the application.
- **src/tests/**: Contains unit tests for testing the functionality of the application.
- **src/main.py**: The entry point for the application, which initializes and runs the UI.

## Import Guidelines

### Tests Directory

- **`__init__.py`**: Should be present but empty.
- **`test_todolist.py`**: Import the `TodoList` class as follows:

```python
  from todolist.todolist import TodoList
```

### TodoList Directory (Under src)
- **`__init__.py`**: Should be present but empty.
- **`todolist.py`**: No imports required

### UI Directory
- **`__init__.py`**: Import the TodoList class as follows:
```python
  from todolist.todolist import TodoList
```
- **`todolist_ui.py`**: Import the TodoList class as follows:

```python
  from todolist.todolist import TodoList
```

### Main file (main.py)
- **`main.py`**: Import the Todo and TodoListWindow classes as follows:

```python
from ui.todolist_ui import Todo, TodoListWindow
```

## In order to clean your project: 

```
rm -rf src/*/__pycache__
```