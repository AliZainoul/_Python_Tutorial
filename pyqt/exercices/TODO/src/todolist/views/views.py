# views.py
from abc import ABC, abstractmethod

from PyQt6.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
    QLabel, 
    QPushButton, 
    QListWidget, 
    QLineEdit, 
    QMessageBox,
    QInputDialog
)
# from PyQt6.QtCore import Qt

class TodoListView():
    @abstractmethod
    def display_todo_list(self, tasks):
        pass

    @abstractmethod
    def mark_task_as_done(self, index):
        pass


class TodoListViewCLI(TodoListView):
    def __init__(self, controller):
        self.controller = controller

    def display_todo_list(self, tasks):
        for index, task in enumerate(tasks):
            status = "Done" if task.is_done else "Not Done"
            print(f"{index + 1}. {task.name} - {status}")

    def mark_task_as_done(self, index):
        print(f"Task {index + 1} marked as done.")

    def show(self):
        self.interaction_loop()

    def interaction_loop(self):
        """
        Main CLI interaction loop to interact with the user.
        """
        self.controller.load()

        while True:
            print("\nOptions:")
            print("1. Add a task")
            print("2. Update task")
            print("3. Mark a task as done")
            print("4. Delete task")
            print("5. Save tasks")
            print("6. Load tasks")
            print("7. Exit")

            option = input("Choose an option (1-7): ")

            match option:
                case "1":
                    task_description = input("Enter task description: ")
                    self.controller.add_task(task_description)
                case "2":
                    index = int(input("Enter task index to update: ")) - 1
                    task_description = input("Enter task description: ")
                    self.controller.update_task(index, task_description)
                case "3":
                    index = int(input("Enter task index to mark as done: ")) - 1
                    self.controller.mark_task_as_done(index)
                case "4":
                    index = int(input("Enter task index to delete: ")) - 1
                    self.controller.delete_task(index)
                case "5":
                    self.controller.save()
                case "6":
                    self.controller.load()
                case "7":
                    print("Exiting...")
                    break
                case _:
                    print("Invalid option. Please choose again.")



class TodoListViewPyQt(QWidget, TodoListView):
    """
    A class to represent the TodoList view using PyQt6.

    This class is responsible for displaying the tasks in the to-do list and 
    interacting with the user interface. It works as a view in the MVC pattern.

    Attributes:
    -----------
    controller : TodoListController
        The controller that manages the to-do list functionality.
    """

    def __init__(self, controller):
        """
        Initialize the TodoListView with a controller.

        Parameters:
        -----------
        controller : TodoListController
            The controller that manages the to-do list.
        """
        super().__init__()

        self.controller = controller

        # Set up the GUI
        self.setWindowTitle("To-Do List")
        self.layout = QVBoxLayout()

        self.label = QLabel("Tasks:")
        self.layout.addWidget(self.label)

        # List widget to display tasks
        self.todo_list_widget = QListWidget()
        self.layout.addWidget(self.todo_list_widget)

        # Input for adding new tasks
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter new task")
        self.layout.addWidget(self.task_input)

        # Using the helper function to add buttons
        self.create_button("Add Task", self.add_task)
        self.create_button("Update Task", self.update_task)
        self.create_button("Delete Task", self.delete_task)
        self.create_button("Mark Task as Done", self.mark_task_as_done)
        self.create_button("Save To-Do List", self.save)
        self.create_button("Load To-Do List", self.load)

        # Set the main layout
        self.setLayout(self.layout)

    def create_button(self, label, handler):
            """
            Helper function to create a QPushButton, connect it to a handler,
            and add it to the layout.

            Parameters:
            -----------
            label : str
                The label text for the button.
            handler : function
                The function to connect to the button's clicked signal.
            """
            button = QPushButton(label)
            button.clicked.connect(handler)
            self.layout.addWidget(button)
    def display_todo_list(self, tasks):
        """
        Display the list of tasks in the QListWidget.

        Parameters:
        -----------
        tasks : List[Task]
            The list of tasks to display.
        """
        self.todo_list_widget.clear()
        for task in tasks:
            item = f"{'[Done]' if task.is_done else '[Pending]'} {task.name}"
            self.todo_list_widget.addItem(item)

    def add_task(self):
        """
        Add a new task to the to-do list.
        """
        task_description = self.task_input.text().strip()
        if task_description:
            self.controller.add_task(task_description)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a valid task description.")

    def delete_task(self):
        """
        Delete the selected task from the to-do list.
        """
        selected_items = self.todo_list_widget.selectedItems()
        if selected_items:
            index = self.todo_list_widget.row(selected_items[0])
            self.controller.delete_task(index)
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a task to delete.")

    def update_task(self):
        """
        Update the selected task in the to-do list.
        """
        selected_items = self.todo_list_widget.selectedItems()
        if selected_items:
            index = self.todo_list_widget.row(selected_items[0])
            task_description, ok = QInputDialog.getText(self, "Update Task", "Enter new task description:")
            if ok and task_description:
                self.controller.update_task(index, task_description)
            elif not task_description:
                QMessageBox.warning(self, "Input Error", "Please enter a valid task description.")
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a task to update.")



    def mark_task_as_done(self):
        """
        Mark the selected task as done in the to-do list.
        """
        selected_items = self.todo_list_widget.selectedItems()
        if selected_items:
            index = self.todo_list_widget.row(selected_items[0])
            self.controller.mark_task_as_done(index)
            self.mark_task_as_done_at_index(index)
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a task to mark as done.")

    def mark_task_as_done_at_index(self, index):
        """
        Visually update the task as done in the list.

        Parameters:
        -----------
        index : int
            The index of the task to mark as done in the list.
        """
        item = self.todo_list_widget.item(index)
        if item:
            item.setText(item.text().replace("[Pending]", "[Done]"))

    def save(self):
        """
        Save the current to-do list to persistence.
        """
        self.controller.save()
        QMessageBox.information(self, "Save", "To-Do list saved successfully.")

    def load(self):
        """
        Load the to-do list from persistence.
        """
        self.controller.load()
        QMessageBox.information(self, "Load", "To-Do list loaded successfully.")
