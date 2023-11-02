from bank import Bank


class DigitalBank(Bank):

    def __init__(self, bank_name, website):
        super().__init__(bank_name)
        self.website = website
