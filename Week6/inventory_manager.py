import json
import os

INVENTORY_FILE = "inventory.json"


def load_inventory():
    """Load inventory from JSON file if it exists, otherwise return empty list."""
    if os.path.exists(INVENTORY_FILE):
        try:
            with open(INVENTORY_FILE, "r") as file:
                inventory = json.load(file)
            print("inventory.json found. \nInventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, IOError):
            print("Error reading inventory.json. Starting with empty inventory.")
            return []
    else:
        print("No inventory file found. Starting with an empty inventory.")
        return []


def save_inventory(inventory):
    """Save inventory to JSON file."""
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully to inventory.json.")


def display_all(inventory):
    """Display all products in inventory."""
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\nCurrent Inventory\n")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | "
              f"Price: ${item['price']:.2f} | Stock: {item['stock']}")


def add_product(inventory):
    """Add a new product to inventory."""
    product_id = input("Product ID: ").strip()

    # Check for duplicate ID
    if any(item["id"] == product_id for item in inventory):
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

    new_item = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(new_item)
    print("\nProduct added successfully!")


def update_stock(inventory):
    """Update stock quantity for an existing product."""
    product_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"] == product_id:
            print(f"\nProduct Found:\nName: {item['name']}")
            print(f"Current Stock: {item['stock']}")

            try:
                new_stock = int(input("\nNew Stock Quantity: "))
            except ValueError:
                print("Error: Invalid stock value.")
                return

            if new_stock < 0:
                print("Error: Stock cannot be negative.")
                return

            item["stock"] = new_stock
            print("\nStock updated successfully!")
            return

    print("Product not found.")


def search_product(inventory):
    """Search for a product by ID."""
    product_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"] == product_id:
            print("\nProduct Found\n")
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Stock: {item['stock']}")
            return

    print("Product not found.")


def print_menu():
    """Display the main menu."""
    print("\nMENU")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")


def main():
    print("# INVENTORY MANAGEMENT SYSTEM\n")
    inventory = load_inventory()

    while True:
        print_menu()
        option = input("\nEnter option: ").strip()

        if option == "1":
            display_all(inventory)
        elif option == "2":
            print("\nAdd New Product")
            add_product(inventory)
        elif option == "3":
            print("\nUpdate Stock")
            update_stock(inventory)
        elif option == "4":
            print("\nSearch Product")
            search_product(inventory)
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