from BankAccount import BankAccount

# Creates the function for a deposit
def make_deposit(account):
    try:
        amount = float(input("How much would you like to deposit? "))

        if amount > 0:
            account.deposit(amount)
            print("Deposit successful!")
        else:
            print("Please enter a positive amount.")

    except ValueError:
        print("Invalid amount. Please enter a number.")

# Creates the function for a withdrawl
def make_withdrawal(account):
    amount = float(input("How much would you like to withdraw? "))

    if amount <= 0:
        print("Please enter a positive amount.")
    elif account.withdraw(amount):
        print("Withdrawal successful!")
    else:
        print("Insufficient funds.")

# Creates the function for displaying account info
def view_account_information(account):
    account.display_info()
# Introduction
print("Welcome to Miller Bank!")
name = input("Please enter your name: ")

account = BankAccount(name)

choice = ""
# Gives options to choose from until they want to quit
while choice != "4":
    print("\nPlease choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")

    choice = input("Enter your choice: ")
    # Shows the actions that will happen once they input a number
    if choice == "1":
        make_deposit(account)
    elif choice == "2":
        make_withdrawal(account)
    elif choice == "3":
        view_account_information(account)
    elif choice == "4":
        print("Thank you for your business!")
    else:
        print("Invalid choice. Please try again.")