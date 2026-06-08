class BankAccount:
    def __init__(self,account_number,owner_name,balance,date_opened):

        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance
        self.date_opened=date_opened
        self.closed=False

    def deposit(self,amount):
        if self.closed:
            print("Account closed.  It Cannot deposit.")
            return

        self.balance+=amount
        print(f"Deposited {amount} - New balance: {self.balance}")

    def withdraw(self, amount):
        if self.closed:
            print("Account is closed.It Cannot withdraw.")
            return

        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount} - New balance: {self.balance}")
        else:
            print("NO funds.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def display_info(self):
        print("----- Account Information -----")
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")
        print(f"Closed: {self.closed}")

    def close_account(self):
        self.closed = True
        print(f"Account {self.account_number} has been closed.")


account1 = BankAccount("2021", "Maggie", 7000, "2026-08-15")
account2 = BankAccount("2022", "Brian", 4000, "2026-07-24")

account1.display_info()
account1.deposit(3000)
account1.withdraw(4000)
account1.check_balance()
account1.close_account()


account2.display_info()
account2.deposit(800)
account2.withdraw(1500)
account2.check_balance()
account2.close_account()