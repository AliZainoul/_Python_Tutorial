import pytest
import os
import pandas as pd
from contact.models.contact import Contact
from contact.models.address import Address
from contact.models.contact_manager import ContactManager

# Define constants for file paths
FILE_PATH_CONTACTS = "src/contact/tests/data_test_contact_manager/test_contacts.csv"
FILE_PATH_ADDRESSES = "src/contact/tests/data_test_contact_manager/test_addresses.csv"
DIRECTORY = "src/contact/tests/data_test_contact_manager"

@pytest.fixture
def contact_manager():
    """Fixture for setting up and tearing down a ContactManager instance."""
    # Ensure the directory exists
    os.makedirs(DIRECTORY, exist_ok=True)

    # Create temporary files for testing
    contacts_file = FILE_PATH_CONTACTS
    addresses_file = FILE_PATH_ADDRESSES
    
    # Ensure files do not exist before test
    if os.path.exists(contacts_file):
        os.remove(contacts_file)
    if os.path.exists(addresses_file):
        os.remove(addresses_file)
    
    manager = ContactManager(contacts_file, addresses_file)
    yield manager
    
    # Teardown - remove temporary files after tests
    if os.path.exists(contacts_file):
        os.remove(contacts_file)
    if os.path.exists(addresses_file):
        os.remove(addresses_file)

def test_add_contact(contact_manager):
    address = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact = Contact("John", "Doe", "1234567890", "john@example.com", address)
    contact_manager.add_contact(contact)
    
    contacts = contact_manager.get_all_contacts()
    
    assert len(contacts) == 1
    assert contacts[0].first_name == "John"
    assert contacts[0].last_name == "Doe"

def test_update_contact(contact_manager):
    address = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact = Contact("John", "Doe", "1234567890", "john@example.com", address)
    contact_manager.add_contact(contact)
    
    contact_manager.update_contact("john@example.com", first_name="Jane", phone_number="0987654321")
    
    updated_contact = contact_manager.get_all_contacts()[0]
    
    assert updated_contact.first_name == "Jane"
    assert updated_contact.phone_number == "0987654321"

def test_delete_contact(contact_manager):
    address = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact = Contact("John", "Doe", "1234567890", "john@example.com", address)
    contact_manager.add_contact(contact)
    
    contact_manager.delete_contact("john@example.com")
    
    contacts = contact_manager.get_all_contacts()
    
    assert len(contacts) == 0

def test_get_all_contacts(contact_manager):
    address1 = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact1 = Contact("John", "Doe", "1234567890", "john@example.com", address1)
    contact_manager.add_contact(contact1)
    
    address2 = Address("5678 Java Ave", "JavaTown", "JavaState", "67890", "JavaCountry")
    contact2 = Contact("Jane", "Smith", "0987654321", "jane@example.com", address2)
    contact_manager.add_contact(contact2)
    
    contacts = contact_manager.get_all_contacts()
    
    assert len(contacts) == 2
    assert any(c.first_name == "John" and c.last_name == "Doe" for c in contacts)
    assert any(c.first_name == "Jane" and c.last_name == "Smith" for c in contacts)

def test_search_contact(contact_manager):
    address = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact = Contact("John", "Doe", "1234567890", "john@example.com", address)
    contact_manager.add_contact(contact)
    
    result = contact_manager.search_contact("John")
    
    assert len(result) == 1
    assert result[0].first_name == "John"
    assert result[0].last_name == "Doe"

def test_persistence(contact_manager):
    address = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact = Contact("John", "Doe", "1234567890", "john@example.com", address)
    contact_manager.add_contact(contact)
    
    # Save the data to file
    contact_manager.save()

    # Create a new ContactManager instance and load data from file
    new_manager = ContactManager(FILE_PATH_CONTACTS, FILE_PATH_ADDRESSES)
    new_manager.load_contacts()
    
    contacts = new_manager.get_all_contacts()

    assert len(contacts) == 1
    assert contacts[0].first_name == "John"
    assert contacts[0].last_name == "Doe"
    assert str(contacts[0].phone_number) == "1234567890"
    assert contacts[0].email == "john@example.com"
