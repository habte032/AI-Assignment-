import random

def get_user_move():
    moves = ["rock", "paper", "scissors"]
    while True:
        move = input("Enter your move (rock, paper, scissors): ")
        if move in moves:
            return move
        else:
            print("Invalid move. Please try again.")

def get_computer_move():
    return random.choice(["rock", "paper", "scissors"])

def compare_moves(user_move, computer_move):
    if user_move == computer_move:
        return "tie"
    elif (user_move == "rock" and computer_move == "scissors") or (user_move == "paper" and computer_move == "rock") or (user_move == "scissors" and computer_move == "paper"):
        return "user"
    else:
        return "computer"

def print_statistics(user_score, computer_score, draw_count):
    print("Player score:", user_score)
    print("Computer score:", computer_score)
    print("Draw count:", draw_count)

# Initialize the player's and computer's scores
user_score = 0
computer_score = 0
draw_count = 0

# Start the game loop
while True:

    # Get the player's move
    user_move = get_user_move()

    # Get the computer's move
    computer_move = get_computer_move()

    # Compare the moves
    winner = compare_moves(user_move, computer_move)
    if winner == "tie":
        print("It's a tie!")
        draw_count += 1
    elif winner == "user":
        print("You win! {} beats {}".format(user_move, computer_move))
        user_score += 1
    else:
        print("Computer wins! {} beats {}".format(computer_move, user_move))
        computer_score += 1

    # Check if the player wants to play again
    play_again = input("Would you like to play again? (y/n): ")
    if play_again == "n":
        break

# Print the final statistics
print_statistics(user_score, computer_score, draw_count)