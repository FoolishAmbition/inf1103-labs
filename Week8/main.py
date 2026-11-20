from math import isfinite
from pathlib import Path

from products import Inventory, ProductFactory
from storage import load_inventory, load_products, save_inventory

LAB_FOLDER = Path(__file__).resolve().parent
INVENTORY_FILE = LAB_FOLDER / "inventory.json"
PRODUCTS_FILE = LAB_FOLDER / "products.csv"


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")
            continue
        if not isfinite(value) or value <= 0:
            print("Please enter a number greater than zero.")
            continue
        return value


def menu_add_product(inventory: Inventory) -> None:
    print("1. Physical Product")
    print("2. Digital Product")
    choice = input("Enter product type: ").strip()
    if choice not in ("1", "2"):
        print("Error: Invalid product type.")
        return

    product_id = input("Product ID: ").strip()
    if inventory.search_product(product_id) is not None:
        print(f"Error: Product ID '{product_id}' already exists.")
        return

    name = input("Product Name: ").strip()
    price = get_positive_float("Price: ")
    try:
        stock = int(input("Stock Quantity: "))
        if choice == "1":
            weight = get_positive_float("Weight (kg): ")
            product = ProductFactory.create("physical", product_id, name, price, stock, weight=weight)
        else:
            size = get_positive_float("Download Size (MB): ")
            product = ProductFactory.create("digital", product_id, name, price, stock, download_size=size)
    except ValueError as error:
        print(f"Could not add product: {error}")
        return

    inventory.add_product(product)
    print("Product added successfully.")


def menu_update_stock(inventory: Inventory) -> None:
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return

    print(f"{product.name} | Current Stock: {product.stock}")
    try:
        stock = int(input("New Stock Quantity: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if product.update_stock(stock):
        print("Stock updated successfully.")
    else:
        print("Stock cannot be negative.")


def menu_search_product(inventory: Inventory) -> None:
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
    else:
        product.display_information()


def main() -> None:
    print("Inventory Management System")
    try:
        inventory = load_inventory(INVENTORY_FILE)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Could not load inventory: {error}")
        return

    while True:
        print("\n1. Display all\n2. Add product\n3. Update stock\n4. Search")
        print("5. Save inventory\n6. Exit\n7. Import products.csv")
        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()
        elif option == "2":
            menu_add_product(inventory)
        elif option == "3":
            menu_update_stock(inventory)
        elif option == "4":
            menu_search_product(inventory)
        elif option in ("5", "6"):
            try:
                save_inventory(INVENTORY_FILE, inventory)
            except OSError as error:
                print(f"Could not save inventory: {error}")
                continue
            print("Inventory saved.")
            if option == "6":
                break
        elif option == "7":
            load_products(PRODUCTS_FILE, inventory)
        else:
            print("Invalid option. Please enter 1-7.")


if __name__ == "__main__":
    main()
