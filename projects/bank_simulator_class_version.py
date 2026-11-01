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

user_1 = BankActivity('Abdulhaqq Sani Chonoko', 5000000)
user_1.run_menu()
    