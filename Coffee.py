# Coffee.py 

from Beverage import Beverage

class Coffee(Beverage):

    def __init__(self, ounces = None, price = None, style = None):
        super().__init__(ounces, price)
        self.style = style

    def getStyle(self):
        return self.style

    def getInfo(self):
        return f"{self.style} Coffee, {super().getInfo()}"


