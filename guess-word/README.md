Word Guessing Game
A classic command-line word guessing game built in Python. The program randomly selects a secret word from a predefined list, and the player has a limited number of attempts to guess the word one letter at a time.

Features
Random Word Selection: A random word is chosen from a word bank at the start of each game.

Limited Attempts: Players have 6 attempts to guess the word, making the game challenging.

Interactive Display: The game displays the partially guessed word (e.g., p _ t h _ n) after each turn.

Input Validation: The program validates user input to ensure it is a single letter and has not been guessed before.

Win/Loss Conditions: The game clearly announces whether the player has won by guessing the word or lost by running out of attempts.

Key Concepts Learned
Random Module: Utilized the random.choice() function to randomly select an item from a list.

Lists and String Manipulation: Used lists to manage the word bank, the letters of the secret word, and the letters guessed so far. The ' '.join() method was used to create a clean display for the user.

Loops (while): The main game logic is controlled by a while loop that continues as long as the player has attempts remaining.

Conditional Logic (if/elif/else): Implemented complex conditional logic to check if a guessed letter is in the word, validate user input, and determine win/loss conditions.

User Input (input()): Captured and processed user input to drive the game.