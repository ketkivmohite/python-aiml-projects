def slice_email():
    print("---Email Slicer --- ")
    email = input("Please enter your email address : ").strip() #strip removes any accidental spaces 

    try :
        username , domain = email.split('@')

        print("\n --- Sliced Details ---")
        print(f"Your username is : {username}")
        print(f"Your domain is : {domain}")
        print("--------------------------")

    except ValueError:
        print("\nError : Invalid email address . Please make sure to include the '@' symbol. ")


if __name__ == "__main__":
    slice_email()

