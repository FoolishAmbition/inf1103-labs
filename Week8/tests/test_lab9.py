import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from main import get_positive_float, main
from orders import BulkDiscount, DiscountStrategy, Order, OrderLine, PercentageDiscount, StudentDiscount
from products import CanBeShipped, DigitalProduct, Inventory, PhysicalProduct, ProductFactory
from storage import load_inventory, load_products, save_inventory


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.product = ProductFactory.create("physical", "P1", "Lamp", 50, 10)

    def test_default_and_swapped_discounts(self):
        order = Order()
        order.add_product(self.product, 5)
        self.assertEqual(order.calculate_total(), 250)
        order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230)
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225)
        order.set_discount(StudentDiscount())
        self.assertEqual(order.calculate_total(), 237.50)

    def test_bulk_threshold(self):
        discount = BulkDiscount(200, 20)
        self.assertEqual(discount.apply(199), 199)
        self.assertEqual(discount.apply(200), 180)

    def test_order_uses_an_external_strategy(self):
        class HalfPrice(DiscountStrategy):
            def apply(self, total):
                return total / 2

        strategy = HalfPrice()
        for quantity in (1, 2):
            order = Order(strategy)
            order.add_product(self.product, quantity)
            self.assertEqual(order.calculate_total(), 25 * quantity)

    def test_order_line_rejects_invalid_quantities(self):
        for quantity in (0, -1, 1.5):
            with self.subTest(quantity=quantity), self.assertRaisesRegex(ValueError, "Quantity"):
                OrderLine(self.product, quantity)


class TestProducts(unittest.TestCase):
    def test_factory_builds_both_types(self):
        physical = ProductFactory.create("physical", "P1", "Lamp", 25, 2, weight=2)
        digital = ProductFactory.create("digital", "D1", "Editor", 40, 0)
        self.assertIsInstance(physical, PhysicalProduct)
        self.assertIsInstance(physical, CanBeShipped)
        self.assertEqual(physical.calculate_shipping_cost(), 10)
        self.assertIsInstance(digital, DigitalProduct)
        self.assertNotIsInstance(digital, CanBeShipped)

    def test_unknown_type(self):
        with self.assertRaisesRegex(ValueError, "Unknown product type: service"):
            ProductFactory.create("service", "S1", "Install", 30, 5)

    def test_both_types_reject_invalid_price_and_stock(self):
        for kind in ("physical", "digital"):
            for price, stock in ((0, 5), (-1, 5), (float("nan"), 5), (25, -1), (25, 1.5)):
                with self.subTest(kind=kind, price=price, stock=stock), self.assertRaises(ValueError):
                    ProductFactory.create(kind, "P1", "Item", price, stock)

    def test_negative_stock_update_leaves_stock_unchanged(self):
        product = ProductFactory.create("digital", "D1", "Editor", 40, 3)
        self.assertFalse(product.update_stock(-1))
        self.assertEqual(product.stock, 3)
        self.assertTrue(product.update_stock(0))
        self.assertEqual(product.stock, 0)


class TestStorageAndInput(unittest.TestCase):
    def test_sample_csv_skips_bad_rows_and_imports_remaining_rows(self):
        original = Path(__file__).resolve().parents[1] / "products.csv"
        inventory = Inventory()
        output = StringIO()
        with redirect_stdout(output):
            load_products(original, inventory)
        self.assertEqual([item.product_id for item in inventory.products()], ["P001", "D001", "P003"])
        messages = output.getvalue().splitlines()
        self.assertEqual(messages[0], "Row 4 skipped: Unknown product type: service")
        self.assertTrue(messages[1].startswith("Row 5 skipped:"))
        self.assertEqual(messages[2:], ["3 products loaded.", "Load attempt finished."])
        with self.assertRaisesRegex(ValueError, "known weight"):
            inventory.search_product("P001").calculate_shipping_cost()

    def test_missing_csv_still_finishes(self):
        with TemporaryDirectory() as folder, redirect_stdout(StringIO()) as output:
            path = Path(folder) / "missing.csv"
            load_products(path, Inventory())
            self.assertEqual(output.getvalue().splitlines(), [
                f"Products file not found: {path}",
                "Load attempt finished.",
            ])

    def test_json_round_trip_keeps_product_fields(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "inventory.json"
            inventory = Inventory()
            inventory.add_product(ProductFactory.create("physical", "P1", "Lamp", 25, 2, weight=1.5))
            inventory.add_product(ProductFactory.create("digital", "D1", "Editor", 40, 0))
            save_inventory(path, inventory)
            loaded = load_inventory(path)
            self.assertEqual([p.to_dict() for p in loaded.products()],
                             [p.to_dict() for p in inventory.products()])

    def test_bad_json_survives_cli_startup(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "inventory.json"
            path.write_text("{bad json", encoding="utf-8")
            with patch("main.INVENTORY_FILE", path), redirect_stdout(StringIO()) as output:
                main()
            self.assertIn("Could not load inventory:", output.getvalue())
            self.assertEqual(path.read_text(encoding="utf-8"), "{bad json")

    def test_price_prompt_repeats_after_invalid_values(self):
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
            with redirect_stdout(StringIO()) as output:
                price = get_positive_float("Price: ")
        self.assertEqual(price, 12.50)
        self.assertEqual(output.getvalue().splitlines(), [
            "Please enter a valid number, e.g. 12.50",
            "Please enter a number greater than zero.",
        ])

    def test_cli_import_update_search_and_save(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "inventory.json"
            choices = ["7", "3", "P001", "12", "4", "P001", "6"]
            with patch("main.INVENTORY_FILE", path), patch("builtins.input", side_effect=choices):
                with redirect_stdout(StringIO()) as output:
                    main()
            self.assertIn("3 products loaded.", output.getvalue())
            self.assertIn("Stock: 12", output.getvalue())
            self.assertEqual(load_inventory(path).search_product("P001").stock, 12)


if __name__ == "__main__":
    unittest.main()
