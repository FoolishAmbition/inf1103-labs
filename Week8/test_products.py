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
Supplier = main.Supplier

class TestProductOverriding(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Test supplier", "test@example.com")

    def test_physical_product_display(self):
        product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, self.supplier)

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
        product = DigitalProduct("D001", "Antivirus", 49.90, 20, 500, self.supplier)

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
        product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, self.supplier)

        result = product.get_fulfilment_info()

        self.assertEqual(
            result,
            "This product requires physical shipping."
        )

    def test_digital_fulfilment(self):
        product = DigitalProduct("D001", "Antivirus", 49.90, 20, 500, self.supplier)

        result = product.get_fulfilment_info()

        self.assertEqual(
            result,
            "This product is delivered digitally."
        )

    def test_product_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Product("P002", "Generic", 10, 5, self.supplier)
    
    def test_physical_shipping_cost(self):
        product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, self.supplier)

        self.assertEqual(product.calculate_shipping_cost(), 12.50)

    def test_shipping_cost_different_weight(self):
        product = PhysicalProduct("P002", "Monitor", 300, 3, 5.0, self.supplier)

        self.assertEqual(product.calculate_shipping_cost(), 25.00)

    def test_digital_product_has_no_shipping(self):
        product = DigitalProduct("D001", "Antivirus", 49.90, 20, 500, self.supplier)

        self.assertFalse(hasattr(product, "calculate_shipping_cost"))
    
    def test_interface_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            CanBeShipped()

class TestInventoryIntegration(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Test supplier", "test@example.com")

    def test_add_both_product_types(self):
        inventory = Inventory()

        physical = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, self.supplier)
        digital = DigitalProduct("D001", "Antivirus", 49.90, 20, 500, self.supplier)

        inventory.add_product(physical)
        inventory.add_product(digital)

        self.assertEqual(len(inventory._products), 2)
        self.assertIsInstance(inventory.search_product("P001"), PhysicalProduct)
        self.assertIsInstance(inventory.search_product("D001"), DigitalProduct)

    def test_physical_json_data(self):
        product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, self.supplier)

        data = product.to_dict()

        self.assertEqual(data["type"], "physical")
        self.assertEqual(data["weight"], 2.5)
        self.assertEqual(data["stock"], 5)

    def test_digital_json_data(self):
        product = DigitalProduct("D001", "Antivirus", 49.90, 20, 500, self.supplier)

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
                    PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, self.supplier)
                )
                inventory.add_product(
                    DigitalProduct("D001", "Antivirus", 49.90, 20, 500, self.supplier)
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
                with patch("sys.stdout", new_callable=StringIO):
                    with self.assertRaises(ValueError):
                        main.load_inventory()

            with open(test_file, "r") as file:
                self.assertEqual(json.load(file), legacy_data)
    
    def test_physical_product_implements_shipping_interface(self):
        self.assertTrue(issubclass(PhysicalProduct, CanBeShipped))
        self.assertFalse(issubclass(DigitalProduct, CanBeShipped))

    def test_update_stock(self):
        product = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, self.supplier)

        self.assertTrue(product.update_stock(10))
        self.assertEqual(product._stock, 10)
        self.assertFalse(product.update_stock(-5))
        self.assertEqual(product._stock, 10)

class TestSupplierAssociation(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "Test supplier", "test@example.com")
        self.physical = PhysicalProduct("P001", "Laptop", 1200, 5, 2.5, self.supplier)
        self.digital = DigitalProduct("D001", "Antivirus", 49.90, 20, 500, self.supplier)
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.test_file = os.path.join(self.folder.name, "inventory.json")
        self.file_patch = patch.object(main, "INVENTORY_FILE", self.test_file)
        self.file_patch.start()
        self.addCleanup(self.file_patch.stop)

    def write_records(self, records):
        with open(self.test_file, "w") as file:
            json.dump(records, file)

    def read_file(self):
        with open(self.test_file, "r") as file:
            return file.read()

    def test_both_products_retain_supplied_object(self):
        self.assertIs(self.physical.supplier, self.supplier)
        self.assertIs(self.digital.supplier, self.supplier)
        self.assertIsNot(self.physical, self.supplier)
        self.assertIsNot(self.digital, self.supplier)

    def test_supplier_display_through_both_products(self):
        for product in (self.physical, self.digital):
            with self.subTest(product=type(product).__name__):
                output = StringIO()
                with redirect_stdout(output):
                    product.display_information()
                self.assertIn("Supplier: S001", output.getvalue())
                self.assertIn("Test supplier", output.getvalue())
                self.assertIn("test@example.com", output.getvalue())

    def test_supplier_validates_required_details(self):
        for details in (("", "Name", ""), ("S1", " ", ""),
                        (None, "Name", ""), ("S1", "Name", None),
                        ("UNKNOWN", "Real company", "")):
            with self.subTest(details=details), self.assertRaises(ValueError):
                Supplier(*details)

    def test_blank_email_is_displayed_as_unavailable(self):
        supplier = Supplier("S002", "No contact", "")
        output = StringIO()
        with redirect_stdout(output):
            supplier.display_information()
        self.assertIn("Email: Not provided", output.getvalue())

    def test_round_trip_preserves_details_and_shared_identity(self):
        inventory = Inventory()
        inventory.add_product(self.physical)
        inventory.add_product(self.digital)
        main.save_inventory(inventory)
        saved = json.loads(self.read_file())
        self.assertEqual(saved[0]["supplier"], self.supplier.to_dict())
        loaded = main.load_inventory()
        physical = loaded.search_product("P001")
        digital = loaded.search_product("D001")
        self.assertEqual(physical.supplier.to_dict(), self.supplier.to_dict())
        self.assertIs(physical.supplier, digital.supplier)
        self.assertIsInstance(physical, PhysicalProduct)
        self.assertIsInstance(digital, DigitalProduct)

    def test_typed_week7_records_migrate_only_on_save(self):
        records = [self.physical.to_dict(), self.digital.to_dict()]
        for record in records:
            record.pop("supplier")
        self.write_records(records)
        before = self.read_file()
        inventory = main.load_inventory()
        self.assertEqual(self.read_file(), before)
        supplier = inventory.search_product("P001").supplier
        self.assertEqual(supplier.to_dict(), {
            "supplier_id": "UNKNOWN", "name": "Unknown supplier", "contact_email": ""
        })
        self.assertIs(supplier, inventory.search_product("D001").supplier)
        main.save_inventory(inventory)
        loaded = main.load_inventory()
        self.assertEqual(loaded.search_product("P001").supplier.to_dict(), supplier.to_dict())

    def test_malformed_supplier_records_rejected_without_write(self):
        for supplier_data in (None, "S001", {},
                              {"supplier_id": "S001", "name": "Test", "contact_email": 7}):
            with self.subTest(supplier_data=supplier_data):
                record = self.physical.to_dict()
                record["supplier"] = supplier_data
                self.write_records([record])
                before = self.read_file()
                with redirect_stdout(StringIO()), self.assertRaises((ValueError, KeyError)):
                    main.load_inventory()
                self.assertEqual(self.read_file(), before)

    def test_conflicting_supplier_details_rejected_without_write(self):
        records = [self.physical.to_dict(), self.digital.to_dict()]
        records[1]["supplier"]["name"] = "Different company"
        self.write_records(records)
        before = self.read_file()
        with redirect_stdout(StringIO()), self.assertRaisesRegex(ValueError, "Conflicting"):
            main.load_inventory()
        self.assertEqual(self.read_file(), before)

    def test_missing_file_starts_empty(self):
        with redirect_stdout(StringIO()):
            inventory = main.load_inventory()
        self.assertEqual(inventory._products, [])
        self.assertFalse(os.path.exists(self.test_file))

    def test_cli_creates_supplier_then_reuses_it_for_other_subtype(self):
        inventory = Inventory()
        with patch("builtins.input", side_effect=[
                "1", "P001", "Laptop", "1200", "5", "2.5",
                "S001", "Test supplier", "test@example.com"
        ]), redirect_stdout(StringIO()):
            main.menu_add_product(inventory)
        with patch("builtins.input", side_effect=[
                "2", "D001", "Antivirus", "49.90", "20", "500", "S001"
        ]), redirect_stdout(StringIO()):
            main.menu_add_product(inventory)
        physical = inventory.search_product("P001")
        digital = inventory.search_product("D001")
        self.assertIsInstance(physical, PhysicalProduct)
        self.assertIsInstance(digital, DigitalProduct)
        self.assertIs(physical.supplier, digital.supplier)
        self.assertEqual(physical.supplier.to_dict(), self.supplier.to_dict())

    def test_cli_rejects_reserved_or_invalid_supplier(self):
        for details in (["UNKNOWN"], ["S002", "", ""], ["", "Test", ""]):
            with self.subTest(details=details):
                inventory = Inventory()
                with patch("builtins.input", side_effect=[
                        "1", "P001", "Laptop", "1200", "5", "2.5", *details
                ]), redirect_stdout(StringIO()):
                    main.menu_add_product(inventory)
                self.assertIsNone(inventory.search_product("P001"))

    def test_cli_validation_still_precedes_supplier_prompts(self):
        inventory = Inventory()
        inventory.add_product(self.physical)
        cases = [
            ["9"], ["1", "P001"],
            ["1", "P002", "Test", "bad"],
            ["1", "P002", "Test", "-1", "2"],
            ["1", "P002", "Test", "1", "-2"],
            ["1", "P002", "Test", "1", "2", "0"],
            ["2", "D002", "Test", "1", "2", "0"]
        ]
        for answers in cases:
            with self.subTest(answers=answers):
                with patch("builtins.input", side_effect=answers), redirect_stdout(StringIO()):
                    main.menu_add_product(inventory)
                self.assertEqual(len(inventory._products), 1)

    def test_main_cli_save_search_update_and_exit(self):
        self.write_records([self.physical.to_dict(), self.digital.to_dict()])
        output = StringIO()
        with patch("builtins.input", side_effect=[
                "1", "4", "D001", "3", "D001", "25", "5", "6"
        ]), redirect_stdout(output):
            main.main()
        saved = json.loads(self.read_file())
        self.assertEqual(saved[1]["stock"], 25)
        self.assertEqual(saved[1]["supplier"], self.supplier.to_dict())
        self.assertIn("Stock updated successfully", output.getvalue())
        self.assertIn("Supplier: S001", output.getvalue())
        self.assertIn("Program terminated", output.getvalue())

class TestInventoryAggregation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )
        self.product = PhysicalProduct(
            "P001", "Laptop", 1200, 5, 2.5, self.supplier
        )
        self.inventory_a = Inventory()
        self.inventory_b = Inventory()

    def test_find_existing_product(self):
        self.inventory_a.add_product(self.product)

        result = self.inventory_a.find_product("P001")

        self.assertIs(result, self.product)

    def test_find_missing_product(self):
        result = self.inventory_a.find_product("P999")

        self.assertIsNone(result)

    def test_remove_existing_product(self):
        self.inventory_a.add_product(self.product)

        result = self.inventory_a.remove_product("P001")

        self.assertTrue(result)
        self.assertIsNone(self.inventory_a.find_product("P001"))

    def test_remove_missing_product(self):
        result = self.inventory_a.remove_product("P999")

        self.assertFalse(result)

    @unittest.skip("PF-2 deferred until the student's prediction is recorded")
    def test_transfer_between_inventories(self):
        self.inventory_a.add_product(self.product)
        self.inventory_a.remove_product("P001")
        self.inventory_b.add_product(self.product)

        self.assertIsNone(self.inventory_a.find_product("P001"))
        self.assertIs(
            self.inventory_b.find_product("P001"),
            self.product
        )

    def test_duplicate_product_rejected(self):
        self.assertTrue(self.inventory_a.add_product(self.product))
        self.assertFalse(self.inventory_a.add_product(self.product))
        self.assertEqual(len(self.inventory_a._products), 1)

    def test_distinct_object_with_duplicate_id_rejected(self):
        self.inventory_a.add_product(self.product)
        duplicate = DigitalProduct("P001", "Different product", 10, 2, 50, self.supplier)
        with redirect_stdout(StringIO()):
            self.assertFalse(self.inventory_a.add_product(duplicate))
        self.assertEqual(len(self.inventory_a._products), 1)
        self.assertIs(self.inventory_a.find_product("P001"), self.product)

    def test_search_delegates_to_find(self):
        with patch.object(self.inventory_a, "find_product", return_value=self.product) as lookup:
            self.assertIs(self.inventory_a.search_product("P001"), self.product)
        lookup.assert_called_once_with("P001")

    def test_remove_each_subtype_preserves_other_collection_entry(self):
        digital = DigitalProduct("D001", "Antivirus", 49.90, 20, 500, self.supplier)
        for target_id, remaining in (("P001", digital), ("D001", self.product)):
            with self.subTest(target_id=target_id):
                inventory = Inventory()
                inventory.add_product(self.product)
                inventory.add_product(digital)
                self.assertTrue(inventory.remove_product(target_id))
                self.assertIsNone(inventory.find_product(target_id))
                self.assertIsNone(inventory.search_product(target_id))
                self.assertEqual(inventory._products, [remaining])
                self.assertFalse(inventory.remove_product(target_id))

    def test_missing_removal_preserves_nonempty_collection(self):
        self.inventory_a.add_product(self.product)
        self.assertFalse(self.inventory_a.remove_product("missing"))
        self.assertEqual(self.inventory_a._products, [self.product])

    def test_empty_display_after_removing_last_entry(self):
        self.inventory_a.add_product(self.product)
        self.inventory_a.remove_product("P001")
        output = StringIO()
        with redirect_stdout(output):
            self.inventory_a.display_all()
        self.assertIn("Inventory is empty", output.getvalue())

if __name__ == "__main__":
    unittest.main()
