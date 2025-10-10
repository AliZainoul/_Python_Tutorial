import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt

app = QApplication([])

window = QWidget()
window.setWindowTitle('My Title : Hello, PyQt!')

my_label = QLabel("Hello World! ")
my_layout = QHBoxLayout()
my_layout.addWidget(my_label, alignment=Qt.AlignmentFlag.AlignCenter)

window.setGeometry(100, 0, 280, 80)
window.setLayout(my_layout)
window.show()

sys.exit(app.exec())