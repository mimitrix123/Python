"""Week 4 Practice 1: Contact Book using a dictionary."""


def main():
    contacts = {}
    while True:
        print("\n1.Add  2.Search  3.Update  4.Delete  5.Show All  6.Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            contacts[name] = phone
            print("Contact saved.")
        elif choice == "2":
            name = input("Name: ").strip()
            print("Phone:", contacts.get(name, "Contact not found."))
        elif choice == "3":
            name = input("Name: ").strip()
            if name in contacts:
                contacts[name] = input("New phone: ").strip()
                print("Contact updated.")
            else:
                print("Contact not found.")
        elif choice == "4":
            name = input("Name: ").strip()
            print("Deleted." if contacts.pop(name, None) is not None else "Contact not found.")
        elif choice == "5":
            for name, phone in sorted(contacts.items()):
                print(f"{name}: {phone}")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
