import json
import os
import tempfile
from unittest.mock import patch

import unittest
from io import StringIO
from contextlib import redirect_stdout

if __package__:
    from . import main
else:
    import main

Product = main.Product
Inventory = main.Inventory
PhysicalProduct = main.PhysicalProduct
DigitalProduct = main.DigitalProduct
CanBeShipped = main.CanBeShipped

class TestProductOverriding(unittest.TestCase):

    def test_physical_product_display(self):
        product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5)

        output = StringIO()

        with redirect_stdout(output):
            product.display_information()

        result = output.getvalue()

        self.assertIn("P001", result)
        self.assertIn("Laptop", result)
        self.assertIn("1200.00", result)
        self.assertIn("Stock: 5", result)
        self.assertIn("Weight: 2.5 kg", result)

    def test_digital_product_display(self):
        product = DigitalProduct("D001", "Antivirus", 49.90, 20, 500)

        output = StringIO()

        with redirect_stdout(output):
            product.display_information()

        result = output.getvalue()

        self.assertIn("D001", result)
        self.assertIn("Antivirus", result)
        self.assertIn("49.90", result)
        self.assertIn("Stock: 20", result)
        self.assertIn("Download Size: 500 MB", result)
    
    def test_physical_fulfilment(self):
        product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5)

        result = product.get_fulfilment_info()

        self.assertEqual(
            result,
            "This product requires physical shipping."
        )

    def test_digital_fulfilment(self):
        product = DigitalProduct("D001", "Antivirus", 49.90, 20, 500)

        result = product.get_fulfilment_info()

        self.assertEqual(
            result,
            "This product is delivered digitally."
        )

    def test_product_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Product("P002", "Generic", 10, 5)
    
    def test_physical_shipping_cost(self):
        product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5)

        self.assertEqual(product.calculate_shipping_cost(), 12.50)

    def test_shipping_cost_different_weight(self):
        product = PhysicalProduct("P002", "Monitor", 300, 3, 5.0)

        self.assertEqual(product.calculate_shipping_cost(), 25.00)

    def test_digital_product_has_no_shipping(self):
        product = DigitalProduct("D001", "Antivirus", 49.90, 20, 500)

        self.assertFalse(hasattr(product, "calculate_shipping_cost"))
    
    def test_interface_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            CanBeShipped()

class TestInventoryIntegration(unittest.TestCase):

    def test_add_both_product_types(self):
        inventory = Inventory()

        physical = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5)
        digital = DigitalProduct("D001", "Antivirus", 49.90, 20, 500)

        inventory.add_product(physical)
        inventory.add_product(digital)

        self.assertEqual(len(inventory._products), 2)
        self.assertIsInstance(inventory.search_product("P001"), PhysicalProduct)
        self.assertIsInstance(inventory.search_product("D001"), DigitalProduct)

    def test_physical_json_data(self):
        product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5)

        data = product.to_dict()

        self.assertEqual(data["type"], "physical")
        self.assertEqual(data["weight"], 2.5)
        self.assertEqual(data["stock"], 5)

    def test_digital_json_data(self):
        product = DigitalProduct("D001", "Antivirus", 49.90, 20, 500)

        data = product.to_dict()

        self.assertEqual(data["type"], "digital")
        self.assertEqual(data["download_size"], 500)
        self.assertEqual(data["price"], 49.90)

    def test_save_and_load_inventory(self):
        with tempfile.TemporaryDirectory() as folder:
            test_file = os.path.join(folder, "inventory.json")

            with patch.object(main, "INVENTORY_FILE", test_file):
                inventory = Inventory()

                inventory.add_product(
                    PhysicalProduct("P001", "Laptop", 1200, 5, 2.5)
                )
                inventory.add_product(
                    DigitalProduct("D001", "Antivirus", 49.90, 20, 500)
                )

                main.save_inventory(inventory)

                with open(test_file, "r") as file:
                    saved_data = json.load(file)

                self.assertEqual(len(saved_data), 2)

                loaded = main.load_inventory()

                physical = loaded.search_product("P001")
                digital = loaded.search_product("D001")

                self.assertIsInstance(physical, PhysicalProduct)
                self.assertIsInstance(digital, DigitalProduct)
                self.assertEqual(physical._weight, 2.5)
                self.assertEqual(digital._download_size, 500)

    def test_legacy_json_rejected_safely(self):
        with tempfile.TemporaryDirectory() as folder:
            test_file = os.path.join(folder, "inventory.json")

            legacy_data = [
                {"id": "1", "name": "6", "price": 231.0, "stock": 1}
            ]

            with open(test_file, "w") as file:
                json.dump(legacy_data, file)

            with patch.object(main, "INVENTORY_FILE", test_file):
                with self.assertRaises(ValueError):
                    main.load_inventory()

            with open(test_file, "r") as file:
                self.assertEqual(json.load(file), legacy_data)
    
    def test_physical_product_implements_shipping_interface(self):
        self.assertTrue(issubclass(PhysicalProduct, CanBeShipped))
        self.assertFalse(issubclass(DigitalProduct, CanBeShipped))

if __name__ == "__main__":
    unittest.main()
