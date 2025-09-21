import random

def get_winner(player_choice, computer_choice):
    """
    Compares player and computer choices to determine the winner.
    Returns 'win', 'lose', or 'draw'.
    """
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "ROCK" and computer_choice == "SCISSORS") or \
         (player_choice == "SCISSORS" and computer_choice == "PAPER") :
        return "win"
    else:
        return "lose"

def main():
    """The main function to run the game loop."""
    choices = ["ROCK", "PAPER", "SCISSORS"]
    
    print("--- Welcome to Rock, Paper, Scissors! ---")

    while True:
        # --- 1. Get Choices ---
        # Get the user's choice and make it uppercase to match our list
        user_choice = input("\nEnter your choice (Rock, Paper, or Scissors): ").upper()

        # Validate the user's input
        if user_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue # Skip the rest of the loop and ask again

        # Get the computer's choice
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}\n")

        # --- 2. Determine the Winner ---
        result = get_winner(user_choice, computer_choice)

        if result == "win":
            print(" You win!")
        elif result == "lose":
            print("You lose!")
        else:
            print(" It's a draw!")

        # --- 3. Ask to Play Again ---
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing!")


# --- Start the game ---
if __name__ == "__main__":
    main()
