#tytuł, autor, ID
#dodawanie nowych książek
#Pozwala na wypożyczanie książek przez użytkowników (książka staje się niedostępna dla innych)
#rejestr użytkowników imię, nazwisko, ID
from itertools import count
from random import choice


class User:
    def __init__(self, imie, nazwisko, id): #konstruktor co tworzy usera
        self.imie = imie
        self.nazwisko = nazwisko
        self.id = id

class Book:
    def __init__(self, tittle, author, isbn, count_of_books):
        self.tittle = tittle
        self.autor = author
        self.isbn = isbn
        self.count_of_books = count_of_books
        self.borrowers = []


users_record = {}
books_record = {}

def display_books():
    pass
def search_book():
    pass
def borrow_book():
    pass
def return_book():
    pass
def manage_books():
    for book in books_record.values():
        print(f"ISBN:{book.isbn}\tTytuł:{book.tittle}\tAutor:{book.author}\tPożyczone:{len(book.borrowers)}/{book.count_of_books}")
    print("1. Dodaj/Modyfikuj")
    print("2.Usuń Książkę")
    choice = input()
    if choice == "1":
        isbn = input("Podaj ISBN")
        tittle = input("Podaj Tytuł")
        author = input("Podaj Autora")
        count_of_books = input("Podaj liczbę sztuk")
        if tittle == "" or author == "" or isbn == "":
            print("Musisz podać tytuł i autora i isbn")
            return
        books_record[isbn] = Book(isbn, tittle, author, count_of_books)
    elif choice == "2":
        pass
def manage_users():
    for user in users_record.values():
        print(f"id:{user.id}\timie:{user.imie}\tnazwisko:{user.nazwisko}")
    print("1. Dodaj/Modyfikuj 2.Usuń Użytkownika")
    choice = input()
    if choice == "1":
        id = input("Podaj ID, jeśli chcesz nadpisać użytkownika, pozostaw puste przy tworzeniu nowego")
        imie = input("Podaj Imię")
        nazwisko = input("Podaj Nazwisko")
        if id == "":
            i = 1
            while (str(i) in users_record):
                i += 1
            id = str(i)
        else:
            if id not in users_record:
                print("Nie ma użytkownika o takim ID")
                return
        if imie == "" or nazwisko == "":
            print("Użytkownik musi mieć imię i nazwisko")
            return
        users_record[id] = User(imie, nazwisko, id)
    elif choice == "2":
        id = input("Podaj ID")
        if id != "":
            if id not in users_record:
                print("Nie ma użytkownika o takim ID")
                return
            del users_record[id]
        else: print("ID nie może być puste")
def input_loop():
    print("1. Display Books")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Manage Books") #dodawać/usuwać/modyfikować
    print("6. Manage Users") #dodawać/usuwać/modyfikować
    print("7. Exit")

    choice = input("Wybierz cyfrę: ")
    if choice == "1":
        display_books()
    elif choice == "2":
        search_book()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        manage_books()
    elif choice == "6":
        manage_users()
    elif choice == "7":
        return False
    else:
        print("Taka opcja nie istnieje, wybierz poprawną cyfrę")

    return True

def main():
    while input_loop():
        pass






main()

