from bank_account import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, account_number, pin_number, customer_id, balance, is_premium, interest_rate):
        super().__init__(account_number, pin_number, customer_id, balance, is_premium)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def isAccepted(self, amount) -> bool:
        if amount % 10000 != 0:
            return False
        if amount < 50000:
            return False
        if not self.is_premium and amount > 5000000:
            return False
        if self.balance - amount < 50000:
            return False
        return True

    def withdraw(self, amount) -> bool:
        if self.isAccepted(amount):
            self.balance -= amount
            return True
        else:
            return False
