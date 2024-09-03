from typing import List
import pandas as pd
from contact.models.contact import Contact
from contact.models.address import Address
from contact.models.contact_persistence import CsvPersistence

class ContactManager:
    """
    A class to manage contacts and their persistence.

    This class provides methods to add, update, delete, retrieve, and search for contacts. 
    It uses CSV files to persist contact data and manage it.

    Attributes:
        contacts_file (str): Path to the CSV file for storing contacts.
        addresses_file (str): Path to the CSV file for storing addresses.
        contacts_persistence (CsvPersistence): Persistence handler for contacts.
        addresses_persistence (CsvPersistence): Persistence handler for addresses.
        contacts (List[Contact]): List of contacts managed by the manager.
        addresses (List[Address]): List of addresses managed by the manager.
    """

    def __init__(self, contacts_file: str, addresses_file: str):
        """
        Initialize the ContactManager with file paths for contacts and addresses.

        Args:
            contacts_file (str): Path to the CSV file for storing contacts.
            addresses_file (str): Path to the CSV file for storing addresses.
        """
        self.contacts_file = contacts_file
        self.addresses_file = addresses_file
        self.contacts_persistence = CsvPersistence(contacts_file)
        self.addresses_persistence = CsvPersistence(addresses_file)
        self.contacts: List[Contact] = []
        self.addresses: List[Address] = []
        self.load_contacts()

    def add_contact(self, contact: Contact) -> None:
        """
        Add a new contact to the contact list and save it to the CSV file.

        Args:
            contact (Contact): The contact object to be added.
        """
        self.contacts.append(contact)
        self.save_contacts()

    def update_contact(self, contact_email: str, **kwargs) -> None:
        """
        Update an existing contact based on their email and provided keyword arguments.

        Args:
            contact_email (str): The email of the contact to be updated.
            **kwargs: The attributes to be updated and their new values.
        """
        for contact in self.contacts:
            if contact.email == contact_email:
                for key, value in kwargs.items():
                    setattr(contact, key, value)
                self.save_contacts()
                return

    def delete_contact(self, contact_email: str) -> None:
        """
        Delete a contact from the contact list based on their email and save the changes to the CSV file.

        Args:
            contact_email (str): The email of the contact to be deleted.
        """
        self.contacts = [c for c in self.contacts if c.email != contact_email]
        self.save_contacts()

    def get_all_contacts(self) -> List[Contact]:
        """
        Retrieve all contacts currently managed by the ContactManager.

        Returns:
            List[Contact]: The list of all contacts.
        """
        return self.contacts

    def search_contact(self, search_term: str) -> List[Contact]:
        """
        Search for contacts by a search term in their first name or last name.

        Args:
            search_term (str): The term to search for within contact names.

        Returns:
            List[Contact]: A list of contacts that match the search term.
        """
        search_term = search_term.lower()
        return [c for c in self.contacts if search_term in (c.first_name + " " + c.last_name).lower()]

    def save_contacts(self) -> None:
        """
        Save the current list of contacts to the CSV file.
        """
        df = pd.DataFrame([c.__dict__ for c in self.contacts])
        self.contacts_persistence.dump(df)

    def load_contacts(self) -> None:
        """
        Load contacts from the CSV file into the contact list.
        """
        df = self.contacts_persistence.load()
        self.contacts = [Contact(**row) for index, row in df.iterrows()]

    def save(self) -> None:
        """
        Save both contacts and addresses to their respective CSV files.
        """
        self.save_contacts()
        # You could also add saving logic for addresses if required

    def load(self) -> None:
        """
        Load both contacts and addresses from their respective CSV files.
        """
        self.load_contacts()
        # You could also add loading logic for addresses if required
