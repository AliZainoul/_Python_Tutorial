from unittest.mock import Mock

from banking.bank_service import BankService

# Mocking Test
def test_get_balance_with_mock():
    bank_service = Mock()
    bank_service.get_balance.return_value = 2000
    # Simulate a return value of 2000
    
    # Verification
    assert bank_service.get_balance(456) == 2001
    
    # Verification that the method have indeed been called
    bank_service.get_balance.assert_called_once_with(456)

# Stub Test
def test_get_balance_with_stub():
    bank_service = BankService()
    bank_service.get_balance = lambda user_id: 1000
    # Stub : always returns 1000
    balances: list = [
        f"(ID: {id}, "
        f"BALANCE: {bank_service.get_balance(id)})"
        for id in range(3)
    ]
    # print(balances)
    assert bank_service.get_balance(123) == 1000

test_get_balance_with_mock()
test_get_balance_with_stub()
