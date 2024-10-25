import pytest

from todolist.models.task import Task
from todolist.models.todolist import TodoList
from todolist.persistence.csv_persistence import CsvPersistence

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

def test_save_and_load(persistence):
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
    assert loaded_todo_list.tasks[0].is_done == False
    assert loaded_todo_list.tasks[1].name == "Task B"
    assert loaded_todo_list.tasks[1].is_done == True

def test_load_empty_csv(persistence):
    """
    Test loading from an empty CSV file.
    """
    loaded_list = persistence.load()
    assert len(loaded_list.tasks) == 0  # No tasks in CSV

def test_load_missing_file(persistence):
    """
    Ensure that loading a non-existent CSV file does not raise an error and returns an empty TodoList.
    """
    todo_list = persistence.load()
    assert isinstance(todo_list, TodoList)
    assert len(todo_list.tasks) == 0

def test_save_creates_file(temporary_csv, persistence):
    """
    Test that saving a TodoList creates a CSV file.
    """
    todo_list = TodoList()
    todo_list.add_task(Task("Task C"))
    persistence.save(todo_list)

    assert temporary_csv.exists()  # The file should be created after saving

def test_csv_content_after_save_and_load(persistence):
    """
    Ensure that the content of the CSV is as expected after saving and loading.
    """
    todo_list = TodoList()
    todo_list.add_task(Task("Task D"))
    task_e = Task("Task E")
    task_e.is_done = True
    todo_list.add_task(task_e)

    # Save tasks to CSV
    persistence.save(todo_list)

    # Load tasks from CSV
    loaded_todo_list = persistence.load()
    assert len(loaded_todo_list.tasks) == 2
    assert loaded_todo_list.tasks[0].name == "Task D"
    assert not loaded_todo_list.tasks[0].is_done
    assert loaded_todo_list.tasks[1].name == "Task E"
    assert loaded_todo_list.tasks[1].is_done