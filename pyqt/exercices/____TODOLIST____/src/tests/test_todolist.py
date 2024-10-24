import pytest
from todolist.models.task import Task
from todolist.models.todolist import TodoList

def test_todolist_initialization():
    todo_list = TodoList()
    assert todo_list.tasks == []

def test_add_task():
    todo_list = TodoList()
    task = Task(name="Buy groceries", is_done=False)
    todo_list.add_task(task)
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].name == "Buy groceries"
    assert todo_list.tasks[0].is_done == False

def test_mark_task_as_done():
    todo_list = TodoList()
    task = Task(name="Buy groceries", is_done=False)
    todo_list.add_task(task)
    todo_list.mark_task_as_done(0)
    assert todo_list.tasks[0].is_done is True

def test_mark_task_as_done_invalid_index():
    todo_list = TodoList()
    with pytest.raises(IndexError):
        todo_list.mark_task_as_done(0)  # No task exists yet

def test_todolist_str_representation():
    todo_list = TodoList()
    task1 = Task(name="Buy groceries", is_done=False)
    task2 = Task(name="Clean the house", is_done=True)
    todo_list.add_task(task1)
    todo_list.add_task(task2)
    result = str(todo_list)
    assert "Task name: Buy groceries and its status is False." in result
    assert "Task name: Clean the house and its status is True." in result


