from typing import List

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 100,
    "milk": 50,
    "coffee": 100,
}


def display_report(machine_resources: dict):
    """
    When the user enters "report" to the prompt, a report should be generated that shows the current resource values:

    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
    """
    print(f'Water: {machine_resources["water"]}ml')
    print(f'Milk: {machine_resources["milk"]}ml')
    print(f'Coffee: {machine_resources["coffee"]}g')
    if "money" not in machine_resources.keys():
        machine_resources["money"] = 0.0
    print(f'Money: ${machine_resources["money"]}')


def resources_sufficient(machine_resources: dict, drink: str, menu: dict):
    """
    User chooses drink, check if enough resources to make drink
    Latte requires 200ml water by only 100ml is left; don't make drink; "Sorry, there is not enough <ingredient>"
    Same should happen for other resource if depleted
    """
    insufficient_resource: List[str] = []

    drink = menu[drink]['ingredients']
    water_to_consume: int = drink['water']
    if 'milk' not in drink:
        drink['milk'] = 0
    milk_to_consume: int = drink['milk']
    coffee_to_consume: int = drink['coffee']

    if water_to_consume > machine_resources["water"]:
        insufficient_resource.append("Water")
    if milk_to_consume > machine_resources["milk"]:
        insufficient_resource.append("Milk")
    if coffee_to_consume > machine_resources["coffee"]:
        insufficient_resource.append("Coffee")

    """
    else:
        drink['water'] -= water_to_consume
        drink['milk'] -= milk_to_consume
        drink['coffee'] -= coffee_to_consume
    """

    if len(insufficient_resource) > 0:
        print(f'Sorry, there is not enough of the following ingredients: \n\t\
            {", ".join(resource for resource in insufficient_resource)}.')
        return False
    else:
        return True


def request_coins():
    """Prompt for coins and sum up coins given"""
    coins = {
        "quarter": .25,
        "dime": .10,
        "nickle": .05,
        "penny": .01,
    }
    num_quarters: int = int(input("How many quarters?: "))
    num_dimes: int = int(input("How many dimes?: "))
    num_nickles: int = int(input("How many nickles?: "))
    num_pennies: int = int(input("How many pennies?: "))

    total = (num_quarters * coins['quarter']) + (num_dimes * coins['dime']) + (num_nickles * coins['nickle']) \
        + num_pennies * coins['penny']

    return total


def check_transaction(drink_cost: float, inserted_coins: float, machine_resources: dict):
    """Take in the drink type for the total cost"""
    if drink_cost > inserted_coins:
        print("Sorry. That's not enough money. Money refunded.")
    elif drink_cost < inserted_coins:
        change: float = inserted_coins - drink_cost
        print(f'Here is ${change} in change.')
        if "money" not in machine_resources.keys():
            machine_resources["money"] = drink_cost
        else:
            machine_resources["money"] += drink_cost

        return round(machine_resources["money"], 2)


def make_drink(drink_ingredients: dict, machine_resources: dict, drink: str):
    """Makes the drink and deducts resources!"""
    machine_resources['water'] -= drink_ingredients['water']
    if 'milk' in drink_ingredients:
        machine_resources['milk'] -= drink_ingredients['milk']
    machine_resources['coffee'] -= drink_ingredients['coffee']
    print(f'Here is your {drink}. Enjoy!')
    return machine_resources





# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# Check user's input to decide what to do next
# Prompt should show every time action has completed; once the drink is dispensed. Prompt again to server next.
isRunning: bool = True

while isRunning:
    cmd = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    # For maintainers of the machine, they can use "off" as the secret word to turn off the machine. Code should end.
    if cmd == 'off':
        isRunning = False

    # TODO: 3 Print report
    # When the user enters "report" to the prompt, a report should be generated that shows the current resource values:
    if cmd == "report":
        display_report(resources)

    # TODO: 4. Check resources sufficient?
    # User chooses drink, check if enough resources to make drink
    # Latte requires 200ml water by only 100ml is left; don't make drink; "Sorry, there is not enough <ingredient>"
    # Same should happen for other resource if depleted
    for item in MENU:
        if item == cmd:
            if resources_sufficient(resources, cmd, MENU):
                # TODO: 5. Process coins
                # Enough resources, prompt for coins
                # Calculate value
                payment = request_coins()

                # TODO: 6. Check transaction successful?
                # Check user inserted enough money to buy their drink; not enough \
                # "Sorry, that's not enough money. Money refunded."
                # Cost of drink gets added to the machine as the profit and reflects next time report is triggered
                # Too much money, offer change! "Here's $2.45 dollars in change." Decimal for 2 places.
                resources["money"] = check_transaction(MENU[cmd]['cost'], payment, resources)

                # print(resources["money"])

                # TODO: 7. Make Coffee
                # Txn successful, enough resources, deduct ingredients from resources
                # All resources deducted: "Here is your <drink type>. Enjoy!"
                resources = make_drink(MENU[cmd]['ingredients'], resources, cmd)
