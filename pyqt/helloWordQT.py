import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Hello, PyQt!')
window.setGeometry(100, 100, 280, 80)
window.show()

sys.exit(app.exec())