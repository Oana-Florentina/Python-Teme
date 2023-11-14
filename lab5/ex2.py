# Design a bank account system with a base class Account and subclasses
# SavingsAccount and CheckingAccount. Implement methods for
# deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Current Balance: ${self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.01):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)
        print(f"Interest calculated and deposited: ${interest_amount}")


class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=100):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdrawal(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            print(amount, self.balance, self.overdraft_limit)
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")


savings_account = SavingsAccount(account_number=1303, holder_name="Florentina", balance=5000, interest_rate=0.02)
savings_account.display_balance()
savings_account.deposit(1000)
savings_account.calculate_interest()

checking_account = CheckingAccount(account_number=2003, holder_name="Flory", balance=2000, overdraft_limit=500)
checking_account.display_balance()
checking_account.withdrawal(2500)

