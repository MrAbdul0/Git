product_price_lists = {
    'ps5': 1200,
    'laptop': 750,
    'phone': 490,
    'earpud': 120,
    'powerbank': 30,
    'headphone': 59
}

def check_product_price(products):
    while True:
        product_name = input("Enter the name of the product(or 'q' to quit ):").strip().lower()
        if product_name == 'q':
            break

        if product_name in products:
            price = products[product_name]
            print(f"The price of {product_name} is ${price} ")
        else:
            print("Item not available")

check_product_price(product_price_lists)

while True:
    user_input = input('Do you want to add a new product (y/n):').lower()
    if user_input == 'y':
        new_product = input('Enter the name of the new product here:').lower()
        new_price = int(input('Enter the price of new product:'))
        product_price_lists.update({new_product: new_price})
        print(f"{new_product} costs ${new_price} is added Successfully!.")
    elif user_input == 'n':
        break
    else:
        print("Please type y or n")
        break


