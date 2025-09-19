Student Grading System
A command-line application built in Python to manage student grades. The system is protected by a simple admin login and allows an authorized user to add grades to a student's record, remove a student entirely, and view the average grade for each student in the system.

This project was a key part of a "Programming with Python 3.X" certification and demonstrates the use of more complex data structures and program flow.

Features
Admin Login: The application is protected by a basic username and password authentication system.

Add Grade: Allows the admin to add a new numerical grade to any existing student's list of scores.

Remove Student: Provides the functionality to completely remove a student and all their associated grades from the system.

Calculate Averages: Automatically calculates and displays the average grade for each student using the statistics library.

Robust Input: The system validates user input to ensure that grades entered are always valid numbers, preventing crashes.

Key Concepts Learned & Practiced
Complex Data Structures: Utilized a dictionary where the values are lists ({'StudentName': [grade1, grade2]}) to store complex, related data efficiently.

Modular Code with Functions: Organized all major features into their own functions (enterGrades, removeStudent, studentAvgs) to create clean, readable, and reusable code.

Using Built-in Libraries: Imported and used the mean function from Python's built-in statistics library to perform calculations.

Program Control Flow: Structured the application with a main login gate that, upon success, enters a while loop for the main menu, which is controlled by if/elif/else statements.