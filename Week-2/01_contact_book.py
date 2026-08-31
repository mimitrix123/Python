"""Week 2 Assignment 1: Contact Book using a dictionary."""


def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contacts:
        print("Contact already exists. Use update instead.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
    else:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input(f"New phone [{contacts[name]['phone']}]: ").strip()
    email = input(f"New email [{contacts[name]['email']}]: ").strip()
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    print("Contact updated successfully.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if contacts.pop(name, None) is not None:
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def show_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for name, details in sorted(contacts.items()):
        print(f"{name}: {details['phone']} | {details['email']}")


def main():
    contacts = {}
    actions = {"1": add_contact, "2": search_contact, "3": update_contact, "4": delete_contact}
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add\n2. Search\n3. Update\n4. Delete\n5. Show All\n6. Exit")
        choice = input("Choose an option: ").strip()
        if choice in actions:
            actions[choice](contacts)
        elif choice == "5":
            show_contacts(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
