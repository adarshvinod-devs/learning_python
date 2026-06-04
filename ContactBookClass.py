import json

class Contactbook:
  def __init__(self):
    try:
      with open("contacts.json","r") as file:
        self.contacts = json.load(file)
    except FileNotFoundError:
      self.contacts = {}

  def save_contacts(self):
    name = input("\nEnter name to save: ")
    phone_no = input("Enter Phone Number to save: ")
    self.contacts[name] = phone_no
    with open("contacts.json","w") as file:
      json.dump(self.contacts,file)
    print("Contact Saved\n")

  def view_contacts(self):
    for key,value in self.contacts.items():
      print(f"\nName: {key}, Phone No: {value}\n")

  def search_contact(self):
    name = input("Enter name to search: ")
    if name in self.contacts:
      print(f"\nName : {name} Phone No: {self.contacts[name]}\n")
    else:
      print("Contact not found\n")
    

  def delet_contact(self):
    name = input("Enter name to delet: ")
    if name in self.contacts:
      del self.contacts[name]
      print("Contact deleted\n")
      with open("contacts.json","w") as file:
        json.dump(self.contacts,file)
    else:
      print("Contact not found\n")

book = Contactbook()

options = ["1. View Contacts","2. Save Contacts", "3. Search Contacts", "4. Delet Contacts", "5. Exit"]

while True:
  for i in options:
   print(i)

  choice = int(input("\nEnter which function to perform: "))

  match choice:
    case 1:
      book.view_contacts()
    case 2:
      book.save_contacts()
    case 3:
      book.search_contact()
    case 4:
      book.delet_contact()
    case 5:
      break