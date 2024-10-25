from abc import ABC, abstractmethod
from todolist.models.todolist import TodoList

class Persistence(ABC):
    @abstractmethod
    def save(self, todo_list: TodoList) -> None:
        pass

    @abstractmethod
    def load(self) -> TodoList:
        pass