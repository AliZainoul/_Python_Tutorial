from todolist.models.task import Task
from todolist.models.todolist import  TodoList
from todolist.persistence.persistence import Persistence

class TodoListManager:
    def __init__(self, persistence: Persistence):
        self.todo_list : TodoList = TodoList()
        self.persistence : Persistence = persistence
        # self.observers = []  # List to hold observers like the controller

    '''
    # def attach(self, observer):
    #     """Attach an observer to the manager."""
    #     self.observers.append(observer)

    # def detach(self, observer):
    #     """Detach an observer."""
    #     self.observers.remove(observer)

    # def notify(self):
    #     """Notify all observers of changes."""
    #     for observer in self.observers:
    #         observer.update()
    '''

    def add_task(self, description):
        """Add a task and notify observers."""
        self.todo_list.tasks = self.persistence.load().tasks
        task = Task(name=description)
        self.todo_list.add_task(task)
        self.save()
        # self.notify()  # Notify observers about the change

    def get_tasks(self):
        """Return the list of tasks."""
        return self.todo_list.tasks

    def update_task(self, index, new_description):
        """Update a task and notify observers."""
        if 0 <= index < len(self.todo_list.tasks):
            self.todo_list.tasks[index].name = new_description
            self.save()
            # self.notify()  # Notify observers about the change
        else:
            raise IndexError("Index Out range.")

    def delete_task(self, index):
        """Delete a task and notify observers."""
        if 0 <= index < len(self.todo_list.tasks):
            del self.todo_list.tasks[index]
            self.save()
            # self.notify()  # Notify observers about the change
        else:
            raise IndexError("Index Out range.")

    def mark_task_as_done(self, index):
        """Mark a task as done and notify observers."""
        if 0 <= index < len(self.todo_list.tasks):
            self.todo_list.mark_task_as_done(index)
            self.save()
            # self.notify()  # Notify observers about the change
        else:
            raise IndexError("Index Out range.")

    def load(self):
        """Load the todo list from persistence."""
        self.todo_list.tasks = self.persistence.load().tasks
        # self.notify()  # Notify observers about the change

    def save(self):
        """Save the current state of the todo list."""
        self.persistence.save(self.todo_list)