class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0 :
            raise ValueError("You can't deposit negative amount")
        self.balance += amount
        print(f"your balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= 0 :
            raise ValueError("You can't withdraw negative amount")
        if self.balance - amount < 0:
            raise ValueError ("You dont have enough money")
        self.balance -= amount
        print(f"your bank balance is {self.balance}")


    def display(self):
        print(f" the account number is : {self.account_number}, your bank balance is {self.balance} DOLLARS")
        
bankaccount1 = BankAccount(12345, 200)

bankaccount1.display()

bankaccount1.deposit(2000)
bankaccount1.display()

bankaccount1.withdraw(200)
bankaccount1.display()

# This line will generate an exception : ValueError ("You can't deposit negative amount")
# bankaccount1.deposit(-1)

# This line will generate an exception : ValueError ("You can't withdraw negative amount")
# bankaccount1.withdraw(-1)

# This line will generate an exception : ValueError ("You dont have enough money")
# bankaccount1.withdraw(2001)