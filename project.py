import json   #used to store structured data like books and members in our program
import os      #allows us to interact with the operating system
import time
# Initialize empty dictionaries to store books and members
books = {}   #keys are book titles and values are details like the author and availability
members = {}   #keys are unique member IDs, and the values are details like the member's name and borrowed books

# File names for storing data
BOOKS_FILE = "books.json"     
MEMBERS_FILE = "members.json"

# Load existing data from files
def load_data():
    global books, members
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r') as f:
            books = json.load(f)
    if os.path.exists(MEMBERS_FILE):
        with open(MEMBERS_FILE, 'r') as f:
            members = json.load(f)

# Save data to files
def save_data():
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f)
    with open(MEMBERS_FILE, 'w') as f:
        json.dump(members, f)

# Function to add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    books[title] = {"author": author, "available": True}
    print(f"Book '{title}' added successfully.")

# Function to delete a book
def delete_book():
    title = input("Enter book title to delete: ")   #using nested dictionaries 
    if title in books:
        del books[title]
        print(f"Book '{title}' deleted successfully.")
    else:
        print("Book not found.")

# Function to check if a book exists
def check_book():
    title = input("Enter book title to check: ")     
    if title in books:
        status = "available" if books[title]["available"] else "borrowed"
        print(f"Book '{title}' exists and is currently {status}.")
    else:
        print("Book not found.")

# Function to register a member
def register_member():
    name = input("Enter member name: ")   # a unique ID based on the current number of members
    member_id = str(len(members) + 1)
    members[member_id] = {"name": name, "books": []}
    print(f"Member '{name}' registered with ID: {member_id}")

# Function to borrow a book
def borrow_book():
    member_id = input("Enter member ID: ")
    if member_id not in members:
        print("Member not found.")
        return                  #For exiting 

    title = input("Enter book title to borrow: ")
    if title not in books:
        print("Book not found.")
        return

    if not books[title]["available"]:  #checks if the book is available by looking at the available key of the book’s entry in the books dictionary
        print("Book is already borrowed.")   
        return

    books[title]["available"] = False
    members[member_id]["books"].append(title)
    print(f"Book '{title}' borrowed successfully by member {member_id}.")

# Function to return a book
def return_book():
    member_id = input("Enter member ID: ")
    if member_id not in members:
        print("Member not found.")
        return

    title = input("Enter book title to return: ")
    if title not in books:
        print("Book not found.")
        return

    if title not in members[member_id]["books"]:
        print("This book was not borrowed by this member.")
        return

    books[title]["available"] = True
    members[member_id]["books"].remove(title)
    print(f"Book '{title}' returned successfully by member {member_id}.")

# Function to display all books
def display_books():
    if not books:
        print("No books in the library.")   #books = {Atomic Habits:{author: James Clear, status: available}, the subtle art of not giving a fu*k:{author:xyz, status: borrowed}}  
    else:
        print("Books in the library:")
        for title, info in books.items(): #it loops through each book in the books dictionary using for title, info in books.items()
            status = "Available" if info["available"] else "Borrowed"
            print(f"- {title} by {info['author']} ({status})") 

# Function to display all members
def display_members():
    if not members:
        print("No registered members.")
    else:
        print("Registered members:")
        for member_id, info in members.items():  #.items() returns each (key, value) pair from the dictionary
            print(f"- ID: {member_id}, Name: {info['name']}, Books borrowed: {', '.join(info['books'])}")

# Main menu function
def main_menu():
    while True:
        print("\nLibrary Management System")
        time.sleep(3)
        print("Project by Abdullah, Wania, Mustafa, Mubarra, Sufyan")
        time.sleep(3)
        print("1. Add a Book")
        time.sleep(1)
        print("2. Delete a Book")
        time.sleep(1)
        print("3. Check if a Book Exists")
        time.sleep(1)
        print("4. Register a Member")
        time.sleep(1)
        print("5. Borrow a Book")
        time.sleep(1)
        print("6. Return a Book")
        time.sleep(1)
        print("7. Display All Books")
        time.sleep(1)
        print("8. Display All Members")
        time.sleep(1)
        print("9. Save and Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            delete_book()
        elif choice == '3':
            check_book()
        elif choice == '4':
            register_member()
        elif choice == '5':
            borrow_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            display_books()
        elif choice == '8':
            display_members()
        elif choice == '9':
            save_data()
            print("Data saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":  #Ensures the script runs only when executed directly, not when imported.
    load_data()
    main_menu()
