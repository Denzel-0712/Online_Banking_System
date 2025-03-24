class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    
    def check_balance(self):
        print(f"Account Balance for {self.name}: ${self.balance:.2f}")

class OnlineBankingSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, name, initial_deposit=0.0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, name, initial_deposit)
            print(f"Account created for {name} with initial balance: ${initial_deposit:.2f}")
    
    def login(self, account_number):
        return self.accounts.get(account_number, None)
    
# Example usage:
bank = OnlineBankingSystem()
bank.create_account("12345", "John Doe", 1000)
account = bank.login("12345")
if account:
    account.deposit(500)
    account.withdraw(300)
    account.check_balance()
