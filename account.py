class Account:
    def __init__(self, name, acc_number):
        self.balance = 0
        self.transaction = 100
        self.name = name
        self.acc_number = acc_number
        self.deposits = []
        self.withdraws = []
        self.loan = 0

    def deposit (self, amount):
        if amount <= 0:
            return f"Deposit amount should be greater than zero"
        else:
            self.balance += amount
            deposits_dictionary= {
                "date":datetime.now().strftime("%x %X"),
                "amount" : amount,
                "narration" : f"You have deposited {amount}. Your balance is {self.balance}"
            }
            self.deposits.append(deposits_dictionary)
            return f"Hello {self.name}, you have deposited {amount} your balance is {self.balance}"
    def withdraw (self, amount):
        if amount+self.transaction > self.balance:
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
        for statements in self.withdraws:
            print(statements)
    def current_balance(self):
        balance = self.balance
        return f"Your current balance is {balance}"
    def full_statements(self):
        full_statements_list = self.deposits + self.withdraws
        full_statements_list.sort (key = lambda statement : statement['date'],reverse = True)
        # sorted_full_statements_list =sorted(full_statements_list)
        for statement in full_statements_list:
            if statement in self.deposits:
                print (f"{statement['date']}___Deposit___{ statement['amount']}")
        for statement in full_statements_list:
            if statement in self.withdraws:
                print (f"{statement['date']}___Withdraw___{ statement['amount']}")
    def borrow(self,amount):
        deposit_sum=0
        for a in self.deposits:
            deposit_sum+=a["amount"]
        if amount<=0:
            return "Dear customer, you can not borrow 0"
        elif len(self.deposits)<10:
            return f"You need to do at least 10 deposits to be able to access the loan service, make {10-len(self.deposits)} more deposits to qualify"
        elif amount<100:
            return "You can only borrow at least 100"
        elif self.balance!=0:
            return f"Your balance is {self.balance},you must have 0 balance to be eligible to this service"
        elif amount > deposit_sum/3:
            return f"You are not qualified to borrow this amount. You can borrow at most {deposit_sum/3}"
        elif self.loan!=0:
            return f"YOu have unpaid loan of {self.loan}, for you to borrow first clear the loan you have"
        else:
            interest=(3/100)*amount
            self.loan+= amount + interest
            return f"You have borrowed {amount} and your will pay{self.loan}"
    def loan_repayment(self,amount):
        if amount<=0:
            return "Dear customer, You can not pay 0 amount, surely?"
        if amount>self.loan:
            remainder=amount-self.loan
            self.loan=0
            return f"Your loan balance is {self.loan} { self.deposit(remainder)}"
        else:
            self.loan-=amount
            return f"You have paid a loan of {amount} KSH and your current loan balance is {self.loan}"
    def transfer(self,amount,instance_name):
        if amount<=0:
            return "invalid amount"
        elif amount>=self.balance:
            return "insufficient amount"
        else:
            self.balance-=amount
            instance_name.balance+=amount
            return f"You have transfered {amount} KSH to {instance_name} account with the name of {instance_name.account_name}. Your new balance is {self.balance}"


