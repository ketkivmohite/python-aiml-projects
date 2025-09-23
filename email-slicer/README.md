Email Slicer
A simple command-line application built with Python that splits an email address into its username and domain name.

This project is a great exercise for practicing basic string manipulation and handling user input gracefully.

Features
User-Provided Email: The user can enter any email address to be processed.

Username & Domain Separation: The application cleanly splits the email at the @ symbol to isolate the username and the domain.

Input Validation: The script uses a try-except block to ensure the user enters a valid email format (i.e., one containing an @ symbol), preventing crashes from invalid input.

Whitespace Cleaning: Automatically removes any leading or trailing spaces from the user's input using the .strip() method.

Key Concepts Learned & Practiced
String Methods: Utilized the .strip() function to clean whitespace and the .split() function to break the string into a list based on a delimiter.

Error Handling (try-except): Implemented error handling to manage ValueError exceptions that occur if the user's input does not contain the @ delimiter.

User Input: Used the input() function to capture the email address from the user in the terminal.

f-Strings: Employed formatted string literals to create a clean, readable output for the user.