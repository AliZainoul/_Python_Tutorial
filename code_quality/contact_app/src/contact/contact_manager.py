"""
    A module that holds a class that manages contacts via their names
"""

class ContactManager :
    """
        ContactManager a class that manages contacts via their names
    """
    def __init__(self):
        """
            Initializes the ContactManager instance
        """
        self._contacts = []

    def add_contact(self, contact: str) -> None:
        """
            Adds a contact to the contact list
            :param contact: The name of the contact to add
            :return: None
        """
        self._contacts.append(contact)

    def remove_contact(self, contact:str) -> bool:
        """
            Removes a contact from the contact list
            :param contact: The name of the contact to remove
            :return: True if the contact was removed, False otherwise
        """
        if contact in self._contacts:
            self._contacts.remove(contact)
            return True
        return False

    def list_contacts(self) -> list:
        """
            Lists all contacts in the contact list
            :return: A list of contacts
        """
        return self._contacts
