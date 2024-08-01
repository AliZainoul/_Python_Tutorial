class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance 
        
    def validate_amount(self, amount):
        if not isinstance(amount, float):
            raise TypeError("Amount must be a float")
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        
    def deposit(self, amount):
        self.validate_amount(amount)
        self.balance += amount
        
    def withdraw(self, amount):
        self.validate_amount(amount)
        if self.balance < amount:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount

    def perform_operation(self, operation:str, amount:float) -> None:
        try:
            getattr(self,operation)(amount)
            print(f"Opération réussie. Nouveau solde: {self.balance}")
        except (TypeError, InvalidAmountError, InsufficientFundsError) as e:
            print(f"Erreur: {e}")

# Création d'un objet BankAccount
big_account = BankAccount(15684945, 2000.0)

# Essai de dépôt et de retrait avec gestion des exceptions centralisée
big_account.perform_operation("deposit", 1500.00)
big_account.perform_operation("deposit", -1500.00) # Cette ligne lève une exception
big_account.perform_operation("deposit", '15666.00')  # Cette ligne lève une exception
big_account.perform_operation("withdraw", '300.00')  # Cette ligne lève une exception
big_account.perform_operation("withdraw", 6000.00)  # Cette ligne lève une exception
