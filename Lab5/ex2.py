class Account:
    """Base class for a bank account"""

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit an amount into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw an amount from the account"""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # Default interest rate is 2%

    def calculate_interest(self):
        """Calculate and add interest to the balance"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest}. New balance: ${self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit  # Allows overdraft up to the specified limit

    def withdraw(self, amount):
        """Withdraw with overdraft support"""
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Withdrawal exceeds overdraft limit.")
        else:
            print("Withdrawal amount must be positive.")


# Example usage
savings = SavingsAccount(account_number="SA123", balance=1000, interest_rate=0.05)
checking = CheckingAccount(account_number="CA123", balance=500, overdraft_limit=200)

# Deposit and Withdrawal for Savings Account
savings.deposit(200)
savings.withdraw(150)
savings.calculate_interest()

# Deposit and Withdrawal for Checking Account
checking.deposit(300)
checking.withdraw(900)  # This will use overdraft
checking.withdraw(100)  # This should fail due to overdraft limit
