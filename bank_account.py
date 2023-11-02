from withdraw import Withdraw
class BankAccount(Withdraw):
    def __init__(self, account_number, pin_number, customer_id, balance, is_premium):
        self.account_number = account_number
        self.pin_number = pin_number
        self.balance = balance
        self.customer_id = customer_id
        self.is_premium = is_premium

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def isAccepted(self, amount) -> bool:
        pass

    def withdraw(self, amount) -> bool:
        pass


