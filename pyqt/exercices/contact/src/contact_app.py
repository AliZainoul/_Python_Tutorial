import sys
from contact.controller.contact_controller import Controller
from contact.ui.gui import App
from PyQt6.QtWidgets import QApplication

class ContactApp:
    def __init__(self):
        self.CONTACTS_FILE = "src/contact/data/contacts.csv"
        self.ADDRESSES_FILE = "src/contact/data/addresses.csv"
        self.controller = Controller(self.CONTACTS_FILE, self.ADDRESSES_FILE)
        self.gui = None  # Initialize the GUI later

    def run(self):
        app = QApplication(sys.argv)  # Instantiate QApplication first
        self.gui = App(self.controller)  # Now create the GUI
        self.controller.set_gui(self.gui)
        self.controller.populate()
        self.gui.show()
        sys.exit(app.exec())