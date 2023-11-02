from customer import Customer

class DigitalCustomer(Customer):
    def __init__(self, citizen_id, full_name, date_of_birth, gender, address, phone_number, email, customer_id,
                 username, password):
        super().__init__(citizen_id, full_name, date_of_birth, gender, address, phone_number, email, customer_id)
        self.username = username
        self.password = password


