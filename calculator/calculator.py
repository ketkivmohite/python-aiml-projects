# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers with error handling
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main function to run the calculator
def calculator():
    print("Welcome to the Python Calculator!")
    try:
        # Get input from user and convert to float
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Choose operation: +, -, *, /")
        
        # Get operation choice from user
        operation = input("Enter operation: ")

        # Perform operation based on user input
        if operation == "+":
            print("Result:", add(num1, num2))
        elif operation == "-":
            print("Result:", subtract(num1, num2))
        elif operation == "*":
            print("Result:", multiply(num1, num2))
        elif operation == "/":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operation!")
    except ValueError:
        # Handle error if user inputs non-number
        print("Invalid input! Please enter numbers only.")

# This ensures the calculator only runs when the script is executed directly
if __name__ == "__main__":
    calculator()
