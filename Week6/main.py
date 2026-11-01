class Product:
    def __init__(self, product_id, name, price, stock):
        # Use an underscore (_) to indicate these are "private" (Encapsulation)
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    # Add methods to manage its own state (Page 3)
    def update_stock(self, quantity):
        if quantity >= 0:
            self._stock = quantity
            return True
        return False

    def display_information(self):
        # We use :.2f to format the price to 2 decimal places
        print(f"ID: {self._product_id} | Name: {self._name} | Price: ${self._price:.2f} | Stock: {self._stock}")
        
    # Helper method to convert the object to a dictionary for JSON saving
    def to_dict(self):
        return {
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }

class Inventory:
    def __init__(self):
        self.products = [] # This list will hold Product objects

    def add_product(self, product):
        # Check for duplicates before adding
        if self.search_product(product._product_id):
            print(f"Error: Product ID '{product._product_id}' already exists.")
            return False
        self.products.append(product)
        return True

    def search_product(self, product_id):
        for product in self.products:
            if product._product_id == product_id:
                return product
        return None

    def display_all(self):
        if not self.products:
            print("\nInventory is empty.")
            return
        
        print("\nCurrent Inventory\n")
        for product in self.products:
            product.display_information()