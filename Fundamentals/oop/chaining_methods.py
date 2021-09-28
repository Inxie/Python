class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
        return self


matt = User("Matt")
matt.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(75).display_user_balance()

hope = User("Hope")
hope.make_deposit(250).make_deposit(300).make_withdrawal(400).make_withdrawal(25).display_user_balance()

monique = User("Monique")
monique.make_deposit(1000).make_withdrawal(250).make_withdrawal(75).make_withdrawal(275).display_user_balance()