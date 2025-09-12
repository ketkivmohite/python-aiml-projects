# This will be a list that holds all our contact dictionaries
import json
FILE_NAME = "contacts.json"
def save_contacts():
    with open(FILE_NAME,"w") as file:
        json.dump(contacts,file,indent=4)

def load_contacts():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    

contacts = load_contacts()

def add_contact():
    """Gets user input and adds a new contact dictionary to the list."""
    print("\nPlease enter the details for the new contact:")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")

    # This is the dictionary for the new contact.
    # It stores data in key: value pairs.
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    # Add the new dictionary to our main list
    contacts.append(new_contact)
    save_contacts()
    print(f"\n Contact for '{name}' was added successfully!")

def view_contacts():
    """Displays all contacts in a user-friendly format."""
    if not contacts:
        print("\nYour contact book is empty. Add a contact to get started.")
        return # Exit the function early if there are no contacts

    print("\n---  Your Contacts ---")
    # We loop through the list of dictionaries
    for i, contact in enumerate(contacts, 1):
        # We access the values using their keys (e.g., contact['name'])
        print(f"{i}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print("-----------------------") # A separator for readability

# --- The Main Program Loop ---
while True:
    print("\n===== Contact Book Menu =====")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 3.")