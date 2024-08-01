'''MyContacts is a simple contact management application'''

import tkinter as tk
from tkinter import messagebox
import json
import os

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

def add_contact(contacts, name_entry, phone_entry, email_entry, contact_list):
    '''add a new contact'''
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name and phone and email:
        contacts[name] = {'phone': phone, 'email': email}
        messagebox.showinfo("Sucess", f'Contact {name} added successfully')
        save_contacts(contacts)
        view_contacts(contacts, contact_list)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")

def view_contacts(contacts, contact_list):
    '''View all contacts'''
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def delete_contact(contacts, contact_list):
    '''Delete a contact'''
    selected_contact = contact_list.get(tk.ACTIVE) 
    if selected_contact:
        name = selected_contact.split(',')[0].split(':')[1].strip()
        if name in contacts:
            del contacts[name]
            messagebox.showinfo("Sucess", f'Contact {name} deleted successfully!')
            save_contacts(contacts)
            view_contacts(contacts, contact_list)
        else:
            messagebox.showwarning("Not Found", f'Contact {name} not found.')
    else:
        messagebox.showwarning("Selection Error", "Please selec a contact to delete")

contacts = load_contacts()

root = tk.Tk()
root.title("MyContacts")

tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone:").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Button(root, text="Add Contact", command=lambda: add_contact(contacts, name_entry, phone_entry, email_entry, contact_list)).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Delete Contact", command=lambda: delete_contact(contacts, contact_list)).grid(row=4, column=0, columnspan=2)

contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=5, column=0, columnspan=2)

view_contacts(contacts, contact_list)

root.mainloop()
