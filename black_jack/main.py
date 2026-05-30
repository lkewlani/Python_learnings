import random
from art import logo

def draw_new_card(cards):
    card_drawn = random.sample(cards,1)
    return card_drawn

def cards_score(selected_cards):
    total_score = 0
    for card in selected_cards:
        total_score += card
    return total_score

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ").lower()

# Logo Display
print(logo)

# User's Current Cards drawn and Cards Score
user_cards_list = random.sample(cards, 2)
user_cards_score = cards_score(user_cards_list)
print(f"Your Cards: {user_cards_list}, Current Card Score = {user_cards_score}")

# Computer's Current Cards drawn and Cards Score
computer_first_draw = random.sample(cards, 1)
computer_first_score = cards_score(computer_first_draw)
print(f"Computer's Cards: {computer_first_draw}, Current Card Score = {computer_first_score}")

# Continue drawing
continue_flag = input("Would you like to continue ? Type 'y' to Continue or 'n' to Pass: ").lower()
new_user_list = user_cards_list
new_comp_list = computer_first_draw
new_user_score = user_cards_score
new_comp_score = computer_first_score

while continue_flag == "y":
# User New Card Draw
    new_user_list = new_user_list + draw_new_card(cards)
    new_user_score = cards_score(new_user_list)
    print(f"Your Cards: {new_user_list}, Current Card Score = {new_user_score}")

# Computer New Card Draw
    new_comp_list = new_comp_list + draw_new_card(cards)
    new_comp_score = cards_score(new_comp_list)
    print(f"Computer's Cards: {computer_first_draw}, Current Card Score = {computer_first_score}")

    if new_user_score > 21:
        continue_flag = "n"
        print(f"You went over 21, Game Over! You Lose!")
        exit()
    else:
        continue_flag = input("Would you like to continue ? Type 'y' to Continue or 'n' to Pass: ").lower()

if continue_flag == "n":
    print(f"Your Final Hand: {new_user_list}, Final Card Score = {new_user_score}")

# Computer New Card Draw
    new_comp_list = new_comp_list + draw_new_card(cards)
    new_comp_score = cards_score(new_comp_list)
    print(f"Computer's Final Hand: {new_comp_list}, Final Card Score = {new_comp_score}")

    if new_user_score > new_comp_score:
        print("You Win!")
    elif new_user_score == new_comp_score:
        print("Draw!")
    else:
        print("You Lose!")