from typing import List
from todolist.models.task import Task
from todolist.models.todolist import TodoList


def main():

    my_tasks        : List[Task]    = [Task() for _ in range (10)]
    todolist        : TodoList      = TodoList()

    todolist.tasks = my_tasks

    print(todolist)

if __name__ == "__main__":
    main()