class Library:

    book_list = []
    
    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def view_all_books(cls):
        if not cls.book_list:
            print("\nNo books available in the library yet!")
        else:
            print("\n--- List of All Books ---")
            for book in cls.book_list:
                book.view_book_info()
    
    @classmethod
    def find_book_by_id(cls, book_id):
        for book in cls.book_list:
            if book._Book__book_id == book_id:
                return book
        return None


class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True  
        
        Library.entry_book(self)
    
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"\nBook '{self.__title}' has been borrowed successfully!")
        else:
            print(f"\nError: Book '{self.__title}' is already borrowed.")
    
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"\nBook '{self.__title}' has been returned successfully!")
        else:
            print(f"\nError: Book '{self.__title}' was not borrowed.")
    
    def view_book_info(self):
        availability_status = "Available" 
        if self.__availability:
            pass 
        else:
            availability_status = "Not Available"
        print(f"Book ID: {self.__book_id}, Title: '{self.__title}', Author: {self.__author}, Availability: {availability_status}")
    
    def get_book_id(self):
        return self.__book_id


# Menu-driven system

print("\n--- Welcome to the Library Management System ---")
    
    # Adding some initial books (manual addition)
book1 =  Book(101, "The Great Gatsby", "F. Scott Fitzgerald")
book2 =  Book(104, "The Catcher in the Rye", "J.D. Salinger")
book3 =  Book(103, "1984", "George Orwell")
book4 =  Book(102, "To Kill a Mockingbird", "Harper Lee")
book5 = Book(111, "Python programming", "JON")
book6 = Book(222, "Python for beginner", "Jane Austen")
book7 = Book(333, "Basic to Advanced Python", "Harper Lee")
    
while True:
    print("\nMenu:")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
        
    choice = int(input("Enter your choice : "))
        
    if choice == 1:
        # View all books
        Library.view_all_books()
        
    elif choice == 2:
            # Borrow a book
        try:
            book_id = int(input("\nEnter the Book ID to borrow: "))
            book = Library.find_book_by_id(book_id)
            if book:
                book.borrow_book()
            else:
                print("\nError: Invalid Book ID. Please try again.")
        except ValueError:
            print("\nError: Invalid input! Book ID must be a number.")
        
    elif choice == 3:
        # Return a book
        try:
            book_id = int(input("\nEnter the Book ID to return: "))
            book = Library.find_book_by_id(book_id)
            if book:
                book.return_book()
            else:
                print("\nError: Invalid Book ID. Please try again.")
        except ValueError:
            print("\nError: Invalid input! Book ID must be a number.")
        
    elif choice == 4:
        print("\nGoodbye!")
        break
        
    else:
        print("\nError: Invalid choice! Please select an option between 1 and 4.")


