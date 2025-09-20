import time 
def countdown():
    
    while True :
        try :
            seconds = int(input("Enter the time in seconds : "))
            if seconds > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\nStarting countdown...")

    while seconds > 0:
        print(seconds)

        time.sleep(1)

        seconds -= 1
    print("\n Time's Up")

if __name__ == "__main__":
    countdown()
