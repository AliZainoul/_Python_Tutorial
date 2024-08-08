from bankaccount import BankAccount
import pytest

def test_initialization():
    """
    Test the initialization of a BankAccount object.

    This test checks if the BankAccount object is correctly initialized with
    the provided account number and balance.
    """
    account = BankAccount("12345", 100.0)
    assert account.getAccountNumber() == "12345"
    assert account.getBalance() == 100.0

def test_getAccountNumber():
    """
    Test the getAccountNumber method.

    This test verifies that the getAccountNumber method returns the correct
    account number of the BankAccount object.
    """
    account = BankAccount("12345", 100.0)
    assert account.getAccountNumber() == "12345"

def test_getBalance():
    """
    Test the getBalance method.

    This test checks if the getBalance method returns the correct balance
    of the BankAccount object.
    """
    account = BankAccount("12345", 100.0)
    assert account.getBalance() == 100.0

def test_setAccountNumber():
    """
    Test the setAccountNumber method.

    This test verifies that the setAccountNumber method correctly updates
    the account number of the BankAccount object.
    """
    account = BankAccount("12345", 100.0)
    account.setAccountNumber("54321")
    assert account.getAccountNumber() == "54321"

def test_setBalance():
    """
    Test the setBalance method.

    This test checks if the setBalance method correctly updates the balance
    of the BankAccount object.
    """
    account = BankAccount("12345", 100.0)
    account.setBalance(200.0)
    assert account.getBalance() == 200.0

def test_deposit_positive_amount():
    """
    Test the deposit method with a positive amount.

    This test checks if the deposit method correctly adds the specified
    positive amount to the balance of the BankAccount object.
    """
    account = BankAccount("12345", 100.0)
    account.deposit(50.0)
    assert account.getBalance() == 150.0

def test_deposit_negative_amount():
    """
    Test the deposit method with a negative amount.

    This test checks if the deposit method raises a ValueError when attempting
    to deposit a negative amount.
    """
    account = BankAccount("12345", 100.0)
    with pytest.raises(ValueError, match="The amount cannot be negative."):
        account.deposit(-50.0)

def test_withdraw_valid_amount():
    """
    Test the withdraw method with a valid amount.

    This test checks if the withdraw method correctly subtracts the specified
    amount from the balance of the BankAccount object.
    """
    account = BankAccount("12345", 100.0)
    account.withdraw(50.0)
    assert account.getBalance() == 50.0

def test_withdraw_exceeding_amount():
    """
    Test the withdraw method with an amount exceeding the balance.

    This test checks if the withdraw method raises a ValueError when attempting
    to withdraw an amount greater than the available balance.
    """
    account = BankAccount("12345", 100.0)
    with pytest.raises(ValueError, match="You're broke!"):
        account.withdraw(150.0)

if __name__ == "__main__":
    pytest.main()
