from datetime import datetime
from tabulate import tabulate
from bank_account import BankAccount
from transaction import Transaction


class LoanAccount(BankAccount):
    def __init__(self, account_number, pin_number, customer_id, is_premium, interest_rate):
        super().__init__(account_number, pin_number, customer_id, balance=100000000, is_premium=is_premium)
        self.interest_rate = interest_rate

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
        return True

    def withdraw(self, amount) -> bool:
        if self.isAccepted(amount):
            self.balance -= (amount + self.getFee(amount))
            transaction = Transaction(self.account_number, amount, 'True')
            self.transactions.append(transaction)
            return True
        else:
            transaction = Transaction(self.account_number, amount, 'False')
            self.transactions.append(transaction)
            return False

    def log(self, amount, bank_name):
        transaction_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        atm_id = bank_name
        acc_number = self.account_number
        current_balance = self.balance
        fee = self.getFee(amount)
        data = [
                    ['BIEN LAI GIAO DICH LOAN'],
                    ['NGAY G/D', transaction_time],
                    ['ATM ID:', atm_id],
                    ['SO TK:', acc_number],
                    ['SO TIEN:', amount],
                    ['SO DU:', current_balance],
                    ['PHI + VAT', fee]
                ]

        colalign = ('left', 'right')
        return tabulate(data, tablefmt='pretty', colalign=colalign)

