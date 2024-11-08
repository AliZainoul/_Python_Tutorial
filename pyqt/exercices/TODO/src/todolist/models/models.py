# models.py

class Task:
    def __init__(self, name: str):
        self._name = name
        self._is_done = False

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name) -> None:
        self._name = new_name

    @property
    def is_done(self) -> bool:
        return self._is_done

    def mark_as_done(self):
        self._is_done = True

    def __del__(self):
        del self


class TodoList:
    def __init__(self):
        self._tasks = []

    def add_task(self, task: Task):
        self._tasks.append(task)

    def mark_task_as_done(self, index: int):
        if 0 <= index < len(self._tasks):
            self._tasks[index].mark_as_done()
        else:
            raise IndexError("Index out range.")

    def get_tasks(self):
        return self._tasks
    
    def set_tasks(self, tasks):
        self._tasks = tasks 