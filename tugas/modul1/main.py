users = {
    "username": ["admin", "john", "doe"],
    "books": ["Naruto", "One Piece", "Dragon Ball", "Captain Tsubatsa", "Kisah cinta kita"]
}

takenBy = {
    "user": ["john", "doe", "john"],
    "books": ["Kisah Nabi", "101 Malam", "Spongebob Adventure"]
}

def menu():
    print("=== MENU ===\n 1. Login\n")

def login():
    print("=== LOGIN ===\n 1. Login\n 2. Exit\n")
    menu_choice = input("\nPilih menu: ")
    if menu_choice == '1':
        username = input("Masukkan username Anda: ")
        userDB(username)
    elif menu_choice == '2':
        exit()
    else:
        login()

def dashboardAdmin():
    print("\nADMINISTRATOR DASHBOARD")
    print("=== ADMIN ===\n 1. Add books\n 2. View Books Available\n 3. Login other user \n 4. Exit Program\n")
    menu_choice = input("\nMasukkan menu: ")
    if menu_choice == '1':
        addBooks(input("\nMasukkan judul buku: "))
    elif menu_choice == '2':
        listBook()
    elif menu_choice == '3':
        login()
    elif menu_choice == '4':
        exit()
    dashboardAdmin()

def listBook():
    print("\nList buku tersedia")
    books = users.get("books")
    for i, book in enumerate(books):
        print(f"{i}. {book.lower()}") 

def dashboardUser(name):
    print("\nWelcome User " + name + "!")
    print("=== USER ===\n 1. Get books on library\n 2. Return books\n 3. View my Books\n 0. Login other account")

    menu_choice = input("\nMasukkan menu: ")
    if menu_choice == '1':
        listBook()
        book_index = input("Masukkan nomor buku: ")
        userGet(name, book_index)
        dashboardUser(name)
    elif menu_choice == '2':
        listMyBooks(name)
        book = input("\nMasukkan nomor buku yang akan dikembalikan: ")
        returnBook(name, book)
    elif menu_choice == '3':
        viewMyBooks(name)
        dashboardUser(name)
    elif menu_choice == '0':
        login()
    else:
        print("Menu tidak tersedia!")
        dashboardUser(name)

def listMyBooks(name):
    print("\nMy Books:")
    user_books = getBooksByUser(name)
    for i, book in enumerate(user_books):
        print(f"{i}. {book.lower()}")

def viewMyBooks(name):
    print("\nMy Books:")
    user_books = getBooksByUser(name)
    for i, book in enumerate(user_books):
        print(f"{i}. {book.lower()}")

def getBooksByUser(username):
    user_books = []
    for i, user in enumerate(takenBy["user"]):
        if user == username:
            user_books.append(takenBy["books"][i])
            i += 1 
    return user_books


def userGet(name, book_index):
    books = users.get("books")
    if book_index.isdigit():
        book_index = int(book_index)
        if 0 <= book_index < len(books):
            book = books[book_index]
            users["books"].remove(book)
            takenBy["user"].append(name)
            takenBy["books"].append(book)
            print(f"\nAnda telah mengambil buku '{book}' dari perpustakaan.")
        else:
            print("\nNomor buku tidak valid.")
    else:
        print("\nMasukkan nomor buku yang valid.")

def returnBook(name, book):
    if book.isdigit():
        book_index = int(book)
        if 0 <= book_index < len(takenBy["books"]):
            returned_book = takenBy["books"].pop(book_index) 
            returned_user = takenBy["user"].pop(book_index) 
            users["books"].append(returned_book) 
            print(f"\nAnda telah mengembalikan buku '{returned_book}' ke perpustakaan.")
        else:
            print("\nPilihan buku tidak valid atau buku tidak ditemukan.")
    else:
        print("\nPilihan buku tidak valid.")
    dashboardUser(name)



def addBooks(name):
    users["books"].append(name)
    print("\nSukses input buku " + name)
    print(users.get("books"))
    print("\n")

def userDB(username):
    check = users.get("username")
    if username == check[0]:
        dashboardAdmin()
    elif username == check[1]:
        dashboardUser(check[1])
    elif username == check[2]:
        dashboardUser(check[2])
    else:
        print("Username Anda tidak ditemukan")
        return login()

login()
