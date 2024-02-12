# 	User (Пользователь):
# ●	Свойства: имя, ID, список взятых книг.
# ●	Методы: вывод информации о пользователе, взятие/возврат книги.

from book import *
import random
import string


class User:

    def __init__(self, name: str):
        self.name = self.check_name(name)
        self.user_id = self.create_id()
        self.borrowed_books = []

    @staticmethod
    def create_id():
        user_id = random.choice(string.ascii_letters) + str(random.randint(1000, 9999))
        return user_id

    @staticmethod
    def check_name(name):
        if type(name) is str:
            if not name.isdigit():
                return name
        raise 'Name is not str'

    def show_info_user(self):
        print(f'Имя: {self.name}  |  ID: {self.user_id}  |  Список взятых книг: {self.show_list_book()}.\n')

    def show_list_book(self):
        a = []
        for book in self.borrowed_books:
            a.append(f'{book.title} - {book.author}')
        return a

    def take_a_book(self, *books):
        for book in books:
            if type(book) is not Book:
                raise 'book is not class Book'
            self.borrowed_books.append(book)

    def return_a_book(self, *books):
        for book in books:
            if type(book) is not Book:
                raise 'book is not class Book'
            self.borrowed_books.remove(book)

    def __str__(self):
        return f'Имя: {self.name}  |  ID: {self.user_id}  |  Список взятых книг: {self.show_list_book()}.\n'


# book1 = Book('a', 'a', 'a', 'a', 2)
# book2 = Book('z', 'z', 'z', 'z', 2)
# user = User('M')
# user.take_a_book(book1)
# user.take_a_book(book2)
# # print(user.show_list_book())
# user.show_info_user()