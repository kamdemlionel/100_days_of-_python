
from carte import MENU, resources

command = input("What would you like? (espresso/latte/cappuccino): ").lower()

def check_resource(cmd):
    """Check if enough resources are available to make the drink."""
    if resources["water"] < MENU[cmd]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif resources["milk"] < MENU[cmd]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif resources["coffee"] < MENU[cmd]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True

def check_sufficient(cmd, total):
    """Check if the inserted money is enough."""
    if total < MENU[cmd]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - MENU[cmd]["cost"], 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {cmd} ☕. Enjoy!")
        return True

def deduction(cmd):
    """Deduct the resources used to make the drink."""
    resources["water"] -= MENU[cmd]["ingredients"]["water"]
    resources["milk"] -= MENU[cmd]["ingredients"]["milk"]
    resources["coffee"] -= MENU[cmd]["ingredients"]["coffee"]
    print(f"Updated resources: water={resources['water']}, milk={resources['milk']}, coffee={resources['coffee']}")


if command == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


elif command in MENU:
    if check_resource(command):
        print("Please insert coins.")
        quarters_amt = int(input("How many quarters?: "))
        dimes_amt = int(input("How many dimes?: "))
        nickles_amt = int(input("How many nickles?: "))
        pennies_amt = int(input("How many pennies?: "))

        total = (quarters_amt * 0.25) + (dimes_amt * 0.10) + (nickles_amt * 0.05) + (pennies_amt * 0.01)

        if check_sufficient(command, total):
            deduction(command)
else:
    print("Invalid command.")

 