class Contact:
    def __init__(self, name, mobile, email, address, gender, dob):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.address = address
        self.gender = gender
        self.dob = dob
        self.favorite = False

    def display(self):
        print(f"Name     : {self.name}")
        print(f"Mobile   : {self.mobile}")
        print(f"Email    : {self.email}")
        print(f"Address  : {self.address}")
        print(f"Gender   : {self.gender}")
        print(f"DOB      : {self.dob}")
        print(f"Favorite : {'Yes' if self.favorite else 'No'}")
        print("-" * 30)


class ContactManager:

    def __init__(self):
        self.contacts = []

    # 1. Add Contact
    def add_contact(self):
        name = input("Enter Name: ")
        mobile = input("Enter Mobile Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        gender = input("Enter Gender: ")
        dob = input("Enter Date of Birth: ")

        contact = Contact(name, mobile, email, address, gender, dob)
        self.contacts.append(contact)

        print("Contact added successfully!")

    # 2. Update Contact
    def update_contact(self):
        old_mobile = input("Enter old mobile number: ")

        for contact in self.contacts:
            if contact.mobile == old_mobile:

                print("1. Update Name")
                print("2. Update Mobile")
                print("3. Update Email")
                print("4. Update Address")
                print("5. Update Gender")
                print("6. Update DOB")

                choice = input("Enter choice: ")

                if choice == "1":
                    contact.name = input("Enter new name: ")

                elif choice == "2":
                    contact.mobile = input("Enter new mobile: ")

                elif choice == "3":
                    contact.email = input("Enter new email: ")

                elif choice == "4":
                    contact.address = input("Enter new address: ")

                elif choice == "5":
                    contact.gender = input("Enter new gender: ")

                elif choice == "6":
                    contact.dob = input("Enter new DOB: ")

                else:
                    print("Invalid choice!")
                    return

                print("Contact updated successfully!")
                return

        print("Contact not found!")

    # 3. List Contacts
    def list_contacts(self):

        if len(self.contacts) == 0:
            print("No contacts available!")

        else:
            print("\n===== List of Contacts =====")

            for contact in self.contacts:
                contact.display()

    # 4. Delete Contact
    def delete_contact(self):

        name = input("Enter name to delete: ")

        for contact in self.contacts:

            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)

                print("Contact deleted successfully!")
                return

        print("Contact not found!")

    # 6. Search Contact
    def search_contact(self):

        search = input("Enter name or mobile number to search: ")

        found = False

        for contact in self.contacts:

            if (search.lower() in contact.name.lower()
                    or search in contact.mobile):

                contact.display()
                found = True

        if not found:
            print("Contact not found!")

    # 7. Favorite Contact
    def favorite_contact(self):

        mobile = input("Enter mobile number: ")

        for contact in self.contacts:

            if contact.mobile == mobile:

                contact.favorite = not contact.favorite

                if contact.favorite:
                    print("Contact added to favorites!")
                else:
                    print("Contact removed from favorites!")

                return

        print("Contact not found!")

    # 8. List Favorite Contacts
    def list_favorites(self):

        found = False

        print("\n===== Favorite Contacts =====")

        for contact in self.contacts:

            if contact.favorite:
                contact.display()
                found = True

        if not found:
            print("No favorite contacts!")


# Object creation
manager = ContactManager()


# Main Menu
while True:

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")

    print("1. Add Contact")
    print("2. Update Contact")
    print("3. List Contacts")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Add/Remove Favorite")
    print("7. List Favorite Contacts")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        manager.add_contact()

    elif choice == "2":
        manager.update_contact()

    elif choice == "3":
        manager.list_contacts()

    elif choice == "4":
        manager.delete_contact()

    elif choice == "5":
        manager.search_contact()

    elif choice == "6":
        manager.favorite_contact()

    elif choice == "7":
        manager.list_favorites()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
