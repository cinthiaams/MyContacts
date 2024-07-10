'''MyContacts is a simple contact management application'''

import json
import os
import time

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    '''Load contacts from the JSON file'''
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    '''Save contacts to the JSON file'''
    with open(CONTACTS_FILE, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    '''add a new contact'''
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f'\nContact {name} added successfully!')

def view_contacts(contacts):
    '''View all contacts'''
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("\nNo contacts available")

def update_contact(contacts):
    '''Update an existing contact'''
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f'\nContact {name} update successfully!')
    else:
        print(f'\nContact {name} not found.')

def delete_contact(contacts):
    '''Delete a contact'''
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f'\nContact {name} deleted successfully!')
    else:
        print(f'\nContact {name} not found.')

def search_contacts(contacts):
    '''Search for contacts by name'''
    search_name = input("Enter the name to search for: ")
    found_contacts = {
        name: info
        for name, info in contacts.items()
        if search_name.lower() in name.lower()
    }
    if found_contacts:
        for name, info in found_contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("\nNo contacts found.")

def menu():
    '''Main function to run the contact manager.'''
    contacts = load_contacts()

    print("\n+---------------------------------+")
    print("|            Welcome to           |")
    print("|            MY CONTACTS          |")
    print("| Your app for contact management |")
    print("+---------------------------------+")

    while True:
        time.sleep(1)  # Add a 1-second delay before showing the menu
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. Exit")

        choice = input("Enter the number of your chosen option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            search_contacts(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
