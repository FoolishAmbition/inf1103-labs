import unittest
from io import StringIO
from contextlib import redirect_stdout

from main import Product, PhysicalProduct, DigitalProduct, CanBeShipped


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

if __name__ == "__main__":
    unittest.main()
