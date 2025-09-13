# --- 1. The Quiz Data ---
# A list of dictionaries, where each dictionary is a single question.
quiz_questions = [
    {
        "question": "What is the National Flower of India?",
        "options": ["A. Rose", "B. Lotus", "C. Lily", "D. Sunflower"],
        "answer": "B"
    },
    {
        "question": "When did India get its Independence?",
        "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1962"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Maharashtra?",
        "options": ["A. Pune", "B. Nagpur", "C. Mumbai", "D. Nashik"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    }
]

# --- 2. The Game Setup ---
score = 0
print("Welcome to the Simple Quiz Game!")
print("---------------------------------")


# --- 3. The Main Game Loop ---
# Loop through each question dictionary in the quiz_questions list
for question_data in quiz_questions:
    # Print the question
    print("\n" + question_data['question'])

    # Print all the options for that question
    for option in question_data['options']:
        print(option)

    # Get the user's answer
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()

    # Check if the answer is correct
    if user_answer == question_data['answer']:
        print("Correct! Great job.")
        # Add 1 to the score if correct
        score += 1
    else:
        # Show the correct answer if the user was wrong
        print(f"Wrong! The correct answer was {question_data['answer']}.")


# --- 4. The Final Score ---
# This code runs after the for loop is completely finished
print("\n---------------------------------")
print("Quiz Over! You've completed the quiz.")
# len(quiz_questions) gives us the total number of questions
print(f"Your final score is: {score} out of {len(quiz_questions)}")

