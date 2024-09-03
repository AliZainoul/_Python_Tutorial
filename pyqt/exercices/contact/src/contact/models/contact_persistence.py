from abc import ABC, abstractmethod
import pandas as pd
import os

class Persistence(ABC):
    """An abstract class that defines the interface for a persistence class."""

    @abstractmethod
    def dump(self, data):
        """Method to save data."""
        pass

    @abstractmethod
    def load(self):
        """Method to load data."""
        pass

    @abstractmethod
    def is_file_exists(self) -> bool:
        """Method to check if the persistence file exists."""
        pass


class CsvPersistence:
    """A persistence class that saves and loads data to a CSV file."""

    def __init__(self, file_name):
        self.file_name = file_name

    def dump(self, data: pd.DataFrame):
        """Saves the DataFrame to a CSV file."""
        data.to_csv(self.file_name, index=False)
    
    def load(self) -> pd.DataFrame:
        """Loads the data from the CSV file, ensuring the correct data types."""
        if not os.path.exists(self.file_name):
            # Return an empty DataFrame if the file does not exist
            return pd.DataFrame()
        dtype = {
            "Contact ID": int,
            "First Name": str,
            "Last Name": str,
            "Phone Number": str,
            "Email": str,
            "Address ID": int
        }
        return pd.read_csv(self.file_name, dtype=dtype)
    
    def is_file_exists(self) -> bool:
        """Checks if the CSV file exists."""
        return os.path.exists(self.file_name) and os.path.isfile(self.file_name)


class CsvPersistenceMock(Persistence):
    """A mock persistence class used for testing."""

    def __init__(self):
        """
        Initialize the CsvPersistenceMock with an empty DataFrame.
        """
        self.data = pd.DataFrame()

    def dump(self, data: pd.DataFrame):
        """
        Mock saving data. Stores data in memory instead of a file.

        Parameters:
        ----------
        data : pd.DataFrame
            The data to be "saved" in memory.
        """
        self.data = data

    def load(self) -> pd.DataFrame:
        """
        Mock loading data. Retrieves data from memory instead of a file.

        Returns:
        -------
        pd.DataFrame:
            The data stored in memory.
        """
        return self.data

    def is_file_exists(self) -> bool:
        """
        Mock file existence check. Always returns True.

        Returns:
        -------
        bool:
            True, as the file is assumed to always exist in this mock.
        """
        return True
