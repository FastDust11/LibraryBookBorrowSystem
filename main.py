#tytuł, autor, ID
#dodawanie nowych książek
#Pozwala na wypożyczanie książek przez użytkowników (książka staje się niedostępna dla innych)
#rejestr użytkowników imię, nazwisko, ID
from itertools import count
from random import choice
import json

'''
class User:
    def __init__(self, imie, nazwisko, id): #konstruktor co tworzy usera
        self.imie = imie
        self.nazwisko = nazwisko
        self.id = id

class Book:
    def __init__(self, isbn, title, author, count_of_books):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.count_of_books = count_of_books
        self.borrowers = []
'''

users_record = {}
books_record = {}

def display_books():
    for book in books_record.values():
        print(f"ISBN:{book['isbn']}\tTytuł:{book['title']}\tAutor:{book['author']}\tPożyczone:{len(book['borrowers'])}/{book['count_of_books']}")
def search_book():
    pass
def borrow_book():
    isbn = input("Podaj ISBN")
    if isbn not in books_record:
        print("Taki ISBN nie istnieje")
        return
    id = input("Podaj ID Czytelnika")
    if id not in users_record:
        print("Takie ID czytelnika nie istnieje")
        return
    wypozyczone = 0
    for book in books_record.values():
        wypozyczone += book['borrowers'].count(id)
    if wypozyczone >= 5:
        print("Czytelnik wypożyczył już 5 książek")
        return
    if len(books_record[isbn]['borrowers']) >= books_record[isbn]['count_of_books']:
        print("Wypożyczono wszystkie egzemplarze")
        return
    books_record[isbn]['borrowers'].append(id)

def return_book():
    pass
def manage_books():
    display_books()
    print("1.Dodaj/Modyfikuj")
    print("2.Usuń Książkę")
    choice = input()
    if choice == "1":
        isbn = input("Podaj ISBN")
        title = input("Podaj Tytuł")
        author = input("Podaj Autora")
        count_of_books = input("Podaj liczbę sztuk")
        if title == "" or author == "" or isbn == "":
            print("Musisz podać tytuł i autora i isbn")
            return
        if not count_of_books.isdigit():
            print("Podaj liczbę")
        books_record[isbn] = {
            "isbn": isbn,
            "title": title,
            "author": author,
            "count_of_books": int(count_of_books),
            "borrowers": []
        }
    elif choice == "2":
        isbn = input("Podaj ISBN")
        if isbn != "":
            if isbn not in books_record:
                print("Nie ma ksiązki o takim ISBN")
                return
            del books_record[isbn]
        else:
            print("ISBN nie może być puste")
def manage_users():
    for user in users_record.values():
        print(f"id:{user['id']}\timie:{user['imie']}\tnazwisko:{user['nazwisko']}")
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
        users_record[id] = {
            "imie": imie,
            "nazwisko": nazwisko,
            "id": id
        }
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

    with open("ksiazki.json", "w") as f:
        f.write(json.dumps(books_record, indent=4))
    with open("czytelnicy.json", "w") as f:
        f.write(json.dumps(users_record, indent=4))

    return True

def main():
    global books_record
    global users_record
    try:
        with open("ksiazki.json", "r") as f:
            books_record = json.loads(f.read())
        with open("czytelnicy.json", "r") as f:
            users_record = json.loads(f.read())
    except:
        print("Nie ma pliku do odczytania")
    while input_loop():
        pass

main()

