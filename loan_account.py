from bank_account import BankAccount


class LoanAccount(BankAccount):

    def __int__(self, account_number, pin_number, customer_id, interest_rate, is_premium):
        super().__int__(account_number, pin_number, customer_id, 100000000, is_premium)
        self.interest_rate = interest_rate

    def calc_interest(self):
        self.balance += self.balance * self.interest_rate

    def getFee(self, amount):
        if self.is_premium:
            return amount * 0.01
        else:
            return amount * 0.05

    def isAccepted(self, amount) -> bool:
        if amount > 100000000:
            return False
        if self.balance - (amount + self.getFee(amount)) < 50000:
            return False

    def withdraw(self, amount) -> bool:
        if self.isAccepted(amount):
            self.balance - (amount + self.getFee(amount))
            return True
        else:
            return False
