def calculate_bmi():
    """
    Asks for weight and height, calculates BMI, and displays the result and category.
    """
    print("---  BMI Calculator ---")

    try:
        # --- 1. Get User Input ---
        # Get weight and convert it to a float (number with decimals)
        weight_kg = float(input("Enter your weight in kilograms (kg): "))
        
        # Get height and convert it to a float
        height_m = float(input("Enter your height in meters (m): "))

        if weight_kg <= 0 or height_m <= 0:
            print("\nError: Weight and height must be positive numbers.")
            return # Exit the function if input is invalid

        # --- 2. Calculate BMI ---
        # The formula is weight / (height squared)
        bmi = weight_kg / (height_m * height_m)

        # --- 3. Determine the Category ---
        category = ""
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else: # bmi >= 30
            category = "Obesity"

        # --- 4. Display the Results ---
        print("\n--- Your BMI Result ---")
        # The :.2f formats the number to show only two decimal places
        print(f"Your BMI is: {bmi:.2f}")
        print(f"This is considered: {category}")
        print("-----------------------")

    except ValueError:
        # This will run if the user enters text instead of a number
        print("\nError: Invalid input. Please enter numbers for weight and height.")
    except ZeroDivisionError:
        # This will run if the user enters 0 for height
        print("\nError: Height cannot be zero.")


# --- Run the main function ---
if __name__ == "__main__":
    calculate_bmi()