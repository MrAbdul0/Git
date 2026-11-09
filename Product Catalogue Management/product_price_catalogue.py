import json

class ProductFinder:
    def __init__(self):
        self._catalogue = {}
        self.load_catalogue() 

    def add_product(self, product_name, price):
        product_name = product_name.strip().lower()
        if product_name in self._catalogue:
            raise ValueError('Product already exists, choose another product')
        try:
            price = float(price)
        except (ValueError, TypeError):
            raise ValueError('Price must be a number')
        if price <= 0:
            raise ValueError('Price must be greater than zero')
        
        if not product_name:
            raise ValueError('Product name cannot be empty')
                
        self._catalogue[product_name] = price
        self.save_catalogue()
        return f'Product {product_name} with price {price} was added successfully'

    def save_catalogue(self):
        with open("catalogue.json", "w") as f:
            json.dump(self._catalogue, f)

    def load_catalogue(self):
        try:
            with open("catalogue.json", "r") as f:
                self._catalogue = json.load(f)
        except FileNotFoundError:
            pass

    def search_price(self, product_name):
        product_name = product_name.strip().lower()
        if not product_name:
            raise ValueError('Product name cannot be empty')
    
        if product_name not in self._catalogue:
            raise ValueError("Product not found, please choose option '1' to add product")
        price = self._catalogue[product_name] 
        return price

    def update_price(self, product_name, new_price):
        product_name = product_name.strip().lower()
        try:
            new_price = float(new_price)
        except(ValueError, TypeError):
            raise ValueError('Price must be a number')

        if new_price <= 0:
            raise ValueError('Price must be greater than zero')
        
        if not product_name:
            raise ValueError('Product name cannot be empty')
        
        if product_name not in self._catalogue:
            raise ValueError("Product not found, please choose option '1' to add product")
        self._catalogue[product_name] = new_price
        self.save_catalogue()
        return f"Price of {product_name} has been updated successfully"

    def delete_product(self, product_name):
        product_name = product_name.strip().lower()
        if not product_name:
            raise ValueError('Product name cannot be empty')
        
        if product_name not in self._catalogue:
            raise ValueError("Product not found, please choose option '1' to add product")
        del self._catalogue[product_name]
        self.save_catalogue()
        return f"Product {product_name} has been deleted successfully"
        
    def view_all_price(self):
        if not self._catalogue:
            raise ValueError('Catalogue cannot be empty')
        for product_name, product_price in sorted(self._catalogue.items(), key=lambda item: item[1], reverse=True):
            print(product_name, product_price)

    def partial_search(self, keyword):
        keyword = keyword.strip().lower()
        if not keyword:
            raise ValueError('keyword is missing')
        matches = {}
        for product_name, product_price in self._catalogue.items():
            if keyword in product_name:
                matches[product_name] = product_price
        if not matches:
            raise ValueError('keyword not found') 
        return matches

finder = ProductFinder()

while True:
    choice =input('1. Add product  2. Search price  3. Update price  4. Delete product  5. view_all_price  6. Partial search  7.Quit:')
    if choice == '1':
        try:
            product_name = input('Enter product name: ')
            product_price = input('Enter product price: ')
            print(finder.add_product(product_name, product_price))
        except ValueError as e:
            print(f'Error: {e}')

    elif choice == '2':
        try:
            product_name = input('Enter product name: ')
            print(finder.search_price(product_name))
        except ValueError as e:
            print(f'Error: {e}')

    elif choice == '3':
        try:
            product_name = input('Enter product name: ')
            product_price = input('Enter product price: ')
            print(finder.update_price(product_name, product_price))
        except ValueError as e:
            print(f'Error: {e}')

    elif choice == '4':
        try:
            product_name = input('Enter product name: ')
            print(finder.delete_product(product_name))
        except ValueError as e:
            print(f'Error: {e}')

    elif choice == '5':
        try:
            finder.view_all_price()
        except ValueError as e:
            print(f'Error: {e}')
 
    elif choice == '6':
        try:
            keyword = input('Enter keyword: ')
            print(finder.partial_search(keyword))
        except ValueError as e:
            print(f'Error: {e}')

    elif choice == '7':
        break

    else:
        print('Enter 1, 2, 3, 4, 5, 6, 7')

    