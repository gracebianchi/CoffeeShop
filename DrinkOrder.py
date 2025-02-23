# DrinkOrder.py

from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:

    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        if isinstance(beverage, Beverage):
            self.drinks.append(beverage)
        else:
            raise ValueError("Only Beverage objects can be added to the order.")

    def getTotalOrder(self):
        total_price = 0
        order_items = []

        if not self.drinks:
            return "Order Items:\nTotal Price: $0.00"

        for drink in self.drinks:
            order_items.append(f"* {drink.getInfo()}")
            total_price += drink.getPrice()

        order_summary = "\n".join(order_items)
        return f"Order Items:\n{order_summary}\nTotal Price: ${total_price:.2f}"


