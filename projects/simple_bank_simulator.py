bank_name = 'Abdul-haqq Chonoko Sani'
bank_balance = 950000

def withdraw():
    while True:
        global bank_balance
        withdrawal_amount = int(input('Enter the amount you want to withdraw:'))
        if withdrawal_amount <= bank_balance:
            bank_balance = bank_balance - withdrawal_amount
            print(f"Dear {bank_name} your account has been debited with ${withdrawal_amount}, your new balance is {bank_balance}")
            break
        elif withdrawal_amount > bank_balance:
            print(f"Withdrawal of ${withdrawal_amount} was declined due to insufficient funds. ")
             
        else:
            print('Enter withdrawal amount:')
            
def credit() :
    while True:
        global bank_balance
        add_money = input('Do you want to add money? (yes/no):').lower()
        if add_money == 'yes':
            credit_amount = int(input('Enter amount you want to add:'))
            bank_balance = bank_balance + credit_amount
            print(f"Dear {bank_name} your account has been credited with ${credit_amount}, your new balance is {bank_balance}")
        elif add_money == 'no':
            break 
        else:
            print('Enter amount!')

def check_balance():
    print(f'Available balance is {bank_balance}.')

withdraw()
credit()
check_balance()









    
