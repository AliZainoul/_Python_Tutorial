import pytest
from todolist.models.task import Task

'''
def test_task_default_values():
    task = Task()
    assert task.name == ""
    assert task.is_done is False

def test_task_default_value_name():
    task = Task(name = "Heyyy")
    assert task.name == "Heyyy"
    assert task.is_done is False

def test_task_default_value_is_done():
    task = Task(is_done = True)
    assert task.name == ""
    assert task.is_done is True

def test_task_values():
    task = Task(name = "Bidule", is_done = True)
    assert task.name == "Bidule"
    assert task.is_done is True

def test_task_set_name():
    task = Task(name="Write code")
    task.name = "Write tests"
    assert task.name == "Write tests"

def test_task_set_name_invalid():
    task = Task(name="Write code")
    with pytest.raises(TypeError):
        task.name = 123  # Invalid type

def test_task_set_is_done():
    task = Task(name="Write code", is_done=False)
    task.is_done = True
    assert task.is_done is True

def test_task_set_is_done_invalid():
    task = Task(name="Write code", is_done=False)
    with pytest.raises(TypeError):
        task.is_done = "yes"  # Invalid type

def test_task_str_representation():
    task = Task(name="Write code", is_done=False)
    assert str(task) == "Task name: Write code and its status is False.\n"



'''
import pytest

def test_task_default_values():
    task = Task()
    assert task.name == ""
    assert task.is_done is False

def test_task_default_value_name():
    task = Task(name = "Heyyy")
    assert task.name == "Heyyy"
    assert task.is_done is False

def test_task_default_value_is_done():
    task = Task(is_done = True)
    assert task.name == ""
    assert task.is_done is True

def test_task_values():
    task = Task(name = "Bidule", is_done = True)
    assert task.name == "Bidule"
    assert task.is_done is True

@pytest.fixture
def task():
    """Fixture that provides a default Task object."""
    return Task(name="Write code", is_done=False)

def test_task_set_name(task):
    task.name = "Write tests"
    assert task.name == "Write tests"

def test_task_set_name_invalid(task):
    with pytest.raises(TypeError):
        task.name = 123  # Invalid type

def test_task_set_is_done(task):
    task.is_done = True
    assert task.is_done is True

def test_task_set_is_done_invalid(task):
    with pytest.raises(TypeError):
        task.is_done = "yes"  # Invalid type

def test_task_str_representation(task):
    assert str(task) == "Task name: Write code and its status is False.\n"