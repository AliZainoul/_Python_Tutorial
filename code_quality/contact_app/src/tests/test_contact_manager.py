import pytest
from contact.contact_manager import ContactManager

@pytest.fixture
def manager():
    return ContactManager()

def test_add_contact(manager):
    manager.add_contact("Alice")
    assert "Alice" in manager.list_contacts()

def test_remove_existing_contact(manager):
    manager.add_contact("Bob")
    removed = manager.remove_contact("Bob")
    assert removed is True
    assert "Bob" not in manager.list_contacts()

def test_remove_non_existing_contact(manager):
    removed = manager.remove_contact("Charlie")
    assert removed is False

def test_list_contacts_initially_empty(manager):
    assert manager.list_contacts() == []

def test_multiple_contacts(manager):
    contacts = ["Alice", "Bob", "Charlie"]
    for c in contacts:
        manager.add_contact(c)
    assert manager.list_contacts() == contacts
