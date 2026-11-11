import json
import os
from abc import ABC, abstractmethod

INVENTORY_FILE = "inventory.json"


# =============================================================
# PRODUCT CLASS
# =============================================================
class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, quantity):
        if quantity >= 0:
            self._stock = quantity
            return True
        return False

    def display_information(self):
        print(f"ID: {self._product_id} | Name: {self._name} | Price: ${self._price:.2f} | Stock: {self._stock}")

    def to_dict(self):
        return {
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }
    
    @abstractmethod
    def get_fulfilment_info(self):
        pass

# =============================================================
# PHYSICAL PRODUCT CLASS
# =============================================================
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self._weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

# =============================================================
# DIGITAL PRODUCT CLASS
# =============================================================
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size} MB")
    
    def get_fulfilment_info(self):
        return "This product is delivered digitally."

# =============================================================
# INVENTORY CLASS
# =============================================================
class Inventory:
    def __init__(self):
        self._products = []          # ⬅️ fixed

    def add_product(self, product):
        if self.search_product(product._product_id):
            print(f"Error: Product ID '{product._product_id}' already exists.")
            return False
        self._products.append(product)  # ⬅️ fixed
        return True

    def search_product(self, product_id):
        for product in self._products:  # ⬅️ fixed
            if product._product_id == product_id:
                return product
        return None

    def display_all(self):
        if not self._products:           # ⬅️ fixed
            print("\nInventory is empty.")
            return
        print("\nCurrent Inventory\n")
        for product in self._products:   # ⬅️ fixed
            product.display_information()


# =============================================================
# FILE HANDLING
# =============================================================
def load_inventory():
    inventory = Inventory()
    if os.path.exists(INVENTORY_FILE):
        try:
            with open(INVENTORY_FILE, "r") as file:
                data = json.load(file)
            for item in data:
                product = Product(item["id"], item["name"], item["price"], item["stock"])
                inventory.add_product(product)
            print("inventory.json found.\nInventory loaded successfully.")
        except (json.JSONDecodeError, IOError):
            print("Error reading inventory.json. Starting with empty inventory.")
    else:
        print("No inventory file found. Starting with an empty inventory.")
    return inventory


def save_inventory(inventory):
    data_to_save = [product.to_dict() for product in inventory._products]
    with open(INVENTORY_FILE, "w") as file:
        json.dump(data_to_save, file, indent=4)
    print("Inventory saved successfully to inventory.json.")


# =============================================================
# MENU HANDLERS
# =============================================================
def menu_add_product(inventory):
    product_id = input("Product ID: ").strip()

    if inventory.search_product(product_id) is not None:
        print(f"Error: Product ID '{product_id}' already exists.")
        return

    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Error: Invalid price or stock value.")
        return

    if price < 0 or stock < 0:
        print("Error: Price and stock must be non-negative.")
        return

    new_product = Product(product_id, name, price, stock)
    inventory.add_product(new_product)
    print("\nProduct added successfully!")


def menu_update_stock(inventory):
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product:
        print(f"\nProduct Found:\nName: {product._name}")
        print(f"Current Stock: {product._stock}")
        try:
            new_stock = int(input("\nNew Stock Quantity: "))
        except ValueError:
            print("Error: Invalid stock value.")
            return

        if product.update_stock(new_stock):
            print("\nStock updated successfully!")
        else:
            print("Error: Stock cannot be negative.")
    else:
        print("Product not found.")


def menu_search_product(inventory):
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product:
        print("\nProduct Found\n")
        product.display_information()
    else:
        print("Product not found.")


def print_menu():
    print("\nMENU")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")


# =============================================================
# MAIN PROGRAM
# =============================================================
def main():
    print("# INVENTORY MANAGEMENT SYSTEM (OOP VERSION)\n")
    inventory = load_inventory()

    while True:
        print_menu()
        option = input("\nEnter option: ").strip()

        if option == "1":
            inventory.display_all()
        elif option == "2":
            print("\nAdd New Product")
            menu_add_product(inventory)
        elif option == "3":
            print("\nUpdate Stock")
            menu_update_stock(inventory)
        elif option == "4":
            print("\nSearch Product")
            menu_search_product(inventory)
        elif option == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System. Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()