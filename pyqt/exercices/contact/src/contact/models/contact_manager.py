from typing import List
import pandas as pd
from faker import Faker
from contact.models.contact import Contact
from contact.models.address import Address
from contact.models.contact_persistence import CsvPersistence

class ContactManager:
    """
    A class to manage contacts and their persistence in CSV files.
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
        self.contacts: List[Contact] = []
        self.load_contacts()

    def add_contact(self, contact: Contact) -> None:
        """
        Add a new contact and save to the CSV file.

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
        contact = self._find_contact_by_email(contact_email)
        if contact:
            for key, value in kwargs.items():
                setattr(contact, key, value)
            self.save_contacts()

    def delete_contact(self, contact_email: str) -> None:
        """
        Delete a contact from the contact list and save the changes to the CSV file.

        Args:
            contact_email (str): The email of the contact to be deleted.
        """
        self.contacts = [c for c in self.contacts if c.email != contact_email]
        self.save_contacts()

    def get_all_contacts(self) -> List[Contact]:
        """
        Retrieve all contacts.

        Returns:
            List[Contact]: The list of all contacts.
        """
        return self.contacts

# contact_manager.py (or wherever ContactManager is defined)

    def search_contact(self, search_term: str) -> list[Contact]:
        """
        Search for contacts by a search term in any of the contact fields:
        first name, last name, phone number, email, or any part of the address.

        Args:
            search_term (str): The term to search for.

        Returns:
            List[Contact]: A list of contacts that match the search term.
        """
        search_term = search_term.lower()
        results = []
        for contact in self.contacts:
            # Combine all searchable fields into a single string
            contact_info = (
                f"{contact.first_name} {contact.last_name} {contact.phone_number} "
                f"{contact.email} {contact.address.street if contact.address else ''} "
                f"{contact.address.city if contact.address else ''} "
                f"{contact.address.state if contact.address else ''} "
                f"{contact.address.zipcode if contact.address else ''} "
                f"{contact.address.country if contact.address else ''}"
            ).lower()
            
            if search_term in contact_info:
                results.append(contact)

        return results


    def save_contacts(self) -> None:
        """
        Save the current list of contacts to the CSV file.
        """
        df = pd.DataFrame([self._contact_to_dict(c) for c in self.contacts])
        self.contacts_persistence.dump(df)

    def load_contacts(self) -> None:
        """
        Load contacts from the CSV file into the contact list.
        """
        df = self.contacts_persistence.load()
        self.contacts = [self._dict_to_contact(row) for _, row in df.iterrows()]

    def save(self) -> None:
        """
        Save both contacts and addresses to their respective CSV files.
        """
        self.save_contacts()
        # Optional: Add logic for saving addresses if needed

    def load(self) -> None:
        """
        Load both contacts and addresses from their respective CSV files.
        """
        self.load_contacts()
        # Optional: Add logic for loading addresses if needed

    def populate(self, count: int = 10) -> None:
        """
        Populate the contact manager with a given number of randomly generated contacts.

        Parameters:
            count (int): The number of contacts to generate. Defaults to 10.
        """
        fake = Faker()
        for _ in range(count):
            contact = Contact(
                fake.first_name(),
                fake.last_name(),
                fake.phone_number(),
                fake.email(),
                Address(
                    fake.street_address(),
                    fake.city(),
                    fake.state(),
                    fake.zipcode(),
                    fake.country()
                )
            )
            self.add_contact(contact)

    def _find_contact_by_email(self, email: str) -> Contact:
        """
        Helper method to find a contact by email.

        Args:
            email (str): The email of the contact to find.

        Returns:
            Contact: The contact with the given email, or None if not found.
        """
        for contact in self.contacts:
            if contact.email == email:
                return contact
        return None

    def _contact_to_dict(self, contact: Contact) -> dict:
        """
        Convert a Contact object to a dictionary.

        Args:
            contact (Contact): The contact object to convert.

        Returns:
            dict: The dictionary representation of the contact.
        """
        return {
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'phone_number': contact.phone_number,
            'email': contact.email,
            'address': str(contact.address)  # Ensure address is formatted properly for CSV
        }

    def _dict_to_contact(self, row: pd.Series) -> Contact:
        """
        Convert a DataFrame row to a Contact object.

        Args:
            row (pd.Series): The DataFrame row to convert.

        Returns:
            Contact: The Contact object constructed from the row.
        """
        address_parts = row['address'].split(', ')
        address = Address(*address_parts)
        return Contact(
            row['first_name'],
            row['last_name'],
            row['phone_number'],
            row['email'],
            address
        )
