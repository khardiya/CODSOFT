import tkinter as tk
from tkinter import messagebox
import os

CONTACTS_FILE = 'contacts.txt'


def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    store_name, phone_number, email, address = line.strip().split(',')
                    contact = {
                        'store_name': store_name,
                        'phone_number': phone_number,
                        'email': email,
                        'address': address
                    }
                    contacts.append(contact)
    return contacts


def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        for contact in contacts:
            f.write(f"{contact['store_name']},{contact['phone_number']},{contact['email']},{contact['address']}\n")


class ContactManager:
    def __init__(self, root):
        self.contacts = load_contacts()
        self.root = root
        self.root.title("Contact Management System")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.store_name_label = tk.Label(self.frame, text="Store Name:")
        self.store_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.store_name_entry = tk.Entry(self.frame)
        self.store_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_number_label = tk.Label(self.frame, text="Phone Number:")
        self.phone_number_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_number_entry = tk.Entry(self.frame)
        self.phone_number_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(self.frame, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(self.frame, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.frame)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, columnspan=2, pady=10)

        self.search_label = tk.Label(self.frame, text="Search:")
        self.search_label.grid(row=5, column=0, padx=10, pady=5)
        self.search_entry = tk.Entry(self.frame)
        self.search_entry.grid(row=5, column=1, padx=10, pady=5)

        self.search_button = tk.Button(self.frame, text="Search", command=self.search_contacts)
        self.search_button.grid(row=6, columnspan=2, pady=10)

        self.contacts_listbox = tk.Listbox(self.frame, width=50)
        self.contacts_listbox.grid(row=7, columnspan=2, pady=10)
        self.contacts_listbox.bind('<<ListboxSelect>>', self.on_select)

        self.edit_button = tk.Button(self.frame, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=8, column=0, pady=10)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=1, pady=10)

        self.display_contacts()

    def add_contact(self):
        store_name = self.store_name_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if store_name and phone_number and email and address:
            contact = {
                'store_name': store_name,
                'phone_number': phone_number,
                'email': email,
                'address': address
            }

            self.contacts.append(contact)
            save_contacts(self.contacts)
            self.display_contacts()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def display_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['store_name']} - {contact['phone_number']}")

    def clear_entries(self):
        self.store_name_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def search_contacts(self):
        query = self.search_entry.get().lower()
        filtered_contacts = [
            contact for contact in self.contacts if
            query in contact['store_name'].lower() or query in contact['phone_number']
        ]
        self.contacts_listbox.delete(0, tk.END)
        for contact in filtered_contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['store_name']} - {contact['phone_number']}")

    def on_select(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]
            self.store_name_entry.delete(0, tk.END)
            self.store_name_entry.insert(tk.END, contact['store_name'])
            self.phone_number_entry.delete(0, tk.END)
            self.phone_number_entry.insert(tk.END, contact['phone_number'])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, contact['email'])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(tk.END, contact['address'])

    def edit_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.contacts[index] = {
                'store_name': self.store_name_entry.get(),
                'phone_number': self.phone_number_entry.get(),
                'email': self.email_entry.get(),
                'address': self.address_entry.get()
            }
            save_contacts(self.contacts)
            self.display_contacts()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "No contact selected!")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            save_contacts(self.contacts)
            self.display_contacts()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "No contact selected!")


root = tk.Tk()
app = ContactManager(root)
root.mainloop()
