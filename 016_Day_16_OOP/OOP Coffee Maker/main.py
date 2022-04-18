from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu

cash_box = MoneyMachine() # should be named money_machine
coffee_unit = CoffeeMaker() # should be named coffee_maker
drink_options = Menu() # should be namemd menu

is_on: bool = True

while is_on:
    choice = input(f'What would you like? {(drink_options.get_items())}: ') # she stored this in a variable; so two lines of code for it
    if choice == "off":
        is_on = False
    # TODO: Print Report
    elif choice == "report":
        coffee_unit.report()
        cash_box.report()
    else:
        found_drink = drink_options.find_drink(choice) # just named it drink
        # TODO: Check resources sufficient?
        if coffee_unit.is_resource_sufficient(found_drink): # use an AND here and run the MAKE_PAYMENT() function
            # TODO: Process coins
            # TODO: Check transaction successful?
            if cash_box.make_payment(found_drink.cost):
                # TODO: Make coffee
                coffee_unit.make_coffee(found_drink)








