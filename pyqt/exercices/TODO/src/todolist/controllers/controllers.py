# controllers.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class TodoListController(Observer):
    def __init__(self, todo_list_manager, view):
        self.todo_list_manager = todo_list_manager
        self.view = view
        self.todo_list_manager.attach(self)  # Attach the controller to the manager

    def add_task(self, description):
        self.todo_list_manager.add_task(description)

    def update_task(self, index, description):
        self.todo_list_manager.update_task(index, description)
    
    def delete_task(self, index):
        self.todo_list_manager.delete_task(index)
    
    def mark_task_as_done(self, index):
        self.todo_list_manager.mark_task_as_done(index)

    def save(self):
        self.todo_list_manager.save()

    def load(self):
        self.todo_list_manager.load()

    def refresh_view(self):
        tasks = self.todo_list_manager.get_tasks()
        self.view.display_todo_list(tasks)

    def update(self):
        # This method is called when TodoList notifies changes (Observer pattern)
        self.refresh_view()