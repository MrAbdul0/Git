promo_codes = {
    'SAVE10': 10,
    'WELCOME20': 20,
    'PAYLESS30': 30,
    'SAVEMORE': 15
}

total = float(input('Enter the total amount of your purchase: '))
code = input('Enter a promo code:').upper()

def apply_code(total, code):
    if code in promo_codes and total >= 1500.0:
        percent = promo_codes[code]
        discount = total * percent/100
        final_price = total - discount
        return f'The result of subtracting {percent} percent discount from {total} is {final_price}.'
    else:
        return f'Discount is invalid or amount is less than 1500.00'

result = apply_code(total, code)
print(result)