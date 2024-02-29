from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    drink = menu.find_drink(order)
    if drink:
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
    elif order == "report":
        coffe_maker.report()
        money_machine.report()
    elif order == "off":
        is_on = False
