from tabulate import tabulate
from digital_bank import DigitalBank
from customer import Customer
from savings_account import SavingsAccount
from loan_account import LoanAccount
import os


def clear_screen():
    print("\n" * 50)


activeBank = DigitalBank('Active Bank', 'nganhangso@active.com')


def initiateData():
    customer1 = Customer('1234515', 'Nguyen Van A', '1/1/1999', True, 'Da Nang',
                         '0895124523', 'vana@gmail.com', '111111', True)
    customer2 = Customer('1234515', 'Nguyen Van B', '1/2/1999', True, 'Da Lat',
                         '0895124523', 'vanB@gmail.com', '111112', False)
    account11 = SavingsAccount('63505', '214', customer1.customer_id, 7126123.00, customer1.isPremium, 0.2)
    account12 = SavingsAccount('72452', '264', customer1.customer_id, 1235412.00, customer1.isPremium, 0.1)
    account13 = LoanAccount('36412', '612', customer1.customer_id, customer1.isPremium, 0.2)
    customer1.add_account(account11)
    customer1.add_account(account12)
    customer1.add_account(account13)
    account21 = LoanAccount('51263', '125', customer2.customer_id, customer1.isPremium, 0.1)
    customer2.add_account(account21)
    activeBank.add_customer(customer1)
    activeBank.add_customer(customer2)


def function1():
    cus_id = input("Nhap Id khach hang: ")
    if activeBank.getCustomerById(cus_id):
        print(activeBank.getCustomerById(cus_id).display_information())
    else:
        print("Can't find customer ID")


def function2():
    cus_id = input("Nhap Id khach hang: ")
    if activeBank.getCustomerById(cus_id):
        customer_info = activeBank.getCustomerById(cus_id)
    else:
        print("Can't find customer ID")
        return
    account_number = input("Enter account number (Only number and have 5 characters): ")
    while len(account_number) != 5 or customer_info.isAccountExisted(
            account_number) or not account_number.isnumeric():
        if len(account_number) != 5 or not account_number.isnumeric():
            print('Invalid input!!')
        elif customer_info.isAccountExisted(account_number):
            print('Account number is existed')
        account_number = input("Enter account number (Only number and have 5 characters): ")

    pin_number = input("Enter pin number (Only number and have 3 characters): ")
    while len(pin_number) != 3 or not pin_number.isnumeric():
        if len(pin_number) != 3 or not pin_number.isnumeric():
            print('Invalid input!!')
        pin_number = input("Enter pin number (Only number and have 3 characters): ")
    account_balance = "0"
    while account_balance.isnumeric():
        if not account_balance.isnumeric():
            print('Invalid input!!')
        account_balance = input("Enter balance (Only number): ")
    account = SavingsAccount(account_number, pin_number, customer_info.customer_id, float(account_balance),
                             customer_info.isPremium, 0.2)
    customer_info.add_account(account)
    print('Add Savings account successful')

def function3():
    cus_id = input("Nhap Id khach hang: ")
    if activeBank.getCustomerById(cus_id):
        customer_info = activeBank.getCustomerById(cus_id)
    else:
        print("Can't find customer ID")
        return
    account_number = input("Enter account number (Only number and have 5 characters): ")
    while len(account_number) != 5 or customer_info.isAccountExisted(
            account_number) or not account_number.isnumeric():
        if len(account_number) != 5 or not account_number.isnumeric():
            print('Invalid input!!')
        elif customer_info.isAccountExisted(account_number):
            print('Account number is existed')
        account_number = input("Enter account number (Only number and have 5 characters): ")
    pin_number = ""
    while len(pin_number) != 3 or not pin_number.isnumeric():
        if len(pin_number) != 3 or not pin_number.isnumeric():
            print('Invalid input!!')
        pin_number = input("Enter account number (Only number and have 3 characters): ")
    account = LoanAccount(account_number, pin_number, customer_info.customer_id, customer_info.isPremium, 0.2)
    customer_info.add_account(account)
    print('Add Loans account successful')

def function4():
    cus_id = input("Nhap Id khach hang: ")
    if activeBank.getCustomerById(cus_id):
        customer_info = activeBank.getCustomerById(cus_id)
    else:
        print("Can't find customer ID")
        return
    acc_id = input("Input account number: ")
    if customer_info.getAccountById(acc_id):
        acc_info = customer_info.getAccountById(acc_id)
    else:
        print("Can't find account number")
        return
    pin_number = input('Input pin number: ')
    if acc_info.pin_number != pin_number:
        print("Wrong pin")
        return
    amount = input("Enter withdraw amount (Only number): ")
    while not amount.isnumeric():
        amount = input("Enter withdraw amount (Only number): ")
        if not amount.isnumeric():
            print('Invalid input!!')
    amount = float(amount)
    if acc_info.withdraw(amount):
        print('Withdraw successful')
        print(acc_info.log(amount, activeBank.bank_name))
    else:
        print('Withdraw failed')

def function5():
    pass


if __name__ == "__main__":
    initiateData()
    user_input = "1"
    while user_input != "0":
        menu = [['1. Thong tin khach hang'],
                ['2. Them tai khoan ATM'],
                ['3. Them tai khoan tin dung'],
                ['4. Rut tien'],
                ['5. Lich su giao dich'],
                ['0. Thoat']]
        print(tabulate(tabular_data=menu, headers=['NGANHANGSO | minhthinh@v1.0.0'], tablefmt='psql'))
        user_input = input("Chuc nang: ")
        match user_input:
            case "1":
                function1()
            case "2":
                function2()
            case "3":
                function3()
            case "4":
                function4()
            case "5":
                function5()
            case "0":
                exit()
        input("Press \"Enter\" to return choose another function...")
        clear_screen()
