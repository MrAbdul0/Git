import re
from datetime import datetime

class BankActivity:
    def __init__(self, bank_name, account_balance):
        self.bank_name = bank_name
        self.account_balance = account_balance

    def withdraw(self, withdraw_amount): 
        if withdraw_amount <= 0:
            return 'Amount must be greater than zero'

        if withdraw_amount > self.account_balance:
            return 'Withdrawal declined due to insufficient balance'   
                   
        if withdraw_amount <= self.account_balance:
            self.account_balance -= withdraw_amount
            return f'Withdrawal of {withdraw_amount} has been initiated, new balance is {self.account_balance}'

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            return 'Amount must be greater than zero'
        self.account_balance += deposit_amount
        return  f'Deposit of {deposit_amount} was successful, new balance is {self.account_balance}'

    def run_menu(self):
        while True:
            choice = input('1. Withdraw  2. Deposit  3. Check_balance  4. Quit:')
            if choice == '1':
                try:
                    withdraw = int(input('Enter withdrawal amount:'))
                except ValueError:
                    print('Enter a number')
                    continue
                print(self.withdraw(withdraw))
            elif choice == '2':
                try:
                    deposit= int(input('Enter deposit amount:'))
                except ValueError:
                    print('Enter a number')
                    continue
                print(self.deposit(deposit))
            elif choice == '3':
                print(f'{self.bank_name} your available balance is: {self.account_balance}')
            elif choice == '4':
                break
            else:
                print('Enter choice 1, 2, 3, 4')


class User:
    def __init__(self, first_name, last_name, username, email, phone_number, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.account = BankActivity('My Bank', 0)

class Bank:
    def __init__(self):
        self._users = {}

    def register(self, first_name, last_name, username, email, phone_number, date_of_birth):
        user = User(first_name, last_name, username, email, phone_number, date_of_birth)
        if user.username in self._users:
            raise ValueError('Username already exist')
        if any(u.email == user.email for u in self._users.values()):
            raise ValueError('Email already exist')
        self._users[username] = user
        return user

    def login(self, username):
        return self._users.get(username.strip().lower())

    def __str__(self):
        return f"{self.first_name} {self.last_name} (@{self.username})"

    def start(self):
        while True:
            choice = input('1. Register  2. Login  3. Quit:')
            if choice == '1':
                try:
                    user = self.register(
                        input('first name:'),
                        input('last name:'),
                        input('username:'),
                        input('email:'),
                        input('phone_number:'),
                        input('date_of_birth (YYYY-MM-DD):')
                    )
                    print(f'Registered {user.first_name}: you can now login')
                except ValueError as e:
                    print(f'Error: {e}')

            elif choice == '2':
                user = self.login(input('Enter username:'))
                if user is None:
                    print('User not found. please register first')
                    continue
                print(f'welcome: {user.first_name}')
                user.account.run_menu()

            elif choice == '3':
                break

bank = Bank()
bank.start()





            

   


    