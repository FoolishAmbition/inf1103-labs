import json
import os
from abc import ABC, abstractmethod
from typing import NotRequired, TypedDict

INVENTORY_FILE = "inventory.json"
UNKNOWN_SUPPLIER_ID = "UNKNOWN"


class SupplierRecord(TypedDict):
    supplier_id: str
    name: str
    contact_email: str


class ProductRecord(TypedDict):
    id: str
    name: str
    price: float
    stock: int
    supplier: SupplierRecord
    type: NotRequired[str]
    weight: NotRequired[float]
    download_size: NotRequired[float]


class Supplier:
    def __init__(self, supplier_id: str, name: str,
                 contact_email: str) -> None:
        if not isinstance(supplier_id, str) or not supplier_id.strip():
            raise ValueError("Supplier ID must be a nonempty string.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Supplier name must be a nonempty string.")
        if not isinstance(contact_email, str):
            raise ValueError("Supplier email must be a string.")
        if supplier_id == UNKNOWN_SUPPLIER_ID and (
                name != "Unknown supplier" or contact_email != ""):
            raise ValueError("Supplier ID UNKNOWN is reserved for missing details.")
        self.supplier_id: str = supplier_id
        self.name: str = name
        self.contact_email: str = contact_email

    def display_information(self) -> None:
        email = self.contact_email or "Not provided"
        print(f"Supplier: {self.supplier_id} | Name: {self.name} | Email: {email}")

    def to_dict(self) -> SupplierRecord:
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "contact_email": self.contact_email
        }


# =============================================================
# PRODUCT CLASS
# =============================================================
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock
        self.supplier: Supplier = supplier

    def update_stock(self, quantity):
        if quantity >= 0:
            self._stock = quantity
            return True
        return False

    def display_information(self):
        print(f"ID: {self._product_id} | Name: {self._name} | Price: ${self._price:.2f} | Stock: {self._stock}")
        self.supplier.display_information()

    def to_dict(self) -> ProductRecord:
        return {
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
            "supplier": self.supplier.to_dict()
        }
    
    @abstractmethod
    def get_fulfilment_info(self):
        pass

# =============================================================
# CAN BE SHIPPED INTERFACE
# =============================================================
class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass

# =============================================================
# PHYSICAL PRODUCT CLASS
# =============================================================
class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self._weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."
    
    def calculate_shipping_cost(self):
        return self._weight * 5.00
    
    def to_dict(self) -> ProductRecord:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self._weight
        return data

# Registering the entire PhysicalProduct class as a virtual subclass of CanBeShipped
CanBeShipped.register(PhysicalProduct)

# =============================================================
# DIGITAL PRODUCT CLASS
# =============================================================
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self._download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size} MB")
    
    def get_fulfilment_info(self):
        return "This product is delivered digitally."
    
    def to_dict(self) -> ProductRecord:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self._download_size
        return data

# =============================================================
# INVENTORY CLASS
# =============================================================
class Inventory:
    def __init__(self) -> None:
        self._products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        if self.find_product(product._product_id) is not None:
            print(f"Error: Product ID '{product._product_id}' already exists.")
            return False

        self._products.append(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        for product in self._products:
            if product._product_id == product_id:
                return product
        return None

    def search_product(self, product_id: str) -> Product | None:
        # Preserve the existing API while keeping one lookup implementation.
        return self.find_product(product_id)

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)

        if product is None:
            return False

        self._products.remove(product)
        return True

    def display_all(self) -> None:
        if not self._products:
            print("\nInventory is empty.")
            return

        print("\nCurrent Inventory\n")
        for product in self._products:
            product.display_information()

# =============================================================
# FILE HANDLING
# =============================================================
def load_inventory():
    inventory = Inventory()
    suppliers: dict[str, Supplier] = {}

    if os.path.exists(INVENTORY_FILE):
        try:
            with open(INVENTORY_FILE, "r") as file:
                data = json.load(file)

            for item in data:
                product_type = item.get("type")
                # Old typed records have no supplier details; do not invent them.
                supplier_data = item.get("supplier", {
                    "supplier_id": UNKNOWN_SUPPLIER_ID,
                    "name": "Unknown supplier",
                    "contact_email": ""
                })
                if not isinstance(supplier_data, dict):
                    raise ValueError("Supplier data must be an object.")
                candidate = Supplier(
                    supplier_data["supplier_id"], supplier_data["name"],
                    supplier_data["contact_email"]
                )
                supplier = suppliers.get(candidate.supplier_id)
                if supplier is None:
                    supplier = candidate
                    suppliers[supplier.supplier_id] = supplier
                elif supplier.to_dict() != candidate.to_dict():
                    raise ValueError(
                        f"Conflicting details for supplier {candidate.supplier_id}"
                    )

                if product_type == "physical":
                    product = PhysicalProduct(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["weight"],
                        supplier
                    )

                elif product_type == "digital":
                    product = DigitalProduct(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["download_size"],
                        supplier
                    )

                else:
                    raise ValueError(
                        f"Unknown or missing product type "
                        f"for product {item.get('id', 'unknown')}"
                    )

                inventory.add_product(product)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, OSError, KeyError,
                TypeError, ValueError) as error:
            print(f"Error loading inventory: {error}")
            print("Inventory file was not changed.")
            raise

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
    print("\nSelect Product Type")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Enter product type: ").strip()

    if product_type not in ("1", "2"):
        print("Error: Invalid product type.")
        return

    product_id = input("Product ID: ").strip()

    if inventory.search_product(product_id) is not None:
        print(f"Error: Product ID '{product_id}' already exists.")
        return

    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Error: Price and stock must be non-negative.")
            return

        if product_type == "1":
            weight = float(input("Weight (kg): "))

            if weight <= 0:
                print("Error: Weight must be positive.")
                return

        else:
            download_size = float(input("Download Size (MB): "))

            if download_size <= 0:
                print("Error: Download size must be positive.")
                return

    except ValueError:
        print("Error: Invalid numeric input.")
        return

    supplier_id = input("Supplier ID (existing ID to reuse): ").strip()
    if supplier_id == UNKNOWN_SUPPLIER_ID:
        print("Error: Supplier ID UNKNOWN is reserved for missing details.")
        return

    supplier = None
    for product in inventory._products:
        if product.supplier.supplier_id == supplier_id:
            supplier = product.supplier
            break

    if supplier is None:
        supplier_name = input("Supplier Name: ").strip()
        contact_email = input("Supplier Email (blank if unavailable): ").strip()
        try:
            supplier = Supplier(supplier_id, supplier_name, contact_email)
        except ValueError as error:
            print(f"Error: {error}")
            return
    else:
        print(f"Reusing supplier: {supplier.name}")

    if product_type == "1":
        new_product = PhysicalProduct(
            product_id, name, price, stock, weight, supplier
        )
    else:
        new_product = DigitalProduct(
            product_id, name, price, stock, download_size, supplier
        )

    if inventory.add_product(new_product):
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
