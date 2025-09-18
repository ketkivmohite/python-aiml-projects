import random

def coinflip():
    """Simulates a single coin flip and returns the result."""
    
    # The `random.choice()` function will randomly pick one item from this list.
    result = random.choice(["Heads", "Tails"])
    
    
    print(f"\n...The coin lands on: {result}!...")


# --- Main Program Loop ---
def main():
    print("--- Welcome to the Coin Flip Simulator! ---")
    
    while True:
        # Wait for the user to press Enter to flip the coin
        input("Press Enter to flip the coin...")
        
        # Call your coinflip function
        coinflip()
        
        # Ask the user if they want to flip again
        play_again = input("\nFlip again? (yes/no): ").lower()
        if play_again != 'yes':
            break # Exit the loop if the answer is not 'yes'
            
    # This line is now unindented to be outside the loop
    print("\nThanks for playing!")


# --- Start the game ---
# It tells Python to run the main() function when the script starts.
if __name__ == "__main__":
    main()

