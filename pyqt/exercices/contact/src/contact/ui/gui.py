# gui.py
import sys
import os
from typing import Optional

from contact.models.address import Address
from contact.models.contact import Contact
from contact.models.contact_table import ContactTableModel

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableView,
    QLineEdit, QFormLayout, QDialog, QDialogButtonBox
)
from PyQt6.QtCore import Qt


class AddContactDialog(QDialog):
    def __init__(self, contact: Optional[Contact] = None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Update Contact")
        self.init_ui(contact)

    def create_line_edit(self, label: str, layout: QFormLayout):
        line_edit = QLineEdit()
        layout.addRow(f"{label}:", line_edit)
        return line_edit

    def init_ui(self, contact: Optional[Contact]):
        form_layout = QFormLayout()

        # DRY creation of line edits
        self._first_name = self.create_line_edit("First Name", form_layout)
        self._last_name = self.create_line_edit("Last Name", form_layout)
        self._phone_number = self.create_line_edit("Phone Number", form_layout)
        self._email = self.create_line_edit("Email", form_layout)
        self._street = self.create_line_edit("Street", form_layout)
        self._city = self.create_line_edit("City", form_layout)
        self._state = self.create_line_edit("State", form_layout)
        self._zipcode = self.create_line_edit("Zipcode", form_layout)
        self._country = self.create_line_edit("Country", form_layout)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(buttons)
        self.setLayout(main_layout)

        if contact:
            self.load_contact_data(contact)

    def load_contact_data(self, contact: Contact):
        self._first_name.setText(contact.first_name)
        self._last_name.setText(contact.last_name)
        self._phone_number.setText(contact.phone_number)
        self._email.setText(contact.email)
        if contact.address:
            self._street.setText(contact.address.street)
            self._city.setText(contact.address.city)
            self._state.setText(contact.address.state)
            self._zipcode.setText(contact.address.zipcode)
            self._country.setText(contact.address.country)

    def get_contact_data(self) -> dict:
        return {
            '_first_name': self._first_name.text(),
            '_last_name': self._last_name.text(),
            '_phone_number': self._phone_number.text(),
            '_email': self._email.text(),
            '_address': Address(
                self._street.text(),
                self._city.text(),
                self._state.text(),
                self._zipcode.text(),
                self._country.text()
            )
        }


class App(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.selected_contact = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Contact Manager")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()
        footer_layout = QHBoxLayout()
        search_layout = QFormLayout()

        header = QLabel('Welcome')
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        self.contact_table = QTableView()
        self.contact_model = ContactTableModel(self.controller.get_all_contacts())
        self.contact_table.setModel(self.contact_model)
        self.contact_table.selectionModel().selectionChanged.connect(self.select_contact)

        main_layout.addWidget(self.contact_table)

        self.search_bar = QLineEdit()
        self.search_bar.textChanged.connect(self.search_contact)
        search_layout.addRow('Search:', self.search_bar)
        main_layout.addLayout(search_layout)

        # DRY Button creation
        self.create_button("Add", footer_layout, self.show_add_contact_dialog)
        self.create_button("Update", footer_layout, self.show_update_contact_dialog)
        self.create_button("Delete", footer_layout, self.delete_selected_contact)

        main_layout.addLayout(footer_layout)
        self.setLayout(main_layout)

    def create_button(self, label: str, layout: QHBoxLayout, handler):
        button = QPushButton(label)
        button.clicked.connect(handler)
        layout.addWidget(button)

    def load_contacts(self):
        contacts = self.controller.get_all_contacts()
        self.contact_model.update_data(contacts)

    def search_contact(self):
        search_term = self.search_bar.text().strip()
        contacts = self.controller.search_contact(search_term)
        self.contact_model.update_data(contacts)

    def select_contact(self):
        indexes = self.contact_table.selectionModel().selectedRows()
        if indexes:
            selected_index = indexes[0]
            self.selected_contact = self.contact_model.get_contact_at_index(selected_index)

    def delete_selected_contact(self):
        if self.selected_contact:
            self.controller.delete_contact(self.selected_contact.email)
            self.load_contacts()
            self.selected_contact = None

    def handle_contact_dialog(self, contact: Optional[Contact] = None):
        dialog = AddContactDialog(contact=contact, parent=self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            contact_data = dialog.get_contact_data()
            print(contact_data)
            if contact:
                # Update existing contact
                self.controller.update_contact(contact.email, **contact_data)
            else:
                # Add new contact
                new_contact = Contact(**contact_data)
                self.controller.add_contact(new_contact)
            self.load_contacts()

    def show_add_contact_dialog(self):
        self.handle_contact_dialog()

    def show_update_contact_dialog(self):
        if self.selected_contact:
            self.handle_contact_dialog(contact=self.selected_contact)
