menu = {
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
def check(a):
    global resources
    global menu
    global continue_
    if menu[a]["ingredients"]["water"] > resources["water"]:  
        print("Sorry that's not enough water")
        continue_ = False
    elif menu[a]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry that's not enough milk")
        continue_ = False
    elif menu[a]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry that's not enough coffee")
        continue_ = False
    else:
        continue_ = True
def paid(a):
    global resources
    global menu
    global money
    print("Please insert coins")
    quart = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nick = float(input("How many nickles? "))
    penn = float(input("How many pennies? "))
    total = (0.25 * quart) + (0.10 * dimes) + (0.05 * nick) + (0.01 * penn)
    if total == menu[a]["cost"]:
        money += total
        print(f" Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n \
Coffee: {resources['coffee']}g\n Money: ${money}")
        print("bon apetite")
    elif total > menu[a]["cost"]:
        money += menu[a]["cost"]
        print(f"bon apetite, your change  ${round(total - menu[a]['cost'])}")
    elif total < menu[a]["cost"]:
        print(f"{a} cost ${menu[a]['cost']}, Sorry that's not enougf money. Money refunded")
def choose(a):
    if a == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif a == "latte":
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150
    elif a == "cappuccino":
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100

continue_ = True
while continue_:
    desired = input("What would you like? espresso, latte, cappucino ").lower()
    if desired == "off":
        break
    elif desired == "report":
        print(f" Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n \
Coffee: {resources['coffee']}g\n Money: ${money}")
    elif desired == "espresso":
        check(a=desired)
        if continue_ == False:
            break
        choose(a=desired)
        paid(a=desired)
    elif desired == "latte":
        check(a=desired)
        if continue_ == False:
            break
        choose(a=desired)
        paid(a=desired)
    elif desired == "cappuccino":
        check(a=desired)
        if continue_ == False:
            break
        choose(a=desired)
        paid(a=desired)