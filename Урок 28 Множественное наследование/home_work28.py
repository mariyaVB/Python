# -------------------------------------------------- Задача -----------------------------------------------------------
# создать систему для управления библиотекой. Вам нужно реализовать следующие классы:
# 	Book (Книга):
# ●	Свойства: название, автор, год издания, жанр, количество экземпляров.
# ●	Методы: вывод информации о книге, уменьшение/увеличение количества экземпляров.
# 	Library (Библиотека):
# ●	Свойства: список книг, список пользователей.
# ●	Методы: добавление/удаление книг, регистр./удаление пользователя, выдача/возврат книги, вывод списка доступных книг.
# 	User (Пользователь):
# ●	Свойства: имя, ID, список взятых книг.
# ●	Методы: вывод информации о пользователе, взятие/возврат книги.
# 	Transaction (Транзакция):
# ●	Свойства: дата, тип (выдача/возврат), книга, пользователь.
# ●	Методы: запись транзакции, вывод информации о транзакции.
#
# Требования:
# ●	Каждый класс должен иметь конструктор для инициализации объектов.
# ●	Методы классов должны быть реализованы так, чтобы обеспечивать безопасность данных и взаимодействие между объектами.
# ●	Классы должны взаимодействовать друг с другом в рамках системы управления библиотекой.

from library import *
from user import *
from book import *
from transaction import *

main_menu = 1
transaction = Transaction()
library = Library()
library.add_registration(User('Мария'))
library.add_books(Book('Мартин Иден', 'Джек Лондон', '1908', 'Роман', 2),
                  Book('Портрет Дориана Грея', 'Оскар Уайльд', '1891', 'Роман', 2))
while main_menu == 1:

    while True:
        command = input('''
                            Режим пользователя 1
                            Режим библиотекарь 2
                            Выход 0
                            Введите цифру соответствующего пункта ______
        ''')
        match command:
            case '0':
                main_menu = 0
                break

            case '1':
                chapter = input('''
                            Вы зашли в Пользователя:
                            1 Регистрация
                            2 Посмотреть доступные книги
                            3 Взять книгу
                            4 Вернуть книгу
                            5 Удалить аккаунт
                            6 Вернуться в главное меню 
                            0 Выход
                            Введите цифру соответствующего пункта _____
                            ''')

                match chapter:
                    case '0':
                        main_menu = 0
                        break

                    case '6':
                        main_menu = 0

                    case '1':
                        library.add_registration(registration())
                        while True:
                            add = input('Добавить еще пользователя? 1 = Да 0 = Нет ')
                            if add == '1':
                                library.add_registration(registration())
                            elif add == '0':
                                break

                    case '2':
                        library.show_book()

                    case '3':
                        desired_book = library.get_book(find_book())
                        desired_user = library.get_user(find_registration())
                        desired_user.take_a_book(desired_book)
                        desired_book.reduce_book(1)
                        transaction.write_transaction('Выдана', desired_user.name, desired_book.title)
                        transaction.show_transaction()

                    case '4':
                        desired_book = library.get_book(find_book())
                        desired_user = library.get_user(find_registration())
                        desired_user.return_a_book(desired_book)
                        desired_book.add_book(1)
                        transaction.write_transaction('Возвращена', desired_user.name, desired_book.title)
                        transaction.show_transaction()

                    case '5':
                        library.delete_registration(find_registration())
                        while True:
                            add = input('Удалить еще пользователя? 1 = Да 0 = Нет ')
                            if add == '1':
                                library.delete_registration(find_registration())
                            elif add == '0':
                                break

                    case '6':
                        pass

            case '2':
                chapter = input('''
                            Вы зашли в Библиотекаря:
                            1 Посмотреть список пользователей
                            2 Посмотреть список книг
                            3 Добавить новую книгу в базу
                            4 Удалить книгу из базы
                            5 Вернуться в главное меню 
                            0 Выход
                            Введите цифру соответствующего пункта _____
                            ''')

                match chapter:
                    case '0':
                        main_menu = 0
                        break

                    case '5':
                        main_menu = 0

                    case '1':
                        library.show_person()

                    case '2':
                        library.show_book()

                    case '3':
                        library.add_books(redaction_book())
                        while True:
                            add = input('Добавить еще книгу? 1 = Да 0 = Нет ')
                            if add == '1':
                                library.add_books(redaction_book())
                            elif add == '0':
                                break

                    case '4':
                        library.delete_book(find_book())
                        while True:
                            add = input('Удалить еще книгу? 1 = Да 0 = Нет ')
                            if add == '1':
                                library.delete_book(find_book())
                            elif add == '0':
                                break