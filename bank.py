class Bank:
    def __init__(self, account, name, balance, bankname):
        self.name = name
        self.account = account
        self.balance = balance
        self.bankname = bankname
    def deposit(self,amount):
        self.amount = amount
        self.balance += amount
        return f"Hello {self.name}, you have deposited {self.amount} your balance is {self.balance}"
    def withdraw(self,amount):
        self.amount = amount
        self.balance -= amount
        return f"Hello {self.name}, you have withdrawn {self.amount} your balance is {self.balance}"