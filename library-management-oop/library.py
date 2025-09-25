class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"'{self.title}' by {self.author}, published in {self.year}")

class User:
    def __init__(self, firstname, lastname, user_id):
        self.firstname = firstname
        self.lastname = lastname
        self.user_id = user_id

    def display_user(self):
        print(f"User: {self.firstname} {self.lastname}, ID: {self.user_id}")

class Librarian(User):
    def __init__(self, firstname, lastname, user_id):
        super().__init__(firstname, lastname, user_id)
        self.books_added = []

    def add_book(self, book):
        self.books_added.append(book)
        print(f"Librarian {self.firstname} {self.lastname} added the book:")
        book.display_info()

class Member(User):
    def __init__(self, firstname, lastname, user_id):
        super().__init__(firstname, lastname, user_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.firstname} {self.lastname} borrowed the book:")
        book.display_info()

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.firstname} {self.lastname} returned the book:")
            book.display_info()
        else:
            print(f"{self.firstname} {self.lastname} does not have this book borrowed.")

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

librarian = Librarian("Aarav", "Mehta", 101)
member1 = Member("Rahul", "Kumar", 202)
member2 = Member("Kavya", "Iyer", 203)

librarian.add_book(book1)
librarian.add_book(book2)

member1.borrow_book(book1)
member2.borrow_book(book2)

member1.return_book(book1)
member1.return_book(book2)  # Trying to return a book not borrowed

