import os

def clear():
    os.system("clear")

name = []
number = []
email = []
clear()
while True:
 def add():
    name1 = input("Enter name: ")
    number1 = input("Enter phone number: ")
    email1 = input("Enter email: ")
    
    name.append(name1)
    number.append(number1)
    email.append(email1)

 def delete():
    i= int(input("Enter the index of contact to delete: ")) - 1
    if 0 <= i < len(name):
        del name[i]
        del number[i]
        del email[i]
        print("Contact deleted.")
    else:
        print("Invalid index.")

 def display():
    if not name:
        print("No contacts to display.")
    else:
        print("Contacts:")
        for i in range(len(name)):
            print(f"{i+1}. Name: {name[i]}, Phone: {number[i]}, Email: {email[i]}")


 print() 
 print("1. Add Contact")
 print("2. Delete Contact")
 print("3. Display Contacts")
 print("4. Clear Console")
 print("5. Quit")
 print()
    
 choice = input("Enter your choice: ")
    
 if choice == "1":
        add()
       
 elif choice == "2":
        delete()
      
 elif choice == "3":
        display()
                
 elif choice == "4":
        clear()
        
 elif choice == "5":
        print("Stopped")
        break
