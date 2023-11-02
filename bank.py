from customer import Customer

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []  # Initialize an empty list to store customers

    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)
            return True
        else:
            return False
