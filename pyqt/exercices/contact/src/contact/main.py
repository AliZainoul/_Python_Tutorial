from models.contact import Contact
from models.address import Address

def main():
    # Create an Address object
    address = Address(
        _street="1234 Python Lane",
        _city="Pythontown",
        _state="PY",
        _zipcode="12345",
        _country="Pythonland"
    )

    # Create a Contact object
    contact = Contact(
        _first_name="John",
        _last_name="Doe",
        _phone_number="1234567890",
        _email="john@example.com",
        _address=address
    )

    # Display the contact details
    print("Contact Details:")
    print(contact)

    # Update the contact's first name and email
    contact.first_name = "Jane"
    contact.email = "jane.doe@example.com"
    
    # Render the contact details after update
    print("\nUpdated Contact Details:")
    print(str(contact))

    # Update multiple fields using update_contact method
    contact.update_contact(
        first_name="Janet",
        last_name="Smith",
        phone_number="0987654321"
    )
    
    # Display the updated contact details
    print("\nUpdated Contact Details After Using update_contact():")
    print(contact)

if __name__ == "__main__":
    main()
