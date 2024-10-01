from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cmaker = CoffeeMaker()
menu = Menu()
mmachine = MoneyMachine()
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cmaker.report()
        mmachine.report()
    else:
        drink = menu.find_drink(choice)
        if cmaker.is_resource_sufficient(drink):
            if mmachine.make_payment(drink.cost):
                cmaker.make_coffee(drink)


