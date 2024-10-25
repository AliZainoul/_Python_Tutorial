import os
import csv

from todolist.models.task import Task
from todolist.models.todolist import  TodoList
from todolist.persistence.persistence import Persistence

class CsvPersistence(Persistence):
    def __init__(self, filename: str):
        self.filename = filename

    def save(self, todo_list: TodoList) -> None:
            """
            Saves the list of tasks to a CSV file. If the file does not exist, it will be created.

            Parameters:
            -----------
            todo_list : TodoList
                The TodoList instance containing tasks to be saved.
            """
            # Ensure the file exists or create it
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)

            # Open the file in write mode
            with open(self.filename, 'w', newline='\n') as file:
                writer = csv.writer(file)
                for task in todo_list.tasks:
                    writer.writerow([task.name, task.is_done])

    def load(self) -> TodoList:
        todo_list = TodoList()
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    task_name, is_done = row
                    task = Task(task_name)
                    if is_done == 'True':
                        task.is_done = True
                    todo_list.add_task(task)
        except FileNotFoundError:
            pass  # If no file exists, start with an empty list
        return todo_list