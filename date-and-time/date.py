# The `datetime` library helps us work with dates and times.
import datetime

def display_current_time():
    """
    Gets the current date and time and displays it in a formatted way.
    """
    print("---  Digital Clock ---")

    # Get the current moment (date and time)
    now = datetime.datetime.now()

    # --- This is the key part ---
    # Format the time into a clean "Hour:Minute:Second" string
    # %H = Hour (24-hour), %M = Minute, %S = Second
    current_time = now.strftime("%H:%M:%S")
    
    # Format the date into a clean "Year-Month-Day" string
    # %Y = Year, %m = Month, %d = Day
    current_date = now.strftime("%Y-%m-%d")

    # Print the results
    print(f"\nCurrent Time: {current_time}")
    print(f"Current Date: {current_date}")
    print("-------------------------")


# --- Run the main function ---
if __name__ == "__main__":
    display_current_time()
