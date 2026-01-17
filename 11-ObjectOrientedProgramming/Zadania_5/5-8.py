class Contact():
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"{self.name:15} {self.email:20} {self.telephone}"
    


class ContactList():
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        print("CONTACT LIST")
        print("-" * 50)
        for contact in self.contacts:
            print(contact)



def main():
    phone_contacts = ContactList()

    phone_contacts.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    phone_contacts.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    phone_contacts.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    phone_contacts.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    phone_contacts.display_contacts()


if __name__ == "__main__":
    main()