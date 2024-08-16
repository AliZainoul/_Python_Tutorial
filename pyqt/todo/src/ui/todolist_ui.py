import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
    QCheckBox,
    QLabel,
)
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QDrag
from PyQt6.QtCore import Qt, QMimeData
import qtawesome as qta

# from todolist import TodoList
# todolist is the folder containing todolist.py
# with __init__ file containing: 
# from todolist import TodoList

# OR:
from todolist.todolist import TodoList


class Todo(QWidget):
    check = pyqtSignal(str, bool)
    remove = pyqtSignal(str)

    def __init__(self, text: str, checked: bool = False):
        super().__init__()
        self.__text = text
        self.__checked = checked
        self.create_ui()

    def create_ui(self):
        """Create the UI"""
        main_layout = QHBoxLayout()

        left_layout = QHBoxLayout()
        self.checkbox = QCheckBox()
        self.checkbox.stateChanged.connect(self.checkbox_state_changed)
        self.label = QLabel(self.__text)
        left_layout.addWidget(self.checkbox)
        left_layout.addWidget(self.label)

        main_layout.addLayout(left_layout)

        main_layout.addStretch()

        if self.__checked:
            font = self.label.font()
            font.setStrikeOut(True)
            self.label.setFont(font)
            self.checkbox.setChecked(True)

        trash_icon = qta.icon("mdi6.trash-can-outline")
        self.btn_delete = QPushButton(trash_icon, "")
        self.btn_delete.clicked.connect(self.fire_remove)
        main_layout.addWidget(self.btn_delete)

        self.setLayout(main_layout)

    @property
    def text(self) -> str:
        return self.__text

    @property
    def checked(self) -> bool:
        return self.__checked

    @checked.setter
    def checked(self, value: bool):
        self.__checked = value
        font = self.label.font()
        font.setStrikeOut(value)
        self.label.setFont(font)
        self.checkbox.setChecked(value)

    def mouseMoveEvent(self, e):
        """Handle the mouse move event"""
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            drag.exec(Qt.DropAction.MoveAction)

    def checkbox_state_changed(self, state: bool):
        """Handle the checkbox state change"""
        self.checked = state
        self.check.emit(self.__text, self.__checked)

    def fire_remove(self):
        """Fire the remove signal"""
        self.remove.emit(self.__text)


class TodoListWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.setWindowTitle("Todo list")
        self.todolist = TodoList()
        self.todolist.add("Buy milk")
        self.todolist.add("Buy coffee")

        self.create_ui()
        self.show_todo_list()

    def create_ui(self):
        """Create the UI"""
        widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.h_layout = QHBoxLayout()
        self.input = QLineEdit()
        self.btn_add = QPushButton("Add")
        self.btn_add.clicked.connect(self.add_todo_handler)
        self.h_layout.addWidget(self.input)
        self.h_layout.addWidget(self.btn_add)
        self.main_layout.addLayout(self.h_layout)

        self.todo_layout = QVBoxLayout()
        self.main_layout.addLayout(self.todo_layout)

        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def add_todo_handler(self):
        """Add a new todo to the list"""
        self.todolist.add(self.input.text())
        self.input.setText("")
        self.input.setFocus()
        self.show_todo_list()

    def show_todo_list(self):
        """Show the list of todos"""
        self.remove_all_todos()
        for todo in self.todolist.todos:
            todo = Todo(todo.text, todo.checked)
            todo.check.connect(self.check_todo_handler)
            todo.remove.connect(self.remove_todo_handler)
            self.todo_layout.addWidget(todo)

    def remove_all_todos(self):
        """Remove all todos from the layout"""
        while self.todo_layout.count():
            item = self.todo_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def check_todo_handler(self, text: str, checked: bool):
        """Check a todo"""
        self.todolist.set_checked(text, checked)

    def remove_todo_handler(self, text: str):
        """Remove a todo from the list"""
        self.todolist.remove(text)
        self.show_todo_list()

    def dragEnterEvent(self, e):
        """Handle the drag event"""
        e.accept()

    def dropEvent(self, e):
        """Handle the drop event"""
        pos = e.position()
        widget = e.source()
        self.todo_layout.removeWidget(widget)
        print("Count", self.todo_layout.count())

        for n in range(self.todo_layout.count()):
            # Get the widget at each index in turn.
            widget = self.todo_layout.itemAt(n).widget()
            if pos.y() < widget.y() + widget.size().height() // 2:
                # We didn't drag past this widget.
                # insert to the top of it.
                print("break", n)
                break
        else:
            # This block is executed if the loop does not break,
            # meaning the dragged item is below all the widgets in the layout.
            # We aren't on the bottom hand side of any widget,
            # so we're at the end. Increment 1 to insert after.
            n += 1
            print("else", n)

        self.todo_layout.insertWidget(n, widget)

        e.accept()
