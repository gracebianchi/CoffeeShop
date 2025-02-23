# FruitJuice.py

from Beverage import Beverage

class FruitJuice(Beverage):

    def __init__(self, ounces = None, price = None, fruits = None):
        super().__init__(ounces, price)
        self.fruits = fruits

    def getFruits(self):
        return self.fruits

    def getInfo(self):
        fruits_str = '/'.join(self.fruits)
        return f"{fruits_str} Juice, {super().getInfo()}"


