import random 
import string 

def generate_password():
    #generates a random strong password based on user-specified length 

    print("--Secure Paswword generator--")

    while True:
        try :
            length = int(input("Enter the desired password length : "))
            if length < 4:
                print("For a strong password,please choose a length of 4 or more")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    #define the character sets #combine all the characters we want to choose from into a aingle string.
    all_characters = string.ascii_letters +string.digits + string.punctuation

    #generate the password #use a loop to randomly choose characters one by one 
    password = ''.join(random.choice(all_characters) for i in range(length))

    print("\n Your new secure password is : ")
    print(password)

if __name__ =="__main__":
    generate_password()