from typing import List
from todolist.models.task import Task

class TodoList:
    """
    A class to represent a to-do list that manages multiple tasks.

    Attributes:
    -----------
    _tasks : List[Task]
        A list of tasks in the to-do list.

    Methods:
    --------
    tasks (property):
        Gets the list of tasks in the to-do list.
    tasks (setter):
        Sets the list of tasks in the to-do list.
    add_task(task: Task):
        Adds a task to the to-do list.
    mark_task_as_done(index: int):
        Marks a task as done based on its index in the list.
    __str__():
        Returns a string representation of the entire to-do list.
    """
    
    def __init__(self):
        """
        Initializes a TodoList object with an empty list of tasks.
        """
        self._tasks: List[Task] = list()

    @property
    def tasks(self) -> List[Task]:
        """
        Gets the list of tasks in the to-do list.

        Returns:
        --------
        List[Task]:
            A list of tasks in the to-do list.
        """
        return self._tasks

    @tasks.setter
    def tasks(self, list_of_tasks: List[Task]) -> None:
        """
        Sets the list of tasks in the to-do list.

        Parameters:
        -----------
        list_of_tasks : List[Task]
            The new list of tasks to set for the to-do list.
        """
        self._tasks = list_of_tasks

    def add_task(self, task: Task) -> None:
        """
        Adds a task to the to-do list.

        Parameters:
        -----------
        task : Task
            The task to add to the to-do list.
        """
        self._tasks.append(task)

    def mark_task_as_done(self, index: int) -> None:
        """
        Marks a task as done based on its index in the list.

        Parameters:
        -----------
        index : int
            The index of the task to mark as done.

        Raises:
        -------
        IndexError:
            If the index is out of range of the task list.
        """
        if 0 <= index < len(self._tasks):
            self._tasks[index].is_done = True
        else:
            raise IndexError("Index out of range")

    def __str__(self) -> str:
        """
        Returns a string representation of the entire to-do list.

        Returns:
        --------
        str:
            A string representation of all tasks in the to-do list.
        """
        result: str = ""
        for task in self.tasks:
            result += str(task)
        return result
