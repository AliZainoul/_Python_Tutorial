import sys
from contact.controller.contact_controller import Controller
from contact.ui.gui import App
from PyQt6.QtWidgets import QApplication

CONTACTS_FILE = "src/contact/data/contacts.csv"
ADDRESSES_FILE = "src/contact/data/addresses.csv"

class ContactApp:
    def __init__(self):
        self.controller = Controller(CONTACTS_FILE, ADDRESSES_FILE)
        self.view = None  # Initialize the GUI later

    def run(self):
        app = QApplication(sys.argv)  # Instantiate QApplication first
        self.view = App(self.controller)  # Now create the GUI
        self.controller.set_gui(self.view)
        # self.controller.populate()
        self.view.show()
        sys.exit(app.exec())