class book:
    def __init__(self , name):
        self.name = name
        self.available = True

class lilbrary:
    def __init__(self):
        self.books = {}

    def add_book(self):
        name = print("Enter the name of the book:")
        self.books[name]=book[name]

    def borrow_book(self):
        name = input("enter book's name to borrow:")

        if name in self.books:
            if self.books[name].available:
                self.books[name].available = False
     
                print("book borrowed")
                
            else:
            
                print("Book is already borrowed")
                
        else:
            print("Book not found") 

            def display_books(self):
                print("books in library")
                for book in self.books.values():
                    if book.available:
                        print(book.name,"available")

                    else:
                        print(book.name,"borrowed")

Library = Library()

while True:
    print("library management system")
    print("1.add book")
    print("2.borrow book")
    print("3.return book")
    print("4.display books")
    print("5.exit")

    choice = int(input("enter your choice"))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.borrow_book()
    elif choice == 3:
        lilbrary.return_book()
    elif choice == 4:
        library.display_books()
    elif choice == 5:
         print("Thank You !")
         break 
    else:
        print("Invalid choice")
    


        
    
