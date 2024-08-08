class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
    -----------
    accountNumber : str
        The account number associated with the bank account.
    balance : float
        The current balance of the bank account.

    Methods:
    --------
    getAccountNumber() -> str:
        Returns the account number of the bank account.
        
    getBalance() -> float:
        Returns the current balance of the bank account.
        
    setAccountNumber(accountNumber: str) -> None:
        Sets a new account number for the bank account.
        
    setBalance(balance: float) -> None:
        Sets a new balance for the bank account.
        
    deposit(amount: float) -> None:
        Deposits a specified amount into the bank account.
        
    withdraw(amount: float) -> None:
        Withdraws a specified amount from the bank account.
    """

    def __init__(self, accountNumber: str, balance: float):
        """
        Constructs all the necessary attributes for the bank account object.

        Parameters:
        -----------
        accountNumber : str
            The account number associated with the bank account.
        balance : float
            The initial balance of the bank account.
        """
        self.__accountNumber: str = accountNumber
        self.__balance: float = balance

    def getAccountNumber(self) -> str:
        """
        Returns the account number of the bank account.

        Returns:
        --------
        str: The account number of the bank account.
        """
        return self.__accountNumber
    
    def getBalance(self) -> float:
        """
        Returns the current balance of the bank account.

        Returns:
        --------
        float: The current balance of the bank account.
        """
        return self.__balance
    
    def setAccountNumber(self, accountNumber: str) -> None:
        """
        Sets a new account number for the bank account.

        Parameters:
        -----------
        accountNumber : str
            The new account number to set.
        """
        self.__accountNumber = accountNumber
    
    def setBalance(self, balance: float) -> None:
        """
        Sets a new balance for the bank account.

        Parameters:
        -----------
        balance : float
            The new balance to set.
        """
        self.__balance = balance
    
    def deposit(self, amount: float) -> None:
        """
        Deposits a specified amount into the bank account.

        Parameters:
        -----------
        amount : float
            The amount to deposit into the account.

        Raises:
        -------
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("The amount cannot be negative.")
        else:
            self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws a specified amount from the bank account.

        Parameters:
        -----------
        amount : float
            The amount to withdraw from the account.

        Raises:
        -------
        ValueError: If the withdrawal amount exceeds the current balance.
        """
        if self.__balance - amount < 0:
            raise ValueError("You're broke!")
        else:
            self.__balance -= amount    
