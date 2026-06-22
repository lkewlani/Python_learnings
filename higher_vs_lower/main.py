from data import data
from art import logo, vs
import random

# Function-Definitions--------------------------------------------------------------------------------------------------
# Format the account data into printable format
def account_data(account):
    """Take the account data and return it in a printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}."

# Compare the followers
def check_answer(user_guess, a_followers, b_followers):
    """Take the user guess and return True or False"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
# ----------------------------------------------------------------------------------------------------------------------

# Main-Logic------------------------------------------------------------------------------------------------------------
# Generate random account
print(logo)
account_b = random.choice(data)
score = 0
continue_game = True

# Make the game repeatable
while continue_game:
    # Re-generate the account B if both the random choices are picked same
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # Start the game
    print(f"Compare A: {account_data(account_a)}")
    print(vs)
    print(f"Compare B: {account_data(account_b)}")

    # Ask user to guess
    guess = input("Enter your guess, who has more followers? Type 'A' or 'B': ").lower()

    # Check if the user is correct
    # - Get follower count of each account
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    # - Use if statement to see the user is correct or not
    guess_is_correct = check_answer(guess, follower_count_a, follower_count_b)
    if guess_is_correct:
        score += 1
        print(f"You've guessed correctly!")
    else:
        print(f"Sorry, you failed to guess correctly!")
        continue_game = False

    print(f"Total score: {score}")
