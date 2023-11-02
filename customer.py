from user import User
from bank_account import BankAccount


class Customer(User):

    def __init__(self, citizen_id, full_name, date_of_birth, gender, address, phone_number, email, customer_id):
        super().__init__(citizen_id, full_name, date_of_birth, gender, address, phone_number, email)
        self.customer_id = customer_id
        self.account_list = list()

    def get_customer_id(self):
        return self.customer_id

    def add_account(self, account):
        if isinstance(account, BankAccount):
            self.account_list.append(account)
            return True
        else:
            return False
