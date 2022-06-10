class Account:
    def __init__(self, name, acc_number):
        self.balance = 0
        self.transaction = 100
        self.name = name
        self.acc_number = acc_number
        self.deposits = []
        self.withdraws = []
    def deposit (self, amount):
        if amount <= 0:
            return f"Deposit amount should be greater than zero"
        else:
            self.balance += amount
            self.deposits.append(f"Hello {self.name}, you have deposited {amount}")
            return f"Hello {self.name}, you have deposited {amount} your balance is {self.balance}"
    def withdraw (self, amount):
        if amount > self.balance:
            return f"Your balance is {self.balance}, you cannot withdraw {amount}"
        elif amount <= 0:
            return f"Amount must be greater than zero"
        else:
            self.balance -= amount + self.transaction
            self.withdraws.append(f"You have withdrawn {amount}")
            return f"You have withdrawn {amount}, your new balance is{self.balance}"
    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for staments in self.withdraws:
            print(staments)
    def current_balance(self):
        balance = self.balance
        print(balance)


