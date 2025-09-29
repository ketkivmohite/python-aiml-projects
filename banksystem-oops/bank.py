class BankAccount :
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")

        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):
        if 0< amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance is {self.balance}.")

        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account Number : {self.account_number}")
        print(f"Account holder : {self.account_holder}")
        print(f"Balance: {self.balance}")

account = BankAccount("12345", "Ketki Mohite", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()
