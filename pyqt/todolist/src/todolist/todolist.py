class Todo:
    """A simple todo"""

    def __init__(self, text):
        self.text = text
        self.checked = False

    def __str__(self):
        return f"Title: {self.text}, checked: {self.checked}"


class TodoList:
    """A simple todo list"""

    def __init__(self):
        self.todos = []

    def add(self, text):
        """Add a new todo to the list"""
        self.todos.append(Todo(text))

    def remove(self, text: str):
        """Remove a todo from the list"""
        todo = self.find_todo_by_title(text)
        if todo:
            self.todos.remove(todo)
        else:
            raise ValueError(f"Todo with title {text} not found")

    def find_todo_by_title(self, text: str) -> Todo:
        """Find a todo by its title"""
        for todo in self.todos:
            if todo.text == text:
                return todo
        return None

    def set_checked(self, text, checked=True):
        """Set the checked status of a todo"""
        todo = self.find_todo_by_title(text)
        if todo:
            todo.checked = checked
        return todo

    def __str__(self):
        return "\n".join([str(todo) for todo in self.todos])


tdl = TodoList()
tdl.add("Buy milk")
print(str(tdl))
