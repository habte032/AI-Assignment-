import random


def get_user_choice():
    """Get the user's choice of rock, paper, or scissors."""
    while True:
        user_choice = input("Choose rock (r), paper (p), or scissors (s): ")
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid choice. Please choose again.")


def get_computer_choice():
    """Get the computer's random choice of rock, paper, or scissors."""
    return random.choice(['r', 'p', 's'])


def compare_choices(user_choice, computer_choice):
    """Compare the user's and computer's choices to determine the winner."""
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == 'r' and computer_choice == 's') or \
            (user_choice == 'p' and computer_choice == 'r') or \
            (user_choice == 's' and computer_choice == 'p'):
        return "user"
    else:
        return "computer"


def print_results(results):
    """Print the results of the game."""
    print("\nResults:")
    print("=========")
    print(f"You won {results['user']} times.")
    print(f"The computer won {results['computer']} times.")
    print(f"There were {results['draw']} draws.")
    if results['user'] > results['computer']:
        print("Congratulations, you win!")
    elif results['user'] < results['computer']:
        print("Sorry, the computer wins.")
    else:
        print("It's a tie!")


def play_game():
    """Play a round of rock, paper, scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = compare_choices(user_choice, computer_choice)
    print(f"\nYou chose {user_choice}. The computer chose {computer_choice}.")
    if result == "user":
        print("You win!")
        return "user"
    elif result == "computer":
        print("The computer wins!")
        return "computer"
    else:
        print("It's a draw.")
        return "draw"


def main():
    """Play multiple rounds of rock, paper, scissors."""
    num_rounds = 0
    while True:
        try:
            num_rounds = int(input("How many rounds do you want to play? "))
            if num_rounds <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    results = {"user": 0, "computer": 0, "draw": 0}
    for i in range(num_rounds):
        print(f"\nRound {i + 1}:")
        result = play_game()
        results[result] += 1

    print_results(results)


