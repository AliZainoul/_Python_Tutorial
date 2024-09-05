import pytest
import os
from contact.models.address import Address
from contact.models.contact import Contact
from contact.models.contact_manager import ContactManager

# Define constants for file paths
FILE_PATH_CONTACTS = "src/tests/data_test/contacts.csv"
FILE_PATH_ADDRESSES = "src/tests/data_test/addresses.csv"
DIRECTORY = "src/tests/data_test"

@pytest.fixture
def contact_manager():
    """Fixture for setting up and tearing down a ContactManager instance."""
    os.makedirs(DIRECTORY, exist_ok=True)
    contacts_file = FILE_PATH_CONTACTS
    addresses_file = FILE_PATH_ADDRESSES
    
    # Ensure files do not exist before the test
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
    """Test adding a contact to the contact manager."""
    address = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact = Contact("John", "Doe", "1234567890", "john@example.com", address)
    contact_manager.add_contact(contact)
    
    contacts = contact_manager.get_all_contacts()
    
    assert len(contacts) == 1
    assert contacts[0].first_name == "John"
    assert contacts[0].last_name == "Doe"

def test_update_contact(contact_manager):
    """Test updating a contact in the contact manager."""
    address = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact = Contact("John", "Doe", "1234567890", "john@example.com", address)
    contact_manager.add_contact(contact)
    
    contact_manager.update_contact("john@example.com", first_name="Jane", phone_number="0987654321")
    
    updated_contact = contact_manager.get_all_contacts()[0]
    
    assert updated_contact.first_name == "Jane"
    assert updated_contact.phone_number == "0987654321"

def test_delete_contact(contact_manager):
    """Test deleting a contact from the contact manager."""
    address = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact = Contact("John", "Doe", "1234567890", "john@example.com", address)
    contact_manager.add_contact(contact)
    
    contact_manager.delete_contact("john@example.com")
    
    contacts = contact_manager.get_all_contacts()
    
    assert len(contacts) == 0

def test_get_all_contacts(contact_manager):
    """Test retrieving all contacts from the contact manager."""
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
    """Test searching for a contact in the contact manager."""
    address = Address("1234 Python Lane", "PyCity", "PyState", "12345", "PyCountry")
    contact = Contact("John", "Doe", "1234567890", "john@example.com", address)
    contact_manager.add_contact(contact)
    
    result = contact_manager.search_contact("John")
    
    assert len(result) == 1
    assert result[0].first_name == "John"
    assert result[0].last_name == "Doe"

def test_save_and_load_contacts(contact_manager):
    """Test saving and loading contacts from the CSV file."""
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

def test_populate(contact_manager):
    """Test populating the contact manager with random contacts."""
    NUM_CONTACTS = 10
    existing_contacts_len = len(contact_manager.get_all_contacts())
    contact_manager.populate(NUM_CONTACTS)
    contacts = contact_manager.get_all_contacts()
    
    assert len(contacts) == NUM_CONTACTS + existing_contacts_len
    
    # Optional: Check that each contact has valid data
    for contact in contacts:
        assert contact.first_name != ""
        assert contact.last_name != ""
        assert contact.phone_number != ""
        assert contact.email != ""
        assert isinstance(contact.address, Address)
        assert contact.address.street != ""
        assert contact.address.city != ""
        assert contact.address.state != ""
        assert contact.address.zipcode != ""
        assert contact.address.country != ""
