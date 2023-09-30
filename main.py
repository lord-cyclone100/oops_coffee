from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

on = True
while on:
    options = my_menu.get_items()
    choice = input (f"What would you like?{options}\nor type 'report' to show resources or 'off' to switch off:").lower()
    if choice == "report":
       my_coffee_maker.report()
       my_money_machine.report()
    elif choice == "off":
        on = False
    # elif choice != "latte" or choice != "espresso" or choice != "cappuccino" or choice != "report" or choice != "off":
    #     print ("Please enter correct option")
    else:
        coffee = my_menu.find_drink(choice)
        if (my_coffee_maker.is_resource_sufficient(coffee)):
           if (my_money_machine.make_payment(coffee.cost)):
                my_coffee_maker.make_coffee(coffee)

