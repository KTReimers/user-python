# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, nameInput):
        self.name= nameInput
        self.amount = 0
    
    def make_deposit(self, numAmount):
        self.amount += numAmount
        return self

    def make_withdrawl(self, numAmount):
        self.amount -= numAmount
        return self
    
    def display_User_Balance(self):
        print(f"User name: {self.name}, Balance: ${self.amount}")

    def transfer_money(self,other_user, numAmount):
        self.amount -= numAmount
        other_user.amount += numAmount
        return (self)

user1 = User("Guido van Rossum")
# print(user1.name)
# user1.display_User_Balance()
user2 = User("Steve Goodman")
user3 = User("Billy Jones")

# user1.make_deposit(50).make_deposit(100).make_deposit(25).make_withdrawl(50).display_User_Balance()
# user2.make_deposit(50).make_deposit(50).make_withdrawl(25).make_withdrawl(25).display_User_Balance()
# user3.make_deposit(100).make_withdrawl(25).make_withdrawl(25).make_withdrawl(25).display_User_Balance()

user1.transfer_money(user3, 50).display_User_Balance()
