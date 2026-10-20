def withdraw(balance, amount):
    if amount <= 0:
        return f'Amount has to be an integer greater than 0'
    elif amount > balance:
        short = amount - balance
        return f"Withdrawal is denied. You are short by ${short}."
    elif amount == balance:
        return f'Withdrawal is approved and the account is now empty.'
    else:
        new_balance = balance - amount
        message = f'Approved and new balance is ${new_balance}.'
        if new_balance < 1000:
            message = message + '\nLow balance warning!'
        return message

print(withdraw(500, -100))
print(withdraw(500, 600))
print(withdraw(500, 500))
print(withdraw(5000, 1000))
print(withdraw(1000, 500)) 