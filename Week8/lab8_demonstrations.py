"""Recorded Lab 8 demonstrations; predictions are in Lab8_Predict_First_Notes.md."""

from main import DigitalProduct, Inventory, Order, PhysicalProduct, Supplier


def demonstrate_association() -> None:
    print("PF1 Supplier association")
    supplier = Supplier("S001", "Demo Supplier", "demo@example.com")
    physical = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, supplier)
    digital = DigitalProduct("D001", "Antivirus", 49.90, 20, 500, supplier)
    del supplier
    physical.supplier.display_information()
    digital.supplier.display_information()
    print("Both products reference the same supplier:", physical.supplier is digital.supplier)


def demonstrate_aggregation() -> None:
    print("\nPF2 Inventory aggregation")
    supplier = Supplier("S001", "Demo Supplier", "demo@example.com")
    product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, supplier)
    inventory_a = Inventory()
    inventory_b = Inventory()
    inventory_a.add_product(product)
    print("Removed from A:", inventory_a.remove_product("P001"))
    print("Product stock update after removal:", product.update_stock(8))
    product.display_information()
    inventory_b.add_product(product)
    print("A lookup is None:", inventory_a.find_product("P001") is None)
    print("B contains the original object:", inventory_b.find_product("P001") is product)


def demonstrate_composition() -> None:
    print("\nPF3 Order composition")
    supplier = Supplier("S001", "Demo Supplier", "demo@example.com")
    product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, supplier)
    first = Order("O001")
    second = Order("O002")
    first.add_order_line(product, 1)
    second.add_order_line(product, 2)
    print("One Product:", first._order_lines[0].product is second._order_lines[0].product is product)
    print("Distinct OrderLines:", first._order_lines[0] is not second._order_lines[0])
    print("First order total:", first.calculate_total())
    print("Second order total:", second.calculate_total())
    print("First order line removed:", first.remove_order_line(0))
    print("Second order total after first-line removal:", second.calculate_total())


def demonstrate_polymorphism() -> None:
    print("\nPF4 Mixed product polymorphism")
    supplier = Supplier("S001", "Demo Supplier", "demo@example.com")
    inventory = Inventory()
    inventory.add_product(PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, supplier))
    inventory.add_product(DigitalProduct("D001", "Antivirus", 49.90, 20, 500, supplier))
    for product in inventory._products:
        product.display_information()
        print(product.get_fulfilment_info())


if __name__ == "__main__":
    demonstrate_association()
    demonstrate_aggregation()
    demonstrate_composition()
    demonstrate_polymorphism()
