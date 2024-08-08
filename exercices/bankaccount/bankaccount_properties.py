class BankAccount_:
    """
    A class to represent a bank account using properties for account number and balance.

    Attributes:
    -----------
    accountNumber : str
        The account number associated with the bank account.
    balance : float
        The current balance of the bank account.

    Methods:
    --------
    accountNumber (property):
        Gets or sets the account number of the bank account.
        
    balance (property):
        Gets or sets the current balance of the bank account.
        
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

    @property
    def accountNumber(self) -> str:
        """
        Gets the account number of the bank account.

        Returns:
        --------
        str: The account number of the bank account.
        """
        return self.__accountNumber
    
    @accountNumber.setter
    def accountNumber(self, accountNumber: str) -> None:
        """
        Sets a new account number for the bank account.

        Parameters:
        -----------
        accountNumber : str
            The new account number to set.
        """
        self.__accountNumber = accountNumber

    @property
    def balance(self) -> float:
        """
        Gets the current balance of the bank account.

        Returns:
        --------
        float: The current balance of the bank account.
        """
        return self.__balance
    
    @balance.setter
    def balance(self, balance: float) -> None:
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
        self.__balance -= amount
