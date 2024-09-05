from dataclasses import dataclass

@dataclass
class Address:
    """
    A class to represent a physical address.

    Attributes:
    ----------
    _street : str
        The street address (e.g., "1234 Python Lane").
    _city : str
        The city where the address is located.
    _state : str
        The state or province where the address is located.
    _zipcode : str
        The postal code for the address.
    _country : str
        The country where the address is located.

    Methods:
    -------
    street() -> str:
        Gets the street address.
    street(value: str) -> None:
        Sets the street address with validation.

    city() -> str:
        Gets the city name.
    city(value: str) -> None:
        Sets the city name with validation.

    state() -> str:
        Gets the state or province name.
    state(value: str) -> None:
        Sets the state or province name with validation.

    zipcode() -> str:
        Gets the postal code.
    zipcode(value: str) -> None:
        Sets the postal code with numeric validation.

    country() -> str:
        Gets the country name.
    country(value: str) -> None:
        Sets the country name with validation.

    __str__() -> str:
        Returns a nicely formatted string representation of the full address.
    """

    _street: str
    _city: str
    _state: str
    _zipcode: str
    _country: str

    @property
    def street(self) -> str:
        """
        Gets the street address.

        Returns:
        -------
        str:
            The street address.
        """
        return self._street

    @street.setter
    def street(self, value: str) -> None:
        """
        Sets the street address with validation.

        Parameters:
        ----------
        value : str
            The new street address.

        Raises:
        ------
        ValueError:
            If the street address is empty.
        """
        if not value:
            raise ValueError("Street cannot be empty")
        self._street = value

    @property
    def city(self) -> str:
        """
        Gets the city name.

        Returns:
        -------
        str:
            The city name.
        """
        return self._city

    @city.setter
    def city(self, value: str) -> None:
        """
        Sets the city name with validation.

        Parameters:
        ----------
        value : str
            The new city name.

        Raises:
        ------
        ValueError:
            If the city name is empty.
        """
        if not value:
            raise ValueError("City cannot be empty")
        self._city = value

    @property
    def state(self) -> str:
        """
        Gets the state or province name.

        Returns:
        -------
        str:
            The state or province name.
        """
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        """
        Sets the state or province name with validation.

        Parameters:
        ----------
        value : str
            The new state or province name.

        Raises:
        ------
        ValueError:
            If the state or province name is empty.
        """
        if not value:
            raise ValueError("State cannot be empty")
        self._state = value

    @property
    def zipcode(self) -> str:
        """
        Gets the postal code.

        Returns:
        -------
        str:
            The postal code.
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, value: str) -> None:
        """
        Sets the postal code with numeric validation.

        Parameters:
        ----------
        value : str
            The new postal code.

        Raises:
        ------
        ValueError:
            If the postal code is not numeric.
        """
        if not value.isdigit():
            raise ValueError("Zipcode must be numeric")
        self._zipcode = value

    @property
    def country(self) -> str:
        """
        Gets the country name.

        Returns:
        -------
        str:
            The country name.
        """
        return self._country

    @country.setter
    def country(self, value: str) -> None:
        """
        Sets the country name with validation.

        Parameters:
        ----------
        value : str
            The new country name.

        Raises:
        ------
        ValueError:
            If the country name is empty.
        """
        if not value:
            raise ValueError("Country cannot be empty")
        self._country = value

    def __str__(self) -> str:
        """
        Returns a nicely formatted string representation of the full address.

        Returns:
        -------
        str:
            A string that provides a human-readable summary of the address.
        """
        return f"{self.street}, {self.city}, {self.state}, {self.zipcode}, {self.country}"
