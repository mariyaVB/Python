# Library (Библиотека):
# ●	Свойства: список книг, список пользователей.
# ●	Методы: добавление/удаление книг, регистр./удаление пользователя, выдача/возврат книги, вывод списка доступных книг.

from book import Book
from user import User


class Library:
    def __init__(self):
        self.books = []
        self.person = []

    def show_person(self):
        for el in self.person:
            print(el)

    def show_book(self):
        for el in self.books:
            print(el)

    def add_registration(self, *new_person):
        for pers in new_person:
            if type(pers) is not User:
                raise 'Not is User'
            self.person.append(pers)

    def delete_registration(self, del_person):
        for pers in self.person:
            if pers.user_id == del_person:
                key = self.person.index(pers)
                del self.person[key]

    def add_books(self, *new_book):
        for book in new_book:
            if type(book) is not Book:
                raise 'Not is Book'
            self.books.append(book)

    def delete_book(self, del_book):
        for book in self.books:
            if book.title == del_book:
                key = self.books.index(book)
                del self.books[key]

    def get_book(self, desired_book):
        for book in self.books:
            if book.title == desired_book:
                return book

    def get_user(self, desired_user):
        for pers in self.person:
            if pers.user_id == desired_user:
                return pers


def registration():
    name = input('Введите свое имя: _____')
    user = User(name)
    print(f'Регистрация завершена. {user}')
    return user


def find_registration():
    name_id = input('Укажите ваш ID: _____')
    return name_id


def redaction_book():
    title = input('Введите название книги: _____')
    author = input('Введите автора: _____')
    year = input('Введите год издания: _____')
    genre = input('Введите жанр: _____')
    count = int(input('Введите количество: _____'))
    book = Book(title, author, year, genre, count)
    return book


def find_book():
    title = input('Название книги: _____')
    return title





