class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance):
        if account_number in self.accounts:
            return "Account already exists"
        if initial_balance < 0:
            return "Initial balance must be non-negative"
        self.accounts[account_number] = {
            "name": name,
            "balance": initial_balance
        }
        return "Account created successfully"

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account not found"
        if amount <= 0:
            return "Deposit amount must be positive"
        self.accounts[account_number]["balance"] += amount
        return "Deposit successful"

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account not found"
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self.accounts[account_number]["balance"]:
            return "Insufficient funds"
        self.accounts[account_number]["balance"] -= amount
        return "Withdrawal successful"

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            return "Account not found"
        return self.accounts[account_number]["balance"]
