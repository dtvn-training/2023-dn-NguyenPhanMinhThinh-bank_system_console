import random
from datetime import datetime


class Transaction():
    def __init__(self, account_number, amount, status):
        random.seed(124213)
        self.id = random.randint(100000, 999999)
        self.account_number = account_number
        self.amount = amount
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.status = status

