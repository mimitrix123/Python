"""Week 3 Assignment 1: Bank Account class."""


class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def display_balance(self):
        print(f"{self.account_holder}'s balance: ₹{self.balance:.2f}")


def main():
    account = BankAccount("Student", 5000)
    account.display_balance()
    account.deposit(1500)
    account.withdraw(1000)
    account.display_balance()


if __name__ == "__main__":
    main()
