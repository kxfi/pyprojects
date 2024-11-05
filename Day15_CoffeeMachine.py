#you can show local history VCS pycharm
#structure pane (on the left side) you can see code structure


# make 3 hot flavors: Espresso, Latte, Cappuccino
# coin operated Penny = 0.01, Dime = 0.10, Nickel = 0.05, Quarter = 0.25

# Print report: resources left
# Check resources sufficient


# INSUFFICIENT Funds

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

#Starts with
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# ... (previous code)
def buyDrink(profit):
    # User insert coins 
    while True: 
        print("Please insert coins.")
        quarters = float(input("How many quarters? ")) * 0.25
        dimes = float(input("How many dimes? ")) * 0.10 
        nickels = float(input("How many nickels? ")) * 0.05
        pennies = float(input("How many pennies? ")) * 0.01
        totalInsert = quarters + dimes + nickels + pennies

        # Check if user has sufficient funds
        if totalInsert >= MENU[hotFlavor]['cost']:
            # User change coins
            costFlavor = MENU[hotFlavor]['cost']  # cost of hot flavor
            changeUser = totalInsert - costFlavor
            print(f"Here is ${changeUser:.2f} in change")
            
            # decrease resources after buying drink
            # take user hot flavor values and (resources - flavor values)
            '''for key in resources["water","milk","coffee"]:
                key -= MENU[hotFlavor]['ingredients'][key] for loop'''
                
            if hotFlavor != 'espresso':
                resources['water'] -= MENU[hotFlavor]['ingredients']['water']
                resources['milk'] -= MENU[hotFlavor]['ingredients']['milk']
                resources['coffee'] -= MENU[hotFlavor]['ingredients']['coffee']
            else:
                resources['water'] -= MENU[hotFlavor]['ingredients']['water']
                resources['coffee'] -= MENU[hotFlavor]['ingredients']['coffee']

            # profit amount total change after buying drink
            profit += MENU[hotFlavor]['cost']  # profit in machine (total)
            print(f"Here is your {hotFlavor} Enjoy!")
            
            return profit # Return the updated profit value and totalInsert

        else:
            print("Sorry that's not enough profit. profit refunded.")
            profit = 0
            return profit

# profit total in machine 
x = True
profit = 0  # Initialize profit outside the loop

while x:
    # What flavor user wants
    hotFlavor = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    # User must choose the only flavors or it will keep asking 
    if hotFlavor not in ['espresso', 'latte', 'cappuccino', 'report']:
        print("Sorry I don't understand, please try again")

    # resources report
    elif hotFlavor == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"profit: ${profit}")
    
    elif MENU[hotFlavor]['ingredients']['water'] > resources['water']:
        print(f"Sorry there is not enough water")
    elif hotFlavor != 'espresso' and MENU[hotFlavor]['ingredients']['milk'] > resources['milk']:
        print(f"Sorry there is not enough milk")
    elif MENU[hotFlavor]['ingredients']['coffee'] > resources['coffee']:
        print(f"Sorry there is not enough coffee")
    else:
        profit = buyDrink(profit)  # Update profit using the return value
