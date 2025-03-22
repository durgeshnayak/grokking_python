import data

money = 0


def print_report():
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Money: {money}$")


def calculate_price(choice, quarters, dimes, nickels, pennies):
    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    coffee_price = int(data.MENU[choice]["cost"])
    return round(total_amount - coffee_price, 2)


def can_make_coffee(choice):
    coffee = data.MENU[choice]
    if choice != "espresso":
        milk = int(coffee["ingredients"]["milk"])
        if milk > int(data.resources["milk"]):
            return "milk"
    water = int(coffee["ingredients"]["water"])
    if water > int(data.resources["water"]):
        return "water"
    coffee = int(coffee["ingredients"]["coffee"])
    if coffee > int(data.resources["coffee"]):
        return "coffee"
    return "OK"


def make_coffee(choice):
    coffee = data.MENU[choice]
    if choice != "espresso":
        milk = int(coffee["ingredients"]["milk"])
        resources_milk = int(data.resources["milk"])
        resources_milk -= milk
        data.resources["milk"] = resources_milk
    water = int(coffee["ingredients"]["water"])
    resources_water = int(data.resources["water"])
    resources_water -= water
    data.resources["water"] = resources_water
    coffee = int(coffee["ingredients"]["coffee"])
    resources_coffee = int(data.resources["coffee"])
    resources_coffee -= coffee
    data.resources["coffee"] = resources_coffee


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        ingredient = can_make_coffee(choice)
        if ingredient != "OK":
            print(f"Sorry there is not enough {ingredient}.")
        else:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            change = calculate_price(choice=choice, quarters=quarters, dimes=dimes, nickels=nickels, pennies=pennies)
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if ingredient == "OK":
                    money += data.MENU[choice]["cost"]
                    make_coffee(choice=choice)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice} ☕. Enjoy!")
                else:
                    print(f"Sorry there is not enough {ingredient}.")
