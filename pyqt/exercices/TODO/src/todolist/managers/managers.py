# managers.py
from todolist.models.models import Task, TodoList

class TodoListManager:
    def __init__(self, persistence):
        self.todo_list : TodoList = TodoList()
        self.persistence = persistence
        self.observers = []  # List to hold observers like the controller

    def attach(self, observer):
        """Attach an observer to the manager."""
        self.observers.append(observer)

    def detach(self, observer):
        """Detach an observer."""
        self.observers.remove(observer)

    def notify(self):
        """Notify all observers of changes."""
        for observer in self.observers:
            observer.update()

    def add_task(self, description):
        """Add a task and notify observers."""
        self.todo_list.set_tasks(self.persistence.load().get_tasks())
        task = Task(name=description)
        self.todo_list.add_task(task)
        self.save()
        self.notify()  # Notify observers about the change

    def get_tasks(self):
        """Return the list of tasks."""
        return self.todo_list.get_tasks()

    def update_task(self, index, new_description):
        """Update a task and notify observers."""
        if 0 <= index < len(self.get_tasks()):
            self.get_tasks()[index].name = new_description
            self.save()
            self.notify()  # Notify observers about the change
        else:
            raise IndexError("Index out range.")

    def delete_task(self, index):
        """Delete a task and notify observers."""
        if 0 <= index < len(self.get_tasks()):
            del self.todo_list.get_tasks()[index]
            self.save()
            self.notify()  # Notify observers about the change
        else:
            raise IndexError("Index out range.")

    def mark_task_as_done(self, index):
        """Mark a task as done and notify observers."""
        if 0 <= index < len(self.get_tasks()):
            self.todo_list.mark_task_as_done(index)
            self.save()
            self.notify()  # Notify observers about the change
        else:
            raise IndexError("Index out range.")
        
    def load(self):
        """Load the todo list from persistence."""
        self.todo_list.set_tasks(self.persistence.load().get_tasks())
        self.notify()  # Notify observers about the change

    def save(self):
        """Save the current state of the todo list."""
        self.persistence.save(self.todo_list)