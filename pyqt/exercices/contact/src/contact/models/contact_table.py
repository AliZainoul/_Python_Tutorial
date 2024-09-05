from typing import Optional

from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from contact.models.address import Address
from contact.models.contact import Contact


class ContactTableModel(QAbstractTableModel):
    def __init__(self, contacts: list[Contact]):
        super().__init__()
        self.contacts = contacts
        self.headers = ["First Name", "Last Name", "Phone Number", "Email", "Address"]

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.contacts)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.headers)

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole) -> QVariant:
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return QVariant()

        contact = self.contacts[index.row()]
        column = index.column()

        match column:
                case 0:
                    return QVariant(contact.first_name)
                case 1:
                    return QVariant(contact.last_name)
                case 2:
                    return QVariant(contact.phone_number)
                case 3:
                    return QVariant(contact.email)
                case 4:
                    address = contact.address
                    if address:
                        return QVariant(f"{address.street}, {address.city}, {address.state}, {address.zipcode}, {address.country}")
                    return QVariant("No Address")
                case _:
                    return QVariant()

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return QVariant(self.headers[section])
        return QVariant()

    def get_contact_at_index(self, index: QModelIndex) -> Optional[Contact]:
        if index.isValid():
            return self.contacts[index.row()]
        return None

    def update_data(self, contacts: list[Contact]):
        self.beginResetModel()
        self.contacts = contacts
        self.endResetModel()
