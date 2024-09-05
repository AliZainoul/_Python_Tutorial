# contact_controller.py
import sys
import os
# Adjust the path to include the src directory for importing modules
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from contact.models.contact import Contact
from contact.models.contact_manager import ContactManager
from contact.ui.gui import App

class Controller:
    def __init__(self, contacts_file: str, addresses_file: str):
        self.contact_manager = ContactManager(contacts_file, addresses_file)
        self.gui = None

    def set_gui(self, gui: App):
        self.gui = gui

    def add_contact(self, contact: Contact) -> None:
        self.contact_manager.add_contact(contact)
        if self.gui:
            self.gui.load_contacts()

    def update_contact(self, contact_email: str, **kwargs) -> None:
        self.contact_manager.update_contact(contact_email, **kwargs)
        if self.gui:
            self.gui.load_contacts()

    def delete_contact(self, contact_email: str) -> None:
        self.contact_manager.delete_contact(contact_email)
        if self.gui:
            self.gui.load_contacts()

    def get_all_contacts(self) -> list[Contact]:
        return self.contact_manager.get_all_contacts()

    def search_contact(self, search_term: str) -> list[Contact]:
        return self.contact_manager.search_contact(search_term)

    def populate(self, count: int = 10) -> None:
        self.contact_manager.populate(count)
