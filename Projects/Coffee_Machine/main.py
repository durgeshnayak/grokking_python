from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
shutdown = False

while not shutdown:
    welcome_message = "What would you like? (" + menu.get_items() + "): "
    choice = input(welcome_message)

    if choice.lower() == "report":
        coffee_maker.report()
    elif choice.lower() == "exit":
        shutdown = True
    else:
        menu_item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
