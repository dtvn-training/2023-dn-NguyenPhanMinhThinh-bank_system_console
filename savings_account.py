from datetime import datetime

from tabulate import tabulate

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

    def log(self, amount, bank_name):
        transaction_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        atm_id = bank_name
        acc_number = self.account_number
        current_balance = self.balance
        fee = 0
        data = [['BIEN LAI GIAO DICH SAVINGS'],
                ['NGAY G/D', transaction_time],
                ['ATM ID:', atm_id],
                ['SO TK:', acc_number],
                ['SO TIEN:', (str(amount) + 'd')],
                ['SO DU:', (str(current_balance) + 'd')],
                ['PHI + VAT', (str(fee) + 'd')]
                ]

        colalign = ('left', 'right')
        return tabulate(data, tablefmt='pretty', colalign=colalign)
