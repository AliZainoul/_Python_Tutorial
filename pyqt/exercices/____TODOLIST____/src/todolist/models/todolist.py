from typing import List
from todolist.models.task import Task

class TodoList:
    def __init__(self):
        self._tasks : List[Task]  = list() 

    @property
    def tasks(self) -> List[Task]:
        return self._tasks
    
    @tasks.setter
    def tasks(self, list_of_tasks : List[Task]):
        self._tasks = list_of_tasks
    
    def add_task(self, task: Task) -> None:
        self._tasks.append(task)

    def mark_task_as_done(self, index: int) -> None:
        self._tasks[index].is_done = True

    def __str__(self) -> str:
        result : str = ""
        for task in self.tasks:
            result += str(task)

        return result
            