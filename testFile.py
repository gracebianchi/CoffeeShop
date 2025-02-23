# testFile.py

from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

def test_Beverage():
    b = Beverage(12, 2.5)
    assert b.getOunces() == 12
    assert b.getPrice() == 2.5
    assert b.getInfo() == "12 oz, $2.50"

    b.updateOunces(15)
    assert b.getOunces() == 15

    b.updatePrice(3.0)
    assert b.getPrice() == 3.0

def test_Coffee():
    c = Coffee(14, 5.0, "Latte")
    assert c.getStyle() == "Latte"
    assert c.getInfo() == "Latte Coffee, 14 oz, $5.00"

def test_FruitJuice():
    j = FruitJuice(12, 5.5, ["Orange", "Mango"])
    assert j.getFruits() == ["Orange", "Mango"]
    assert j.getInfo() == "Orange/Mango Juice, 12 oz, $5.50"
    
def test_DrinkOrder():
    coffee = Coffee(14, 6.0, "Espresso")
    juice = FruitJuice(16, 4.0, ["Strawberry", "Watermelon"])
    beverage = Beverage(12, 5.5)
    order = DrinkOrder()

    order.addBeverage(coffee)
    order.addBeverage(juice)
    order.addBeverage(beverage)
    assert len(order.drinks) == 3

    total_price = coffee.getPrice() + juice.getPrice() + beverage.getPrice()
    order_summary = order.getTotalOrder()
    
    assert "* Espresso Coffee, 14 oz, $6.00" in order_summary
    assert "* Strawberry/Watermelon Juice, 16 oz, $4.00" in order_summary
    assert "* 12 oz, $5.50" in order_summary
    assert f"Total Price: ${total_price:.2f}" in order_summary
    
    
