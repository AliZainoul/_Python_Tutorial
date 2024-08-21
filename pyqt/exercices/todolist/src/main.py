import sys
from PyQt6.QtWidgets import QApplication
from ui.todolist_ui import Todo, TodoListWindow

def main():
    app = QApplication(sys.argv)
    window = TodoListWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()