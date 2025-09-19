# Import the `mean` function from the statistics library and give it a shorter alias 'm'
from statistics import mean as m

# --- Data ---
# A dictionary to store admin login credentials
admins = {'Python': 'Pass@123'}

# A dictionary to store student names and their list of grades
studentDict = {
    'Seeta': [76, 78, 75],
    'Geeta': [87, 88, 89],
    'Reeta': [90, 65, 67]
}

# --- Functions ---

def enterGrades():
    """Adds a new grade to an existing student's record."""
    nameToEnter = input('Student Name: ')
    
    # Use a try-except block for robust input validation
    try:
        gradeToEnter = float(input('Grade: '))
    except ValueError:
        print("Invalid input. Please enter a number for the grade.")
        return # Exit the function if the grade is not a number

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(gradeToEnter)
    else:
        print('Student does not exist.')

    print(studentDict)

def removeStudent():
    """Removes a student from the records."""
    nameToRemove = input('What Student to Remove?: ')
    if nameToRemove in studentDict:
        print('Removing student...')
        del studentDict[nameToRemove]
    else:
        print("Student not found.")

    print(studentDict)

def studentAvgs():
    """Calculates and displays the average grade for each student."""
    print("\n--- Student Averages ---")
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        print(f'{eachStudent} has an average grade of: {avgGrade:.2f}')

def main():
    """The main function to run the application."""
    
    # --- 1. Login ---
    print("--- Welcome to Grade Central ---")
    login = input('Username: ')
    password = input('Password: ')

    # Check if the login credentials are correct
    if login in admins and admins[login] == password:
        print(f'\nWelcome, {login}!')
        
        # --- 2. Main Application Loop ---
        # This loop will continue until the user chooses to exit.
        while True:
            print("\n[1] - Enter Grades")
            print("[2] - Remove Student")
            print("[3] - Student Average Grades")
            print("[4] - Exit")
            
            action = input('What would you like to do today? (Enter a number): ')

            if action == "1":
                enterGrades()
            elif action == "2":
                removeStudent()
            elif action == "3":
                studentAvgs()
            elif action == "4":
                print("\nLogging out. Goodbye!")
                break # This is the correct way to exit the loop
            else:
                print("\nNo valid choice was given, try again.")
    else:
        print("Invalid username or password. Access denied.")


# --- Start the program ---
if __name__ == "__main__":
    main()
