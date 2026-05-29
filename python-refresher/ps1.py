class BankAccount:
    def __init__(self, balance: int | float, name: str, account_number: int):
        self.balance = balance
        if balance < 0:
            balance = 0
        self.name = name
        self.account_number = account_number

    def isNumber(self, var):
        """
        Checks if a variable is a number if they are instances of int or float
        @ret a boolean, if the variable is a number
        """
        isInt = isinstance(var, int)
        isFloat = isinstance(var, float)

        return isInt or isFloat

    def withdraw(self, amount: int | float):
        """
        Withdraws money from the account
        Money must be a number and not exceed the account balance or go below zero
        @ret an integer, -1 if the action failed and the new account balance otherwise
        """
        if (not self.isNumber(amount)) or (amount > self.balance or amount < 0):
            print("Invalid amount!")
            return -1

        self.balance -= amount
        return self.balance

    def deposit(self, amount: int | float):
        """
        Deposits money into the account
        Money must be a number and be positive
        @ret an integer, -1 if the action failed and the new account balance otherwise
        """
        if (not self.isNumber(amount)) or (amount < 0):
            print("Invalid amount!")
            return -1

        self.balance += amount
        return self.balance

    def print_balance(self):
        """
        Prints account information
        """
        print("Name: " + self.name)
        print("Balance: " + "$" + self.balance + " dollars")
        print("Account ID: " + self.account_number)
