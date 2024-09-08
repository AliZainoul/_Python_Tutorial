import pytest
import pandas as pd
import os
from faker import Faker
from contact.models.contact_persistence import CsvPersistence

# Define constants for file paths
FILE_PATH_CONTACTS = "src/tests/data_test/contacts.csv"
FILE_PATH_ADDRESSES = "src/tests/data_test/addresses.csv"
DIRECTORY = "src/tests/data_test"

# Fixtures
@pytest.fixture(scope="module")
def faker():
    """Fixture to provide a Faker instance."""
    return Faker()

@pytest.fixture(scope="module")
def data_test_dir():
    """Fixture to create a directory named 'data_test' inside 'contact/tests'."""
    os.makedirs(DIRECTORY, exist_ok=True)
    yield DIRECTORY

@pytest.fixture
def sample_data(faker):
    """Fixture to provide sample contact data as a DataFrame using Faker."""
    data = {
        "First Name": [faker.first_name() for _ in range(12)],
        "Last Name": [faker.last_name() for _ in range(12)],
        "Phone Number": [faker.phone_number() for _ in range(12)],
        "Email": [faker.email() for _ in range(12)],
        "Address": [str(faker.address()) for _ in range(12)]
    }
    return pd.DataFrame(data)

@pytest.fixture
def csv_persistence(data_test_dir):
    """Fixture to provide an instance of CsvPersistence with a constant file path."""
    return CsvPersistence(FILE_PATH_CONTACTS)

# Test Cases
def test_dump_and_load(csv_persistence, sample_data):
    """Test saving and loading data using CsvPersistence."""
    # Dump the sample data to CSV
    csv_persistence.dump(sample_data)

    # Load the data back from CSV
    loaded_data = csv_persistence.load()

    # Assert that the loaded data matches the original data
    pd.testing.assert_frame_equal(sample_data, loaded_data)

def test_is_file_exists(csv_persistence, sample_data):
    """Test checking file existence."""
    # Initially, the file should not exist
    if os.path.exists(FILE_PATH_CONTACTS):
        os.remove(FILE_PATH_CONTACTS)
    assert not csv_persistence.is_file_exists()

    # Dump the sample data to create the file
    csv_persistence.dump(sample_data)

    # Now, the file should exist
    assert csv_persistence.is_file_exists()

def test_load_non_existent_file(csv_persistence):
    """Test loading data from a non-existent file."""
    # Ensure the file does not exist
    if os.path.exists(FILE_PATH_CONTACTS):
        os.remove(FILE_PATH_CONTACTS)

    # Load data from the non-existent file
    loaded_data = csv_persistence.load()

    # Assert that the loaded data is an empty DataFrame
    assert loaded_data.empty