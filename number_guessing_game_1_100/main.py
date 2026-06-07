import random
from art import logo

print(logo)
print("Welcome to the number guessing Game!")
print("I am thinking a number between 1 and 100.")

# Select a number between 1 and 100.
num = random.randint(1, 100)

# Choose a Difficulty
diff_level = input("Choose a Difficulty Level, Type 'easy' or 'hard': ").lower()

no_of_guesses = 0
if diff_level == "easy":
    no_of_guesses = 10
elif diff_level == "hard":
    no_of_guesses = 5
else:
    print("Invalid Level Selection, try again.")

print(f"You have {no_of_guesses} attempts remaining to guess the number.")

number_guessed = False
for _ in range(no_of_guesses):
    guess = int(input("Guess a number: "))
    if guess == num:
        print("Congratulations, you guessed the number!")
        number_guessed = True
        break
    elif guess < num:
        print("Your guess is too low.")
    elif guess > num:
        print("Your guess is too high.")

if not number_guessed:
    print(f"You've run out of guesses, the number I was thinking of was {num}.")
