# from todolist import TodoList
# todolist is the folder containing todolist.py


# OR:
from todolist.todolist import TodoList
# with __init__ file in todolist with:
# from .todolist import TodoList



def test_add():
    todo_list = TodoList()
    todo_list.add("Buy milk")
    assert todo_list.find_todo_by_title("Buy milk").text == "Buy milk"


def test_remove():
    todo_list = TodoList()
    todo_list.add("Buy milk")
    todo_list.remove("Buy milk")
    assert todo_list.todos == []


def test_remove_raises_error():
    todo_list = TodoList()
    todo_list.add("Buy milk")
    try:
        todo_list.remove("Buy bread")
    except ValueError as e:
        assert str(e) == "Todo with title Buy bread not found"
    else:
        assert False, "Expected ValueError"


def test_find_todo_by_title():
    todo_list = TodoList()
    todo_list.add("Buy milk")
    todo = todo_list.find_todo_by_title("Buy milk")
    assert todo.text == "Buy milk"


def test_checked():
    todo_list = TodoList()
    todo_list.add("Buy milk")
    todo = todo_list.set_checked("Buy milk")
    assert todo.checked
    todo.checked = False
    assert not todo.checked
