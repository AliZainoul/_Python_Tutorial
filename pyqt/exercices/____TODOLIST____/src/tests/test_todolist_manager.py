import pytest
from todolist.models.task import Task
from todolist.models.todolist import TodoList
from todolist.managers.todolist_manager import TodoListManager
from todolist.persistence.csv_persistence import CsvPersistence
import os

@pytest.fixture
def temporary_csv(tmp_path):
    """
    Fixture to create a temporary CSV file for persistence testing.
    """
    return tmp_path / "test_tasks.csv"

@pytest.fixture
def persistence(temporary_csv):
    """
    Fixture to create a CsvPersistence instance.
    """
    return CsvPersistence(str(temporary_csv))

@pytest.fixture
def todo_list_manager(persistence):
    """
    Fixture to create a TodoListManager instance with CsvPersistence.
    """
    return TodoListManager(persistence)

def test_add_task(todo_list_manager):
    todo_list_manager.add_task("Test Task 1")
    tasks = todo_list_manager.todo_list.tasks
    assert len(tasks) == 1
    assert tasks[0].name == "Test Task 1"
    assert not tasks[0].is_done

def test_update_task(todo_list_manager):
    todo_list_manager.add_task("Initial Task")
    todo_list_manager.update_task(0, "Updated Task")
    assert todo_list_manager.todo_list.tasks[0].name == "Updated Task"

def test_update_task_invalid_index(todo_list_manager):
    with pytest.raises(IndexError):
        todo_list_manager.update_task(0, "Invalid Task")

def test_delete_task(todo_list_manager):
    todo_list_manager.add_task("Task to Delete")
    todo_list_manager.delete_task(0)
    assert len(todo_list_manager.todo_list.tasks) == 0

def test_delete_task_invalid_index(todo_list_manager):
    with pytest.raises(IndexError):
        todo_list_manager.delete_task(0)

def test_mark_task_as_done(todo_list_manager):
    todo_list_manager.add_task("Incomplete Task")
    todo_list_manager.mark_task_as_done(0)
    assert todo_list_manager.todo_list.tasks[0].is_done

def test_mark_task_as_done_invalid_index(todo_list_manager):
    with pytest.raises(IndexError):
        todo_list_manager.mark_task_as_done(0)

def test_load_empty_csv(persistence, todo_list_manager):
    todo_list_manager.load()
    assert len(todo_list_manager.todo_list.tasks) == 0  # No tasks in CSV

def test_save_and_load(persistence, todo_list_manager):
    todo_list_manager.add_task("Task 1")
    todo_list_manager.add_task("Task 2")
    todo_list_manager.mark_task_as_done(1)
    todo_list_manager.save()
    todo_list_manager.todo_list.tasks = []  # Clear in-memory tasks

    todo_list_manager.load()
    tasks = todo_list_manager.todo_list.tasks
    assert len(tasks) == 2
    assert tasks[0].name == "Task 1"
    assert not tasks[0].is_done
    assert tasks[1].name == "Task 2"
    assert tasks[1].is_done

def test_csv_persistence_load_missing_file(persistence):
    """
    Ensure that loading a non-existent CSV file does not raise an error and returns an empty TodoList.
    """
    todo_list = persistence.load()
    assert isinstance(todo_list, TodoList)
    assert len(todo_list.tasks) == 0

def test_csv_persistence_save_and_load(temporary_csv, persistence):
    """
    Verify saving tasks to a CSV file and loading them back.
    """
    todo_list = TodoList()
    todo_list.add_task(Task("Task A"))
    task_b = Task("Task B")
    task_b.is_done = True
    todo_list.add_task(task_b)
    
    # Save tasks to CSV
    persistence.save(todo_list)
    
    # Load tasks from CSV
    loaded_todo_list = persistence.load()
    assert len(loaded_todo_list.tasks) == 2
    assert loaded_todo_list.tasks[0].name == "Task A"
    assert not loaded_todo_list.tasks[0].is_done
    assert loaded_todo_list.tasks[1].name == "Task B"
    assert loaded_todo_list.tasks[1].is_done
