from abc import ABC, abstractmethod
from math import isfinite


class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        if not isfinite(price) or price <= 0:
            raise ValueError("Price must be greater than zero.")
        if type(stock) is not int or stock < 0:
            raise ValueError("Stock must be a non-negative integer.")

        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def stock(self) -> int:
        return self._stock

    def update_stock(self, quantity: int) -> bool:
        if type(quantity) is int and quantity >= 0:
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

class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        if weight is not None and (not isfinite(weight) or weight <= 0):
            raise ValueError("Weight must be greater than zero.")
        self._weight = weight

    def display_information(self):
        super().display_information()
        if self._weight is None:
            print("Weight: unknown")
        else:
            print(f"Weight: {self._weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        if self._weight is None:
            raise ValueError("Shipping cost requires a known weight.")
        return self._weight * 5.00

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self._weight
        return data

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        if download_size is not None and (not isfinite(download_size) or download_size <= 0):
            raise ValueError("Download size must be greater than zero.")
        self._download_size = download_size

    def display_information(self):
        super().display_information()
        if self._download_size is None:
            print("Download Size: unknown")
        else:
            print(f"Download Size: {self._download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self._download_size
        return data

class Inventory:
    def __init__(self):
        self._products = []

    def add_product(self, product: Product) -> bool:
        if self.search_product(product.product_id):
            return False
        self._products.append(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        for product in self._products:
            if product.product_id == product_id:
                return product
        return None

    def products(self) -> tuple[Product, ...]:
        return tuple(self._products)

    def display_all(self):
        if not self._products:
            print("\nInventory is empty.")
            return
        print("\nCurrent Inventory\n")
        for product in self._products:
            product.display_information()


class ProductFactory:
    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        weight: float | None = None,
        download_size: float | None = None,
    ) -> Product:
        # The lab CSV does not include weight or download size.
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, weight)
        if product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, download_size)
        raise ValueError(f"Unknown product type: {product_type}")
