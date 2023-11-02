from user import User
from bank_account import BankAccount
from savings_account import SavingsAccount
from loan_account import LoanAccount
from tabulate import tabulate


class Customer(User):

    def __init__(self, citizen_id, full_name, date_of_birth, gender, address, phone_number, email, customer_id,
                 isPremium):
        super().__init__(citizen_id, full_name, date_of_birth, gender, address, phone_number, email)
        self.customer_id = customer_id
        self.isPremium = isPremium
        self.accounts = list()

    def get_customer_id(self):
        return self.customer_id

    def add_account(self, account):
        if isinstance(account, BankAccount):
            self.accounts.append(account)
            return True
        else:
            return False

    def total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total

    def isAccountExisted(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return True
        return False
    def display_information(self):
        premium = 'PREMIUM' if self.isPremium else ''
        data = [[self.customer_id, 'FUNIX', premium, self.total_balance()]]
        for account in self.accounts:
            account_info = []
            account_info.append(account.account_number)
            account_type = 'SAVINGS' if isinstance(account, SavingsAccount) else 'LOAN'
            account_info.append(account_type)
            account_info.append('')
            account_info.append(str(account.balance))
            data.append(account_info)
        colalign = ("right", "right", "right", "right")
        return tabulate(data, tablefmt = 'pretty', colalign = colalign)
