class Contact_list():
    def __init__(self,contacts=[]):
        self.contacts=contacts
        self.i=0
    def add(self,contact):
        self.contacts.append(contact)
    def display(self):
        for self.i in self.contacts:
            print(self.i.name.ljust(25), self.i.email.ljust(20) ,self.i.telephone)