from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel

app = QApplication([])

window = QWidget()
window.setWindowTitle('My Title : Hello, PyQt!')

my_label = QLabel("Hello World! ")
my_layout = QHBoxLayout()
my_layout.addWidget(my_label)

window.setGeometry(100, 100, 280, 80)
window.setLayout(my_layout)
window.show()

app.exec()

app.quit()