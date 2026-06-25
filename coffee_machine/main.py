# Coffee Machine Program Requirements
from inventory import menu, resources

# Function-Definitions--------------------------------------------------------------------------------------------------
def user_selection(selected_drink):
    if selected_drink in menu:
        print(f"\nYou have selected {selected_drink}.")
        return True
    elif selected_drink == "off":
        print("\nTurning off the coffee machine.")
        return False
    elif selected_drink == "report":
        print("\nCurrent resource values:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")
        return True 
    else:
        print("\nInvalid selection. Please choose from espresso, latte, cappuccino, or filter coffee.")
        return True

def check_resources(drink):
    """Check if there are enough resources to make the selected drink."""
    ingredients = menu[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"\nSorry, there is not enough {item}, Cannot make the drink due to insufficient resources!!!!")
            return False
    return True

def validate_amount(user_amount):
    """Validate the user input for amount of money inserted."""
    try:
        user_amount_inp = float(input(f"\nPlease insert the amount. How many {user_amount}?: ")) 
        return float(user_amount_inp)
    except ValueError:
        print("Invalid input. Please enter a valid numerical value.")
        user_amount_inp = float(input(f"\nPlease insert the amount. How many {user_amount}?: ")) 
        return float(user_amount_inp)
# ----------------------------------------------------------------------------------------------------------------------

# Main-Logic------------------------------------------------------------------------------------------------------------
continue_running = True
result = True
profit = 0

# Denominations 
denominations = {"hundreds": 100.00, "fifties": 50.00, "tens": 10.00, "fives": 5.00}

# Lets start the coffee machine and accept user input for the drink selection
while continue_running:
    # Accept user Input 
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino/filter coffee): ").lower()

    # Validate the User Input
    continue_running = user_selection(user_input)
    
    # Give the user 3 chances to select a valid drink or report
    if not continue_running:
        break   
    else:
        number_of_turns = 0
        while user_input == "report" or user_input not in menu:
            user_input = input("\nWhat would you like? (espresso/latte/cappuccino/filter coffee): ").lower()
            continue_running = user_selection(user_input)
            number_of_turns += 1
            if number_of_turns == 3:
                print("You have exceeded your maximum 3 number of turns. Please try again later.")
                continue_running = False
                break

    # Check if there are enough resources to make the selected drink
    result = check_resources(user_input)

    # Validate the amount of money inserted by the user and process the transaction
    if result == True and continue_running == True:
        """Accept, validate and calculate the amount of money inserted by the user"""
        calulated_amount = 0
        for denomination, value in denominations.items():
            user_input_amount = validate_amount(denomination) * value
            calulated_amount += user_input_amount
            print(calulated_amount)

        # Process the transaction if the user has inserted enough money for the selected drink
        if calulated_amount >= menu[user_input]["cost"]:
            change = calulated_amount - menu[user_input]["cost"]
            profit += menu[user_input]["cost"]
            print(f"\nHere is Rs.{change} in change.")
            print(f"Here is your {user_input}. Enjoy!")
            
            # Deduct the required resources from the available resources
            for item in menu[user_input]["ingredients"]:
                resources[item] -= menu[user_input]["ingredients"][item]
        else:
            print("\nSorry that's not enough money. Money refunded.")
            break
    else:
        break
