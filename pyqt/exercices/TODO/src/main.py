import sys

from todolist.managers.managers import TodoListManager
from todolist.controllers.controllers import TodoListController
from todolist.views.views import TodoListViewCLI, TodoListViewPyQt
from todolist.persistence.persistence import CsvPersistence

from PyQt6.QtWidgets import QApplication


def main(view_type: str):
    FILE_NAME = "data/tasks.csv"

    # Set up persistence (CsvPersistence in this case)
    persistence = CsvPersistence(FILE_NAME)

    # Create the TodoListManager, responsible for the model and persistence
    todo_list_manager = TodoListManager(persistence)

    # Initialize the appropriate view and controller based on the view_type
    match view_type:
        case "cli":
        # CLI view setup
            # Initialize without a controller
            view = TodoListViewCLI(controller=None) 
            # Pass manager and view
            controller = TodoListController(todo_list_manager, view)  
            # Set the controller in the view
            view.controller = controller
            # Show the GUI
            view.show()

        case "pyqt":
        # PyQt view setup
            app = QApplication(sys.argv)
            # Initialize without a controller
            view  = TodoListViewPyQt(controller=None)  
            # Pass manager and view
            controller = TodoListController(todo_list_manager, view)  
            # Set the controller in the view
            view.controller = controller
            # Load initial tasks  
            controller.load()
            controller.refresh_view()
            # Show the GUI
            view.show()
            sys.exit(app.exec())

        case _:
            print("Invalid view type. Choose 'cli' or 'pyqt'.")

if __name__ == "__main__":
    """
    Entry point for running the TodoList application. 

    This block expects a single command-line argument to determine the type of view to initialize:
    either "cli" for a command-line interface or "pyqt" for a PyQt graphical user interface.

    Usage:
    ------
    python main.py [cli|pyqt]

    Parameters:
    -----------
    sys.argv[1] : str
        Command-line argument that specifies the type of view:
        - "cli" for the command-line interface
        - "pyqt" for the graphical interface using PyQt

    Raises:
    -------
    SystemExit
        Exits the program if an incorrect number of arguments is provided or if the specified
        view type is invalid.

    Notes:
    ------
    The `view_type` argument is passed to the `main` function to initialize and start the
    appropriate interface and controller setup.
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py [cli|pyqt]")
        sys.exit(1)

    view_type = sys.argv[1].lower()
    main(view_type)
