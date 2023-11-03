from tabulate import tabulate

from withdraw import Withdraw
from report import Report
from transaction import Transaction


class BankAccount(Withdraw, Report):
    def __init__(self, account_number, pin_number, customer_id, balance, is_premium):
        self.account_number = account_number
        self.pin_number = pin_number
        self.balance = balance
        self.customer_id = customer_id
        self.is_premium = is_premium
        self.transactions = list()

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def isAccepted(self, amount) -> bool:
        pass

    def withdraw(self, amount) -> bool:
        pass

    def log(self, amount, bank_name):
        pass

    def displayTransactions(self):
        data = [['Ma GD', 'Account number', 'amount', 'Time', 'Status']]
        if len(self.transactions) == 0:
            return "No transaction records"
        for transaction in self.transactions:
            data.append([transaction.id, self.account_number, transaction.amount, transaction.time, transaction.status])

        colalign = ("left", "left", "left", "left", "left")
        return tabulate(data, headers='firstrow', tablefmt='pretty', colalign=colalign)