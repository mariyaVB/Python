# ---------------------------------------------- Задача --------------------------------------------------------------
# Создать класс Book с атрибутами title, author, status ("в наличии" или "выдана") и методом display_info(),
# который выводит информацию о книге. Создайте дочерний класс BorrowableBook, который наследует от класса Book.
# Добавьте атрибут borrower (заимствовавший книгу) и методы borrow_book(user) и return_book(),
# которые позволяют пользователю взять книгу в библиотеке и вернуть ее после использования.

class Book:
    def __init__(self):
        self.__title = 'Martin Eden'
        self.__author = 'Jack London'
        self._status = 'в наличии'

    def display_info(self):
        print(f'Книга: {self.__title}, Автор: {self.__author}, Статус: {self._status}.')


class BorrowableBook(Book):
    def __init__(self, borrower):
        self.__borrower = borrower
        super().__init__()

    def borrow_book(self):
        if self._status == 'в наличии':
            self._status = 'взял' + ' ' + str(self.__borrower)

    def return_book(self):
        self._status = 'в наличии'


print('Сработал класс Book')
book = Book()
book.display_info()
print('Работает класс BorrowableBook(Book)')
user = BorrowableBook('Ivan')
user.borrow_book() # взял книгу
user.display_info()
user.return_book() # вернул книгу
user.display_info()


