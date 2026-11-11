import unittest
from io import StringIO
from contextlib import redirect_stdout

from main import PhysicalProduct, DigitalProduct


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


if __name__ == "__main__":
    unittest.main()
