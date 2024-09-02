from dataclasses import dataclass, field
from typing import Optional
from contact.models.address import Address

@dataclass
class Contact:
    """
    A class to represent a contact person.

    Attributes:
    ----------
    _first_name : str
        The first name of the contact.
    _last_name : str
        The last name of the contact.
    _phone_number : str
        The contact's phone number.
    _email : str
        The contact's email address.
    _address : Optional[Address]
        The contact's physical address, which is optional.

    Methods:
    -------
    first_name() -> str:
        Gets the contact's first name.
    first_name(value: str) -> None:
        Sets the contact's first name with validation.
    
    last_name() -> str:
        Gets the contact's last name.
    last_name(value: str) -> None:
        Sets the contact's last name with validation.
    
    phone_number() -> str:
        Gets the contact's phone number.
    phone_number(value: str) -> None:
        Sets the contact's phone number with validation.
    
    email() -> str:
        Gets the contact's email address.
    email(value: str) -> None:
        Sets the contact's email address with validation.
    
    address() -> Optional[Address]:
        Gets the contact's address.
    address(value: Address) -> None:
        Sets the contact's address with type validation.
    
    render_contact() -> str:
        Returns a formatted string with the full contact details.
    
    __str__() -> str:
        Returns a nicely formatted string representation of the contact.
    
    update_contact(**kwargs) -> None:
        Updates the contact's attributes with the given keyword arguments.
    
    __del__() -> None:
        Destructor method that provides a message when a contact is deleted.
    """

    _first_name: str
    _last_name: str
    _phone_number: str
    _email: str
    _address: Optional[Address] = field(default=None)

    @property
    def first_name(self) -> str:
        """
        Gets the first name of the contact.
        
        Returns:
        -------
        str:
            The contact's first name.
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """
        Sets the first name of the contact with validation.

        Parameters:
        ----------
        value : str
            The new first name of the contact.

        Raises:
        ------
        ValueError:
            If the first name is empty.
        """
        if not value:
            raise ValueError("First name cannot be empty")
        self._first_name = value

    @property
    def last_name(self) -> str:
        """
        Gets the last name of the contact.
        
        Returns:
        -------
        str:
            The contact's last name.
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        Sets the last name of the contact with validation.

        Parameters:
        ----------
        value : str
            The new last name of the contact.

        Raises:
        ------
        ValueError:
            If the last name is empty.
        """
        if not value:
            raise ValueError("Last name cannot be empty")
        self._last_name = value

    @property
    def phone_number(self) -> str:
        """
        Gets the phone number of the contact.
        
        Returns:
        -------
        str:
            The contact's phone number.
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str) -> None:
        """
        Sets the phone number of the contact with validation.

        Parameters:
        ----------
        value : str
            The new phone number of the contact.

        Raises:
        ------
        ValueError:
            If the phone number contains non-numeric characters.
        """
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        self._phone_number = value

    @property
    def email(self) -> str:
        """
        Gets the email address of the contact.
        
        Returns:
        -------
        str:
            The contact's email address.
        """
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """
        Sets the email address of the contact with validation.

        Parameters:
        ----------
        value : str
            The new email address of the contact.

        Raises:
        ------
        ValueError:
            If the email address does not contain an "@" symbol.
        """
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value

    @property
    def address(self) -> Optional[Address]:
        """
        Gets the physical address of the contact.
        
        Returns:
        -------
        Optional[Address]:
            The contact's physical address, or None if not set.
        """
        return self._address

    @address.setter
    def address(self, value: Address) -> None:
        """
        Sets the physical address of the contact with type validation.

        Parameters:
        ----------
        value : Address
            The new address of the contact.

        Raises:
        ------
        ValueError:
            If the provided value is not of type Address.
        """
        if not isinstance(value, Address):
            raise ValueError("Address must be of type Address")
        self._address = value

    def __str__(self) -> str:
        """
        Returns a string representation of the contact suitable for display.

        Returns:
        -------
        str:
            A string that provides a human-readable summary of the contact.
        """
        contact_details = (
            f"Name: {self.first_name} {self.last_name}\n"
            f"Phone: {self.phone_number}\n"
            f"Email: {self.email}\n"
        )
        if self.address:
            contact_details += str(self.address)
        return contact_details
    
    def update_contact(self, **kwargs) -> None:
        """
        Updates the contact's attributes based on provided keyword arguments.

        Parameters:
        ----------
        **kwargs : dict
            A dictionary of attribute names and their new values.

        Example:
        --------
        update_contact(first_name="Jane", phone_number="5559876543")
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __del__(self):
        """
        Destructor method that is called when a contact is being deleted.
        Prints a message indicating which contact is being deleted.
        """
        print(f"Contact {self.first_name} {self.last_name} is being deleted")
        del(self)
