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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
# Print report of all coffee machine resources
def cost():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    value = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return value

def checkbev(beverage):
    if beverage == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] < resources["water"] and MENU["cappuccino"]["ingredients"]["milk"] < resources["milk"] and MENU["cappuccino"]["ingredients"]["coffee"] < resources ["coffee"]:
            return True
        elif MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water")
            return False
        elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
        elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
    elif beverage == "espresso":
        if MENU["espresso"]["ingredients"]["water"] < resources["water"] and MENU["espresso"]["ingredients"]["coffee"] < resources ["coffee"]:
            return True
        elif MENU["espresso"]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water")
            return False
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
    elif beverage == "latte":
        if MENU["latte"]["ingredients"]["water"] < resources["water"] and MENU["latte"]["ingredients"]["milk"] < resources["milk"] and MENU["latte"]["ingredients"]["coffee"] < resources ["coffee"]:
            return True
        elif MENU["latte"]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water")
            return False
        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
    else:
        return

while (True):
    beverage = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if beverage == "off":
        break
    elif beverage == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}")
    elif beverage == "cappuccino":
        if checkbev("cappuccino") == True:
            cash_given = cost()
            if cash_given > MENU["cappuccino"]["cost"]:
                print("Here is your cappuccino ☕. Enjoy!")
                cash_return = round((cash_given - MENU["cappuccino"]["cost"]),2)
                print(f"Here is ${cash_return} in change.")
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                money = money + MENU["cappuccino"]["cost"]
            else:
                print("That's not enough money. Money refunded.")
    elif beverage == "espresso":
        if checkbev("espresso") == True:
            cash_given = cost()
            if cash_given > MENU["espresso"]["cost"]:
                print("Here is your espresso ☕. Enjoy!")
                cash_return = round((cash_given - MENU["espresso"]["cost"]),2)
                print(f"Here is ${cash_return} in change.")
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                money = money + MENU["espresso"]["cost"]
            else:
                print("That's not enough money. Money refunded.")
    elif beverage == "latte":
        if checkbev("latte") == True:
            cash_given = cost()
            if cash_given > MENU["espresso"]["cost"]:
                print("Here is your latte ☕. Enjoy!")
                cash_return = round((cash_given - MENU["latte"]["cost"]),2)
                print(f"Here is ${cash_return} in change.")
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                money = money + MENU["latte"]["cost"]
            else:
                print("That's not enough money. Money refunded.")

    else:
        print("Hmm sorry. Could you try again? 😄")
print("Thank you.")
