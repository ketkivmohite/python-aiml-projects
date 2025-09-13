import random

# A list of words for the game
word_bank = ['python', 'github', 'developer', 'project', 'learning']

# Choose a random word from the bank to be the correct answer
secret_word = random.choice(word_bank)

# Create the initial display for the guessed word, e.g., ['_', '_', '_', '_', '_']
guessed_word_display = ['_'] * len(secret_word)

attempts = 6
already_guessed_letters = []

print("Welcome to the Word Guessing Game!")
print("You have 6 attempts to guess the word.")

# The main game loop
while attempts > 0:
    # Print the current state of the word, e.g., "_ . y . t . _ . _ . n"
    print('\nCurrent word: ' + ' '.join(guessed_word_display))
    print(f"Attempts left: {attempts}")

    # Get the user's guess
    guess = input('Guess a letter: ').lower()

    # --- Input Validation ---
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please guess a single letter.")
        continue # Skip the rest of the loop and start from the top

    if guess in already_guessed_letters:
        print(f"You've already guessed the letter '{guess}'. Try another one.")
        continue

    # Add the guess to the list of letters already tried
    already_guessed_letters.append(guess)


    # --- Check the Guess ---
    if guess in secret_word:
        print(f"\nGreat guess! The letter '{guess}' is in the word.")
        # Update the display to show the correctly guessed letter
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word_display[i] = guess
    else:
        attempts -= 1 # Lose an attempt only on a wrong guess
        print(f"\nWrong guess! The letter '{guess}' is not in the word.")


    # --- Check for a Win ---
    if '_' not in guessed_word_display:
        print('\nCongratulations! You guessed the word: ' + secret_word)
        break # Exit the loop because the game is won


# --- Check for a Loss (this code runs only if the while loop finishes naturally) ---
if attempts == 0 and '_' in guessed_word_display:
    print('\nYou\'ve run out of attempts! The word was: ' + secret_word)