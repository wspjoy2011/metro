from typing import List, Protocol


class Item(Protocol):
    quantity: int
    price: float


class Product:
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


class Stock:
    def __init__(self, company_name: str, quantity: int, price: float):
        self.product_name = company_name
        self.quantity = quantity
        self.price = price


def calculate_total(items: List[Item]) -> float:
    return round(sum([item.quantity * item.price for item in items]), 2)


purchases = [
    Product('PC', 10, 150.0),
    Product('Notebook', 5, 250.0),
    Stock('APL', 100, 47.17),
    Stock('NYT', 57, 119.7),
]

final_cost = calculate_total(purchases)
print(final_cost)
