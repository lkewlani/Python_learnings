import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input == 0:
    print("You chose Rock")
    print(rock)
    valid_input = True
elif user_input == 1:
    print("You chose Paper")
    print(paper)
    valid_input = True
elif user_input == 2:
    print("You chose Scissors")
    print(scissors)
    valid_input = True
else:
    print("You chose a wrong option")
    valid_input = False

if valid_input:
    computer_input = random.randint(0,2)
    if computer_input == 0:
        print("Computer choses Rock")
        print(rock)
        if user_input == 0:
            print("Its a draw")
        elif user_input == 1:
            print("Paper beats Rock, You win")
        elif user_input == 2:
            print("Rock beats scissors, Computer wins")
    elif computer_input == 1:
        print("Computer choses Paper")
        print(paper)
        if user_input == 0:
            print("Paper beats Rock, Computer win")
        elif user_input == 1:
            print("Its a draw")
        elif user_input == 2:
            print("Scissors beats Paper, You win")
    elif computer_input == 2:
        print("Computer choses Scissors")
        print(scissors)
        if user_input == 0:
            print("Rock beats scissors, You wins")
        elif user_input == 1:
            print("Scissors beats Paper, Computer win")
        elif user_input == 2:
            print("Its a draw")