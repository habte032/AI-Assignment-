# Rock Paper Scissor game
# Name: Abraham Shiferaw
# ID: 0704/12

import random

moves = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
draw_count = 0
while True:
    player_move = input("Enter your move (rock, paper, scissors): ")
    computer_move = random.choice(moves)
    print('Computer move: ', computer_move)
    if player_move == computer_move:
        print("It's a tie!")
        draw_count += 1
    elif player_move == "rock" and computer_move == "scissors":
        print("You win! Rock smashes scissors.")
        player_score += 1
    elif player_move == "paper" and computer_move == "rock":
        print("You win! Paper covers rock.")
        player_score += 1
    elif player_move == "scissors" and computer_move == "paper":
        print("You win! Scissors cuts paper.")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    play_again = input("Would you like to play again? (y/n): ")
    if play_again == "n":
        break
print("Player score:", player_score)
print("Computer score:", computer_score)
print("Draw count:", draw_count)