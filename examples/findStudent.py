"""
This script defines a list of students and provides functions to find students based on their ID, age, or name 
with various comparison operations.

The script includes the following functionalities:
1. `find_by_id`: Finds students by their ID using a specified comparison operation.
2. `find_by_age`: Finds students by their age using a specified comparison operation.
3. `find_by_name`: Finds students by their name using a specified comparison operation.
4. `find_student`: Combines the above functions to search for students based on multiple criteria.

The script also demonstrates usage examples by calling `find_student` with different arguments.
"""

# List of students, each represented as a tuple (ID, name, age)
students = [
    (1, "marc", 30),
    (2, "michel", 30),
    (3, "michel", 40),
    (4, "luc", 30),
]

# Constants representing the index positions for ID, name, and age in the student tuples
STUDENT_INDEX_ID = 0
STUDENT_INDEX_NAME = 1
STUDENT_INDEX_AGE = 2

# Dictionary mapping operation symbols to their corresponding lambda functions
operations = {
    "sw": lambda a, b: a.startswith(b),  # Starts with
    "ew": lambda a, b: a.endswith(b),    # Ends with
    "=": lambda a, b: a == b,            # Equals
    ">": lambda a, b: a > b,              # Greater than
    ">=": lambda a, b: a >= b,            # Greater than or equal to
    "<": lambda a, b: a < b,              # Less than
    "<=": lambda a, b: a <= b,            # Less than or equal to
}

def find_by_id(students, id, op="="):
    """
    Finds students by their ID using the specified comparison operation.

    Parameters:
    students (list of tuples): The list of students.
    id (int): The ID to compare.
    op (str, optional): The comparison operation to use (default is "=").

    Returns:
    list of tuples: Students that match the ID comparison.
    """
    return [student for student in students if operations[op](student[STUDENT_INDEX_ID], id)]

def find_by_age(students, age, op="="):
    """
    Finds students by their age using the specified comparison operation.

    Parameters:
    students (list of tuples): The list of students.
    age (int): The age to compare.
    op (str, optional): The comparison operation to use (default is "=").

    Returns:
    list of tuples: Students that match the age comparison.
    """
    return [student for student in students if operations[op](student[STUDENT_INDEX_AGE], age)]

def find_by_name(students, name, op="="):
    """
    Finds students by their name using the specified comparison operation.

    Parameters:
    students (list of tuples): The list of students.
    name (str): The name to compare.
    op (str, optional): The comparison operation to use (default is "=").

    Returns:
    list of tuples: Students that match the name comparison.
    """
    return [student for student in students if operations[op](student[STUDENT_INDEX_NAME], name)]

def find_student(id=None, id_op="=", name=None, name_op="=", age=None, age_op="="):
    """
    Finds students by their ID, age, and/or name using specified comparison operations.

    Parameters:
    id_op (str, optional): The comparison operation for ID (default is "=").
    age_op (str, optional): The comparison operation for age (default is "=").
    name_op (str, optional): The comparison operation for name (default is "=").
    id (int, optional): The ID to compare (default is None).
    name (str, optional): The name to compare (default is None).
    age (int, optional): The age to compare (default is None).

    Returns:
    list of tuples: Students that match all specified comparisons.
    """
    ops = dict()
    if id:
        ops["id"] = (id, id_op, find_by_id)
    if name:
        ops["name"] = (name, name_op, find_by_name)
    if age:
        ops["age"] = (age, age_op, find_by_age)

    result = students
    for key, (value, op, fn) in ops.items():
        result = fn(result, value, op)

    return result

# Example usage of the find_student function

# First three calls is with 1 parameter (ID or NAME or AGE)
print(find_student(id=1))
print(find_student(name="michel"))
print(find_student(age=30))

print(find_student(id=1, id_op = ">"))
print(find_student(name="l", name_op = "ew"))
print(find_student(age=30, age_op = ">="))

print(find_student(name="michel", age = 30))
print(find_student(name="mi", name_op="sw", age = 30, age_op=">"))
print(find_student(id=1, id_op=">", age = 30))
print(find_student(id=1, id_op=">", age = 40, age_op="<", name="m", name_op = "sw"))

