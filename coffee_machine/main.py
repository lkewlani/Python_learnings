# Coffee Machine Program Requirements
from inventory import menu, resources

# Function-Definitions--------------------------------------------------------------------------------------------------
def user_selection(selected_drink):
    if selected_drink in menu:
        print(f"You have selected {selected_drink}.")
        return True
    elif selected_drink == "off":
        print("Turning off the coffee machine.")
        return False
    elif selected_drink == "report":
        print("Current resource values:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")
        return True 
    else:
        print("Invalid selection. Please choose from espresso, latte, or cappuccino.")
        return True

def check_resources(drink):
    """Check if there are enough resources to make the selected drink."""
    ingredients = menu[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# ----------------------------------------------------------------------------------------------------------------------

# Main-Logic------------------------------------------------------------------------------------------------------------
continue_running = True
profit = 0

while continue_running:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    continue_running = user_selection(user_input)
    if not continue_running:
        break   
    else:
        if user_input == "report" or user_input not in ["latte", "cappuccino", "espresso"]:
            user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
            continue_running = user_selection(user_input)
        
        result = check_resources(user_input)
        
        if result:
            user_input_hundreds = float(input("Please insert the amount. How many hundreds?: ")) * 100
            user_input_fifties = float(input("How many fifties?: ")) * 50
            user_input_tens = float(input("How many tens?: ")) * 10
            user_input_fives = float(input("How many fives?: ")) * 5

            calulated_amount = user_input_hundreds + user_input_fifties + user_input_tens + user_input_fives
            if calulated_amount >= menu[user_input]["cost"]:
                change = calulated_amount - menu[user_input]["cost"]
                profit += menu[user_input]["cost"]
                print(f"Here is Rs.{change} in change.")
                print(f"Here is your {user_input}. Enjoy!")
                # Deduct the required resources from the available resources
                for item in menu[user_input]["ingredients"]:
                    resources[item] -= menu[user_input]["ingredients"][item]
            else:
                print("Sorry that's not enough money. Money refunded.")
                break
        else:
            print("Cannot make the drink due to insufficient resources.")
            break

