#Name- Bezawit Solomon
#ID-1894/12

import random

# Defining the rules of the game
rules = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
  }

# Initializing the statistics
user_wins = 0
computer_wins = 0
draws = 0

# Take user input
user_action = input("Enter a choice (rock, paper, scissors): ")

 # Generate computer action
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)



print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# Comparing the action and update the statistics
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
    draws += 1

elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
        user_wins += 1

    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    computer_wins += 1

    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":

    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
        user_wins += 1
    else:
        print("Rock smashes scissors! You lose.")
        computer_wins += 1

print(f"User wins: {user_wins}")
print(f"Computer wins: {computer_wins}")
print(f"Draws: {draws}")
