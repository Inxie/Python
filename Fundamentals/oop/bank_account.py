class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0.03
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if balance - amount < 0:
            return False
        else:
            return True

patrick = BankAccount("Patrick", 0)
patrick.deposit(100).deposit(500).deposit(175).withdraw(25).yield_interest().display_account_info()

leslie = BankAccount("Leslie", 0)
leslie.deposit(1000).deposit(500).withdraw(150).withdraw(25).withdraw(50).withdraw(250).yield_interest().display_account_info()