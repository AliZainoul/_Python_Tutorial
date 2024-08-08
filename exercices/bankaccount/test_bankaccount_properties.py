from bankaccount import BankAccount
import pytest      

def test_initialization():
    """
    Test the initialization of the BankAccount class.
    
    This test verifies that a BankAccount object is properly initialized with the given account number and balance.
    """
    account = BankAccount("12345", 100.0)
    assert account.accountNumber == "12345"
    assert account.balance == 100.0

def test_getAccountNumber():
    """
    Test the accountNumber property (getter).
    
    This test checks that the account number is correctly returned by the accountNumber property.
    """
    account = BankAccount("12345", 100.0)
    assert account.accountNumber == "12345"

def test_getBalance():
    """
    Test the balance property (getter).
    
    This test verifies that the balance is correctly returned by the balance property.
    """
    account = BankAccount("12345", 100.0)
    assert account.balance == 100.0

def test_setAccountNumber():
    """
    Test the accountNumber property (setter).
    
    This test verifies that the account number can be updated using the accountNumber property setter.
    """
    account = BankAccount("12345", 100.0)
    account.accountNumber = "54321"
    assert account.accountNumber == "54321"

def test_setBalance():
    """
    Test the balance property (setter).
    
    This test checks that the balance can be updated using the balance property setter.
    """
    account = BankAccount("12345", 100.0)
    account.balance = 200.0
    assert account.balance == 200.0

def test_deposit_positive_amount():
    """
    Test the deposit method with a positive amount.
    
    This test verifies that depositing a positive amount increases the balance correctly.
    """
    account = BankAccount("12345", 100.0)
    account.deposit(50.0)
    assert account.balance == 150.0

def test_deposit_negative_amount():
    """
    Test the deposit method with a negative amount.
    
    This test verifies that depositing a negative amount raises a ValueError.
    """
    account = BankAccount("12345", 100.0)
    with pytest.raises(ValueError, match="The amount cannot be negative."):
        account.deposit(-50.0)

def test_withdraw_valid_amount():
    """
    Test the withdraw method with a valid amount.
    
    This test verifies that withdrawing a valid amount decreases the balance correctly.
    """
    account = BankAccount("12345", 100.0)
    account.withdraw(50.0)
    assert account.balance == 50.0

def test_withdraw_exceeding_amount():
    """
    Test the withdraw method with an amount exceeding the balance.
    
    This test verifies that withdrawing an amount greater than the current balance raises a ValueError.
    """
    account = BankAccount("12345", 100.0)
    with pytest.raises(ValueError, match="You're broke!"):
        account.withdraw(150.0)

if __name__ == "__main__":
    pytest.main()
