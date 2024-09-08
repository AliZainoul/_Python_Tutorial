import pytest
from contact.models.contact import Contact
from contact.models.address import Address

@pytest.fixture
def sample_address():
    """
    Fixture to create a sample Address instance.
    """
    return Address("1234 Python Lane", "Pythontown", "PY", "12345", "Pythonland")

@pytest.fixture
def sample_contact(sample_address):
    """
    Fixture to create a sample Contact instance using the sample_address fixture.
    """
    return Contact("John", "Doe", "1234567890", "john@example.com", sample_address)

# Tests for Address class
def test_address_initialization(sample_address):
    assert sample_address.street == "1234 Python Lane"
    assert sample_address.city == "Pythontown"
    assert sample_address.state == "PY"
    assert sample_address.zipcode == "12345"
    assert sample_address.country == "Pythonland"

def test_address_setters_and_getters(sample_address):
    sample_address.street = "5678 Code St"
    assert sample_address.street == "5678 Code St"
    
    sample_address.city = "Codetown"
    assert sample_address.city == "Codetown"
    
    sample_address.state = "CT"
    assert sample_address.state == "CT"
    
    sample_address.zipcode = "67890"
    assert sample_address.zipcode == "67890"
    
    sample_address.country = "Codeland"
    assert sample_address.country == "Codeland"

# Tests for Contact class
def test_contact_initialization(sample_contact, sample_address):
    assert sample_contact.first_name == "John"
    assert sample_contact.last_name == "Doe"
    assert sample_contact.phone_number == "1234567890"
    assert sample_contact.email == "john@example.com"
    assert sample_contact.address == sample_address

def test_contact_setters_and_getters(sample_contact):
    sample_contact.first_name = "Jane"
    assert sample_contact.first_name == "Jane"

    sample_contact.last_name = "Smith"
    assert sample_contact.last_name == "Smith"

    sample_contact.phone_number = "0987654321"
    assert sample_contact.phone_number == "0987654321"

    sample_contact.email = "jane@example.com"
    assert sample_contact.email == "jane@example.com"

    new_address = Address("5678 Code St", "Codetown", "CT", "67890", "Codeland")

    print(f"Type of new_address: {type(new_address)}")
    print(f"Type expected: {Address}")
    print(f"new_address: {new_address}")
    
    assert isinstance(new_address, Address)  # This should pass
    sample_contact.address = new_address  # If this fails, print debug info

    assert sample_contact.address == new_address  # Ensure that the address was set correctly


def test_render_contact(sample_contact):
    expected_output = (
        "Name: John Doe\n"
        "Phone: 1234567890\n"
        "Email: john@example.com\n"
        "1234 Python Lane, Pythontown, PY, 12345, Pythonland"
    )
    assert str(sample_contact) == expected_output

def test_update_contact(sample_contact):
    sample_contact.update_contact(first_name="Jane", last_name="Smith", phone_number="0987654321")
    
    assert sample_contact.first_name == "Jane"
    assert sample_contact.last_name == "Smith"
    assert sample_contact.phone_number == "0987654321"