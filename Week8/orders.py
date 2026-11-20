from abc import ABC, abstractmethod
from math import isfinite

from products import Product


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self._percentage = percentage

    def apply(self, total: float) -> float:
        return total * (100 - self._percentage) / 100


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float):
        if not isfinite(threshold) or not isfinite(amount) or not 0 <= amount <= threshold:
            raise ValueError("Bulk discount requires 0 <= amount <= threshold.")
        self._threshold = threshold
        self._amount = amount

    def apply(self, total: float) -> float:
        if total >= self._threshold:
            return total - self._amount
        return total


class StudentDiscount(PercentageDiscount):
    def __init__(self):
        super().__init__(5)


class OrderLine:
    def __init__(self, product: Product, quantity: int):
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Quantity must be greater than zero and a whole number.")
        self._product = product
        self._quantity = quantity

    def calculate_subtotal(self) -> float:
        return self._product.price * self._quantity


class Order:
    def __init__(self, discount: DiscountStrategy | None = None):
        self._order_lines: list[OrderLine] = []
        self._discount = NoDiscount() if discount is None else discount

    def add_product(self, product: Product, quantity: int) -> None:
        self._order_lines.append(OrderLine(product, quantity))

    def set_discount(self, discount: DiscountStrategy) -> None:
        self._discount = discount

    def calculate_total(self) -> float:
        subtotal = sum(line.calculate_subtotal() for line in self._order_lines)
        return self._discount.apply(subtotal)
