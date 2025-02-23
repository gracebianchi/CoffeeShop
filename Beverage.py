# Beverage.py

class Beverage:

    def __init__(self, ounces = None, price = None):
        self.ounces = int(ounces)
        self.price = float(price)

    def updateOunces(self, newOunces):
        self.ounces = newOunces

    def updatePrice(self, newPrice):
        self.price = newPrice

    def getOunces(self):
        return self.ounces

    def getPrice(self):
        return self.price

    def getInfo(self):
        return f"{self.ounces} oz, ${self.price:.2f}"

