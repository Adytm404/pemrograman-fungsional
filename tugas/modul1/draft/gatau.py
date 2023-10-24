class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.books_borrowed = []

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.users = {}
        self.books = []

    def add_user(self, username, role):
        self.users[username] = User(username, role)

    def login(self, username):
        return self.users.get(username)

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def view_available_books(self):
        available_books = [book for book in self.books if book.available]
        return available_books

    def borrow_book(self, user, book_title):
        for book in self.books:
            if book.title == book_title and book.available:
                book.available = False
                user.books_borrowed.append(book)
                return True
        return False

    def return_book(self, user, book_title):
        for book in user.books_borrowed:
            if book.title == book_title:
                book.available = True
                user.books_borrowed.remove(book)
                return True
        return False

def main():
    library = Library()

    library.add_user("admin", "admin")
    library.add_user("mahasiswa1", "mahasiswa")
    library.add_user("mahasiswa2", "mahasiswa")

    library.add_book("Book1", "Author1")
    library.add_book("Book2", "Author2")
    library.add_book("Book3", "Author3")

    while True:
        print("\n=== LOGIN ===")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            user = library.login(username)

            if user:
                while True:
                    print("\n=== {} ===".format(user.role.upper()))
                    if user.role == "admin":
                        print("1. Add books")
                        print("2. View Books Available")
                        print("3. Login other user")
                    elif user.role == "mahasiswa":
                        print("1. Get books on library")
                        print("2. Return books")
                        print("3. View my Books")

                    print("0. Login other account")

                    choice = input("Enter your choice: ")

                    if choice == "0":
                        break
                    elif choice == "1":
                        if user.role == "admin":
                            title = input("Enter book title: ")
                            author = input("Enter author: ")
                            library.add_book(title, author)
                            print("Book added successfully!")
                        elif user.role == "mahasiswa":
                            print("Available Books:")
                            available_books = library.view_available_books()
                            if not available_books:
                                print("No books available.")
                            else:
                                for i, book in enumerate(available_books):
                                    print("{}. {} by {}".format(i + 1, book.title, book.author))
                                book_choice = int(input("Enter the number of the book you want to borrow: ")) - 1
                                if 0 <= book_choice < len(available_books):
                                    if library.borrow_book(user, available_books[book_choice].title):
                                        print("Book borrowed successfully!")
                                    else:
                                        print("Book not available or already borrowed.")
                    elif choice == "2":
                        if user.role == "mahasiswa":
                            if not user.books_borrowed:
                                print("You have no books to return.")
                            else:
                                print("Your Borrowed Books:")
                                for i, book in enumerate(user.books_borrowed):
                                    print("{}. {} by {}".format(i + 1, book.title, book.author))
                                book_choice = int(input("Enter the number of the book you want to return: ")) - 1
                                if 0 <= book_choice < len(user.books_borrowed):
                                    if library.return_book(user, user.books_borrowed[book_choice].title):
                                        print("Book returned successfully!")
                                    else:
                                        print("Book not found.")
                        else:
                            print("Invalid choice.")
                    elif choice == "3":
                        pass
                    else:
                        print("Invalid choice.")
            else:
                print("Invalid username.")
        elif choice == "2":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
