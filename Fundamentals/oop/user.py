class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        pass

matt = User("Matt")
matt.make_deposit(100)
matt.make_deposit(200)
matt.make_deposit(50)
matt.make_withdrawal(75)
print(matt.account_balance)

hope = User("Hope")
hope.make_deposit(250)
hope.make_deposit(300)
hope.make_withdrawal(400)
hope.make_withdrawal(25)
print(hope.account_balance)

monique = User("Monique")
monique.make_deposit(1000)
monique.make_withdrawal(250)
monique.make_withdrawal(75)
monique.make_withdrawal(275)
print(monique.account_balance)