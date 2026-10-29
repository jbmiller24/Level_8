import random
# Defining the Bank Account class and parameters
class BankAccount:
    
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00
    # Adding a deposit to account
    def deposit(self, amount):
        self.balance += amount
    # Withdrawing from account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
    # Displaying account info
    def display_info(self):
        print("Name:", self.name)
        print("Account #:", self.account_number)
        print(f"Balance: ${self.balance:.2f}")