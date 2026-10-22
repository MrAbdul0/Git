def list_of_leads(leads):
    for lead in leads:
        name = lead[0]
        product = lead[1]
        last_contact = lead[2]
        if last_contact <= 2:
            print(f'{name} is interested in buying {product}. Last contacted is {last_contact} days ago, we wait!')
        elif last_contact <= 5:
            print(f'{name} is interested in buying {product}. Last contacted is {last_contact} days ago, send a reminder message!')
        elif last_contact >= 6:
            print(f'{name} is interested in buying {product}. Last contacted is {last_contact} days ago, Call now!')

leads = [
    ['David', 'Shoes', 1],
    ['Sarah', 'Shirts', 4],
    ['Aisha', 'Bags', 5],
    ['Michael', 'Watches', 7]
]

while True:
    user_input = input('Do you want to add a new lead? (yes/no):')
    if user_input.lower() == 'yes':
        name = input('Enter the name of the lead:')
        product = input('Enter the product the lead is interested in:')
        last_contact = int(input('Enter the number of days since last contacted:'))
        leads.append([name, product, last_contact])
        print('Lead added successfully!')
    elif user_input.lower() == 'no':
        break
    
list_of_leads(leads)